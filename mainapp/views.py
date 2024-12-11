from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Stocks
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from yahoo_fin.stock_info import get_live_price
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from django.contrib.auth.models import User

# Fetch cryptocurrency price from Binance API
def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return float(data['price'])
    except Exception:
        return None

# API to fetch live stock/crypto prices
@csrf_exempt
def stockpriceapi(request):
    if request.method == "POST":
        try:
            stock = request.POST.get('stock')
            if stock.endswith("USDT"):  # Determine if it's a cryptocurrency
                price = get_crypto_price(stock)
            else:  # Assume it's a stock
                price = get_live_price(stock)
            
            if price is not None:
                return JsonResponse({'price': round(price, 4)})
            else:
                return JsonResponse({'error': 'Invalid symbol or API error'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def charts(request):
    selected_ticker = "NASDAQ:AAPL"
    if request.method == "POST":
        selected_ticker = request.POST.get('ticker', selected_ticker)
    
    context = {
        'selected_ticker': selected_ticker
    }
    return render(request, 'charts.html', context)

@login_required(login_url='login')
def instructions(request):
    return render(request, 'instructions.html')

@login_required(login_url='login')
def sell(request, pk):
    stock = get_object_or_404(Stocks, pk=pk, user=request.user)
    if stock.state != "sold":
        price = get_crypto_price(stock.title) if stock.title.endswith("USDT") else get_live_price(stock.title)
        if price is not None:
            stock.state = "sold"
            stock.sold_price = price
            stock.profit = round(stock.quantity * (price - stock.bought_price), 4)
            stock.save()
            userprofile = UserProfile.objects.get(user=request.user)
            userprofile.balance = round((userprofile.balance + stock.quantity * price), 4)
            userprofile.save()
    return redirect('profile')

@login_required(login_url='login')
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    active_user_stocks = Stocks.objects.filter(user=request.user, state='active')
    history_user_stocks = Stocks.objects.filter(user=request.user, state='sold')
    userprofiles = UserProfile.objects.all().order_by('-balance')

    error = ''
    if request.method == 'POST':
        assetsymbol = request.POST.get('assetsymbol')
        quantity = int(request.POST.get('quantity'))
        try:
            # Fetch price based on asset type
            bought_price = get_crypto_price(assetsymbol) if assetsymbol.endswith("USDT") else get_live_price(assetsymbol)
            if bought_price is None:
                raise ValueError("Price could not be retrieved.")
        except Exception:
            error = "Failed to fetch the asset price."
            bought_price = None

        if bought_price and userprofile.balance > (bought_price * quantity):
            Stocks.objects.create(user=request.user, title=assetsymbol, quantity=quantity, bought_price=bought_price, state='active')
            userprofile.balance = round(userprofile.balance - (bought_price * quantity), 4)
            userprofile.save()
        else:
            error = error or "You don't have enough balance."

        active_user_stocks = Stocks.objects.filter(user=request.user, state='active')
        history_user_stocks = Stocks.objects.filter(user=request.user, state='sold')

    context = {
        'userprofile': userprofile,
        'history_user_stocks': history_user_stocks,
        'active_user_stocks': active_user_stocks,
        'userprofiles': userprofiles,
        'error': error
    }
    return render(request, 'profile.html', context)

def loginsystem(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Incorrect username or password'})

@login_required(login_url='login')
def logoutsystem(request):
    if request.method == "GET":
        logout(request)
        return redirect('login')

def signupsystem(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "GET":
        return render(request, 'registration.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'registration.html', {'form': UserCreationForm(), 'error': 'Passwords don\'t match!'})
        else:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                user_profile = UserProfile.objects.create(user=request.user)
                user_profile.participants = request.POST.get('participants', '')
                user_profile.name = request.POST.get('name', '')
                user_profile.is_group = request.POST.get('is_group', '') == 'group'
                user_profile.save()
                return redirect('profile')
            except IntegrityError:
                return render(request, 'registration.html', {'form': UserCreationForm(), 'error': 'Username is already taken!'})
