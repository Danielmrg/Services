from django.shortcuts import render , redirect , HttpResponse , get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user , unauthenticated_user
from django.contrib import messages
from .filters import ReqFilter ,CatFilter
from .forms import *
from .models import *


# Create your views here.

# ---------- home views -----------------#
def home(request):
    tags=Tag.objects.all()
    categorys=Category.objects.all()
    myfilter=CatFilter(request.GET,queryset=categorys)
    categorys=myfilter.qs
    context={
        'tags':tags,
        'categorys':categorys,
        'myfilter':myfilter,
    }
    return render(request,'home/home.html',context)

def category(request,title):
    tags=Tag.objects.all()
    experts=Expert.objects.filter(category=title)
    context={
        'tags':tags,
        'experts':experts,
    }
    return render(request,'home/category.html',context)

# ---------- expert views -----------------#
@login_required(login_url='login')
@allowed_user(allowed_roles=['expert'])
def dashboard(request):
    Requests = request.user.expert.request_srv_set.all()
    myfilter=ReqFilter(request.GET,queryset=Requests)
    Requests=myfilter.qs
    context={
        'Requests':Requests,
        'myfilter':myfilter,
    }
    return render(request,'dashboard/dashboard.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['expert'])
def expert_update(request):
    user=request.user.expert
    form=ExpertForm(instance=user)
    if request.method == 'POST':
        form = ExpertForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت بروزرسانی شد.')
            return redirect('dashboard')
    context={
        'form':form
    }
    return render(request,'dashboard/form.html',context)

# ---------- Customer views -----------------#
@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def profile(request):
    Requests = request.user.customer.request_srv_set.all()
    myfilter=ReqFilter(request.GET,queryset=Requests)
    Requests=myfilter.qs
    context={
        'Requests':Requests,
        'myfilter':myfilter,
    }
    return render(request,'profile/profile.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def customer_update(request):
    user=request.user.customer
    form=CustomerForm(instance=user)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما با موفقیت بروزرسانی شد.')
            return redirect('profile')
    context={
        'form':form
    }
    return render(request,'profile/form.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def request_srv(request,expert):
    expert=Expert.objects.get(id=expert)
    customer=request.user.customer
    form=ReqForm(initial={'expert':expert,'customer':customer})
    if request.method=="POST":
        form=ReqForm(request.POST,initial={'expert':expert,'customer':customer})
        if form.is_valid():
            form.save()
            messages.success(request,'درخواست شما با موفقیت ثبت شد.')
            return redirect('profile')
    context={
        'form':form,
    }
    return render(request,'profile/Request.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def upadte_request(request,pk):
    Request=Request_srv.objects.get(id=pk)
    form = ReqForm(instance=Request)
    if request.method == 'POST':
        form = ReqForm(request.POST,instance=Request)
        if form.is_valid():
            form.save()
            messages.success(request,'درخواست شما با موفقیت بروزرسانی شد.')
            return redirect('profile')
    context={
        'form':form,
    }
    return render(request,'profile/Request.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def delete_request(request,pk):
    Request=Request_srv.objects.get(id=pk)
    Request.delete()
    messages.success(request,'در خواست شما با موفقیت حذف شد')
    return redirect('profile')

# ---------- regestration views -----------------#
@unauthenticated_user
def signup_customer(request):
    form=RegisterationForm()
    if request.method =="POST":
        form=RegisterationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                username=username,
                email=email,
            )
            messages.success(request,'حساب شما به عنوان یک مشتری ایجاد شد.')
            return redirect('login')
    context={
        'form':form,
    }   
    
    return render(request,'contrib/signup.html',context)

@unauthenticated_user
def signup_expert(request):
    form=RegisterationForm()
    if request.method =="POST":
        form=RegisterationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            group=Group.objects.get(name='expert')
            user.groups.add(group)
            Expert.objects.create(
                user=user,
                username=username,
                email=email,
            )
            messages.success(request,'حساب شما به عنوان یک متخصص ثبت شد.')
            return redirect('login')
    context={
        'form':form,
    }   
    
    return render(request,'contrib/signup.html',context)

@unauthenticated_user
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request , 'نام کاربری یا رمز عبور اشتباه است.')
        
    return render(request,'contrib/login.html')

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    messages.success(request,'شما از حساب خود خارج شده اید.')
    return redirect('login')