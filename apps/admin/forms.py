#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 23:02
# @Author  : yuzhenyu
# @File    : forms.py

from wtforms import Form
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Length, Email


class LoginForm(Form):
    username=StringField(label="用户名", validators=[InputRequired("用户名为必填项"),Length(4, 20, '用户名长度为4到20位')])
    password=StringField(label="密码", validators=[InputRequired("密码为必填项"),Length(6, 9, '用户名长度为6到9位')])
    
