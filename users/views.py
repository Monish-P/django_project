from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid(): #is_valid() checks the entered data is valid
            form.save()
            #cleaned_data is a dictionary containing the valid data , and we are getting the username as key by get()
            messages.success(request,'Your account has beeen created ! You are now able to log in')
            return redirect('login')
        else:
            messages.error(request,'Please enter valid details')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

def profile(request):
    if request.method=='POST':
        u_update=UserUpdateForm(request.POST,instance=request.user)
        #instance=request.user means the present instance of the user will be displayed on the form
        p_update=ProfileUpdateForm(request.POST,request.FILES)
        if u_update.is_valid() and p_update.is_valid():
            u_update.save()
            p_update.save()
            messages.success(request,'Your details have been updated.')
            return redirect('profile')
    else:
        u_update=UserUpdateForm(instance=request.user)
        p_update=ProfileUpdateForm()

    context={
        'u_update':u_update,
        'p_update':p_update
    }
    return render(request,'users/profile.html',context)

