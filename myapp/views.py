from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render
from .models import Property, Unit, Tenant

def property_profile(request, property_id):
    property_obj = Property.objects.get(pk=property_id)
    units = Unit.objects.filter(property=property_obj)
    tenants = Tenant.objects.filter(unit__property=property_obj)
    return render(request, 'property_profile.html', {'property': property_obj, 'units': units, 'tenants': tenants})

def tenant_management(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_management.html', {'tenants': tenants})

def tenant_profile(request, tenant_id):
    tenant_obj = Tenant.objects.get(pk=tenant_id)
    return render(request, 'tenant_profile.html', {'tenant': tenant_obj})
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home') 
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
def home(request):
    return render(request,'Home.html')
def index(request):
    return render(request,'index.html')
