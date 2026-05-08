from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . forms import ProfileForm
from accounts.forms import RegisterForm
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def register(request):
    if request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = RegisterForm()
    return render(request, 'register.html', {'form': fm})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request=request,
            data=request.POST
        )
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {
        'form': form
    })





def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def profileView(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form=ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form, 'profile': profile})



# def profileView(request):

#     profile, created = UserProfile.objects.get_or_create(
#         user=request.user
#     )

#     if request.method == 'POST':

#         form = ProfileForm(
#             request.POST,
#             request.FILES,
#             instance=profile
#         )

#         if form.is_valid():

#             form.save()

#             return redirect('/profile/')

#     else:

#         form = ProfileForm(instance=profile)

#     return render(request, 'profile.html', {
#         'form': form
#     })


# def profileView(request):

#     profile = UserProfile.objects.get(user=request.user)

#     if request.method == 'POST':

#         form = ProfileForm(
#             request.POST,
#             request.FILES,
#             instance=profile
#         )

#         if form.is_valid():
#             form.save()
#             return redirect('profile')

#     else:

#         form = ProfileForm(instance=profile)

#     return render(
#         request,
#         'profile.html',
#         {'form': form}
#     )