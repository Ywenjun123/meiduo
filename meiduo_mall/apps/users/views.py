from django.shortcuts import render,HttpResponse
from django.views import View

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
        2.入库
        3.返回相应
        """
        pass