from django.shortcuts import render, redirect
from app.models import Slider, Banner_Area, Main_Category, Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def BASE(request):
    return render(request, 'base.html')


def Home(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]
    banner = Banner_Area.objects.all().order_by('-id')[0:3]

    main_category = Main_Category.objects.all()
    product = Product.objects.filter(section__name="Top Deals of The Day")
    context = {
        'sliders': sliders,
        'banner': banner,
        'main_category': main_category,
        'product': product,
    }
    return render(request, 'main/home.html', context)


def Product_Details(request, slug):
    product = Product.objects.filter(slug=slug)
    if product.exists():
        product = Product.objects.get(slug=slug)
    else:
        return redirect('404')

    context = {
        'product': product
    }
    return render(request, 'product/product_detail.html', context)


def Error404(request):
    return render(request, 'errors/404.html')


def My_Account(request):
    return render(request, 'account/my_account.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(
            username=username,
            email=email,

        )
        user.set_password(password)
        user.save()
        return redirect('my_account')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('my_account')
    return render(request, 'account/my_account.html')
