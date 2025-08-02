from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()
    #Log user in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #authenticate user
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user=user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.success(request, "There is an error during LogIn")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records })


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged Out..')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully created an account")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You must be logged in to view that page..')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        del_record = Record.objects.get(id=pk)
        del_record.delete()
        messages.success(request, "Record deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to view that page..')
        return redirect('home')
    

@login_required
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            add_record = form.save()

            messages.success(request, 'You have succefully add a new record')
            return redirect('home')
        messages.error(request, 'Error Detected')
    
    return render(request, 'add_record.html', {'form': form})


@login_required
def update_record(request, pk):
    try:
        current_record = Record.objects.get(id=pk)
    except Record.DoesNotExist:
        messages.error(request, 'Record not Found')
        return redirect('home')
    
    form = AddRecordForm(request.POST or None, instance= current_record)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'You have succefully Updated the record')
            return redirect('home')
        messages.error(request, 'Error Detected')
    return render(request, 'update_record.html', {'form': form})



