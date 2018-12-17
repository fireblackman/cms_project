from django.shortcuts import render,redirect
from re_login.models import Register
from re_login.form import UserLogin,UserRegister

import hashlib


# Create your views here.


#创建加密函数
def hash_lib(content):
    hash = hashlib.md5()
    hash.update(content.encode())
    result = hash.hexdigest()
    return  result




#注册
def register(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        namefilter = Register.objects.filter(username=username)
        if len(namefilter) > 0:
            return render(request,'register.html',{'error':'用户名已存在'})
        elif username == '' or len(username.split(' ')) > 1:
            return render(request,'register.html',{'error':'用户名不能为空或含有空格'})
        elif len(username) < 2:
            return render(request,'register.html',{'error':'用户名过短'})

        password = request.POST['upwd']
        password1 = request.POST['upwds']
        if password1 != password:
            return render(request, 'register.html', {'error':'两次输入的密码不一致！'})
        elif len(password) < 6:
            return render(request,'register.html',{'error':'密码长度不足'})

        password = hash_lib(password1)
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        user = Register.objects.create(username=username, password=password, email=email,phone_number=phone_number)
        user.save()
        return render(request, 'success.html', {'username': username, 'operation': '注册'})




#登录
def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid(): #获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = hash_lib(password)
            namefilter = Register.objects.filter(username=username,password=password)
            if len(namefilter) > 0:
                return render(request,'success.html',{'username':username,'operation':'登录'})
            else:
                return render(request, 'login.html', {'error':'该用户名不存在！'})
    else:
        form =UserLogin()
        return render(request,'login.html', {'form':form})