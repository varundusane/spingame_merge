from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.shortcuts import render, redirect
from django.contrib import messages

from player.models import Player
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


# def login(request):
#     pr = Profile.objects.get(user=request.user)
#     if request.user.is_authenticated and pr.is_agent:
#         print(request.user)
#         return redirect('jobseeker:jobseeker_home')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('pass')

#             # print(username)
#             # print(password)
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 pr = Profile.objects.get(user=user)
#                 if pr.is_agent:
#                     login(request, user)
#                     if 'next' in request.POST:
#                         return redirect(request.POST.get('next'))
#                     else:
#                         return redirect('agent:agent_home')
#                 else:
#                     messages.info(request, 'This Agent Login')
#             else:
#                 messages.info(request, 'Username OR password is incorrect')

#         context = {}

#     return render(request, 'account/login_agent.html', context)


def register(request):
    form = RegisterForm()
    # if request.method == 'GET':
    #     context = {'form': form}
    #     return render(request, 'register.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # form.save()

            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            nickname = form.cleaned_data.get('nickname')
            password1 = form.cleaned_data.get('password1')
            user.save()
            pr = Player(user=user, nickname=nickname, password1=password1)
            pr.save()
            new_user = authenticate(username=username, password=password1)
            if new_user is not None:
                login(request, new_user)
            else:
                form = RegisterForm()
        return render(request, 'register.html')
    else:
        print('Form is not valid')
        print(form.errors.as_data())
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
    return render(request, 'register.html', context)

    return render(request, 'register.html', {})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(Dashboard)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

# def login(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("main:homepage")
# 			else:
# 				messages.error(request, "Invalid username or password.")
#         else:
# 			messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="login.html", context={"login_form":form})
    
    # pr = Player.objects.get(user=request.user)
    # if request.user.is_authenticated:
    #     print(request.user)
    #     return redirect('dashboard.html')
    # else:
        # if request.method == 'POST':
        #     username = request.POST.get('username')
        #     password = request.POST.get('password1')

            # print(username)
            # print(password)
        #     user = authenticate(request, username=username, password=password)

        #     if user is not None:
        #         pr = Player.objects.get(user=user)
                
        #         login(request, user)
        #         return redirect('dashboard.html')
                
        #     else:
        #         messages.info(request, 'Username OR password is incorrect')

        # context = {}

        # return render(request, 'login.html', context)

def Dashboard(request):
    return render(request, 'dashboard.html')

def Game(request):
    return render(request, 'game.html')