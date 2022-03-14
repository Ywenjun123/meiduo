from django.shortcuts import render,redirect
from django.views import View
from django import http
from apps.users.models import User
from django.urls import reverse
import re
import logging


logger = logging.getLogger('django')
# Create your views here.
class RegisterView(View):
 

    """
    1.用户名我们需要判断是否重复(这个要开发一个视图)
            用户名的长度有5-20个的要求
    2.密码 有长度的限制 8-20 要求为 字母,数字,_
    3.确认密码 和密码一致
    4.手机号   手机号得先满足规则
        再判断手机号是否重复
    5.图片验证码是一个后端功能
        图片验证码是为了防止 计算机攻击我们发送短信的功能
    6.短信发送
    7.必须同意协议
    8.注册也是一个功能


    必须要和后端交互的是:
        1.用户名/手机号是否重复
        2.图片验证码
        3.短信
        4.注册功能
    """
    
    def get(self,request):

        return render(request,'register.html')

    def post(self,request):
        """
        1.接收前端提交的用户名,密码和手机号
        2.数据的验证(我们不相信前端提交的任何数据)
            2.1 验证比传(必须要让前端传递给后端)的数据是否有值
            2.2 判断用户名是否符合规则
            2.3 判断密码是否 符合规则
            2.4 判断确认密码和密码是否一致
            2.5 判断手机号是否符合规则
        3.验证数据没有问题才入库
        4.返回响应
        """
         # 1.接收前端提交的用户名,密码和手机号
        data = request.POST
        username=data.get('username')
        passwrod=data.get('password')
        passwrod2=data.get('password2')
        mobile=data.get('mobile')
        # 2.数据的验证(我们不相信前端提交的任何数据)
        #     2.1 验证必传(必须要让前端传递给后端)的数据是否有值
        # all([el,el,el]) el必须有值 只要有一个为None 则为False
        if not all([username,passwrod,passwrod2,mobile]):
            return http.HttpResponseBadRequest('参数有问题')
        #     2.2 判断用户名是否符合规则 判断 5-20位 数字 字母 _
        if not re.match(r'[0-9a-zA-Z_]{5,20}',username):
            return http.HttpResponseBadRequest('用户名不合法')
        #     2.3 判断密码是否 符合规则
        if not re.match(r'[0-9a-zA-Z_]{8,20}',passwrod):
            return http.HttpResponseBadRequest('密码不合法')
        #     2.4 判断确认密码和密码是否一致
        if passwrod != passwrod2:
            return http.HttpResponseBadRequest('密码不一致')
        #     2.5 判断手机号是否符合规则
        if not re.match(r'1[3-9]\d{9}',mobile):
            return http.HttpResponseBadRequest('手机号不符合规则')
        # 2.6 验证同意协议是否勾选(作业)

        # 3.验证数据没有问题才入库
        # 当我们在操作外界资源(mysql,redis,file)的时候,我们最好进行 try except的异常处理
        # User.objects.create  直接入库 理论是没问题的 但是 大家会发现 密码是明文
        try:
            user = User.objects.create_user(username=username,password=passwrod,mobile=mobile)
        except Exception as e:
            logger.error(e)
            return render(request,'register.html',context={'error_message':'数据库异常'})
            return http.HttpResponseBadRequest('数据库异常')

        # 4.返回响应, 跳转到首页

        # 注册完成之后,默认认为用户已经登陆了
        # 保持登陆的状态
        # session
        # 自己实现request.session

        # 系统也能自己去帮助我们实现 登陆状态的保持
        # from django.contrib.auth import login
        # login(request,user)

        return redirect(reverse('contents:index'))
        # return http.HttpResponse('注册成功')
        pass