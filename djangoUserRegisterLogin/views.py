# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from MangeOS.modules.regist import token_confirm
from django.core.mail import send_mail
import json
from settings import EMAIL_HOST_USER
from settings import DEPLOY_IP
import json
import time
from token import token_confirm

@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method != 'POST':
        print('12222222222')
        return render(request, 'accounts/login.html')
        # return render(request, 'index.html')

    print('333333333333333')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is None:
        login_err = "Wrong username or password!"
        return render(request, 'accounts/login.html', {'login_err': login_err})

    if user.is_active:
        auth_login(request, user)
        # return render(request, 'index.html')
        # login(request, user)
        print('444444444')
        return HttpResponseRedirect('/')
    else:
        login_err = "You are disabled account!"
        return render(request, 'accounts/login.html', {'login_err': login_err})

    # retuddrn render(request, 'index.html')

def register(request):

    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    date_join = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    try:
        user = User.objects.filter(username=username).values('username').first()['username']

    except:
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        is_active=True,
                                        # is_active=False,
                                        date_joined=date_join)
        user.save()

    print('11111111111111111111')
    return HttpResponseRedirect('/')
    # return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

def forget_pass(request):
    return render(request, 'accounts/resetpass.html')


def active_user(request,token):
    try:
        username = token_confirm.confirm_validate_token(token)
    except:
        return HttpResponse(u'对不起，验证链接已经过期')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(u'对不起，您所验证的用户不存在，请重新注册')

    user.is_active = True
    user.save()
    confirm = u'验证成功，请进行登录操作。'

    return HttpResponseRedirect('/accounts/login',{'confirm':confirm})

def reset_pass(request):
    email = request.POST.get('email')
    token = token_confirm.generate_validate_token(email)
    message = "\n".join(
        [u'{0},Hello'.format(email), u'请访问该链接，完成密码更改:', '/'.join([DEPLOY_IP, 'accounts/change_pass', token])])
    subject = u'ManageOS用户密码更新提示'
    send_mail(subject, message, EMAIL_HOST_USER, [email])
    return HttpResponse(u"验证信息已发送到邮箱，请及时登录,有效期为1个小时!")

def change_pass(request,token):
    return render(request, 'accounts/new_pass.html',{'token':token})

def do_change_pass(request):
    token = request.POST.get('token')
    new_password = request.POST.get('new_password')
    ac_new_password = request.POST.get('ac_new_password')

    if new_password != ac_new_password:
        return render(request, 'accounts/new_pass.html', {token: token})

    try:
        email = token_confirm.confirm_validate_token(token)
    except:
        return HttpResponse(u'对不起，验证链接已经过期')

    user = User.objects.get(email=email)
    user.set_password(new_password)
    user.save()
    confirm = u'密码更新成功，请进行登录操作。'
    return HttpResponseRedirect('/accounts/login', {'confirm': confirm})


