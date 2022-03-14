from django.db import models

"""
1. 自己定义模型
    class User(models.Model):
        username=
        password=
        mobile=

    密码是明文,我们自己要完成验证 等等一些问题

2. 我们发现我们在学习基础的时候 django自带了 admin后台管理
    admin 后台管理 也有用户信息的保存和认证 密码是密文,也可以验证用户信息

   我们就想用户 django自带的用户模型


"""
from django.contrib.auth.models import AbstractUser

"""
当系统的类/方法不能满足我们需求的时候,我们就继承/重写
# """
class User(AbstractUser):

    mobile=models.CharField(max_length=11,unique=True,verbose_name='手机号')
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username




# class Person(object):
#
#     name = ''
#     sex = ''
#     age =''
#
#
# class Man(Person):
#
#     weigth=''
#
#     pass



