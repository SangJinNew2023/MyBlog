from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .forms import UserForm
from myboard.models import Category
from django.contrib.auth.views import LoginView

# Create your views here.
# def login(request):
#     category = Category.objects.order_by('id')
#     if request.method == "POST":
#         form = LogInForm(request.POST)
#         if form.is_valid():
#             return render(request, 'myboard_users/login.html', {'form': form, 'category': category})
#     else:
#         form = LoginView()
#     category = Category.objects.order_by('id')
#     return render(request, 'myboard_users/login.html', {'form': form, 'category': category})



def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #Get the each data('username') from form
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #user authentication
            login(request, user) #login
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'myboard_users/signup.html', {'form': form})

def page_not_found(request, exception):
    return render(request, 'myboard_users/404.html', {})

def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Password Request'
                    email_template_name = 'myboard_users/password_message.txt'
                    parameters = {
                        'email': user.email,
                        'domain': '127.0.0.1',
                        'site_name':'MyBoard',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol' : 'http',
                    }
                    email = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email, '', [user.email], fail_silently=False)
                    except:
                        return HttpResponse('Invaild Header')
                    return redirect('password_reset_done')
    else:
        password_form = PasswordResetForm()
    context = {
        'password_form': password_form,
    }
    return render(request, 'myboard_users/password_reset.html', context)
