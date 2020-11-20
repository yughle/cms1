#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/11/18 20:26 
# filename: views.py
# development_tool： PyCharm
from io import BytesIO
from flask import Blueprint, render_template, session, request, redirect, url_for, make_response

from apps.admin.models import Users
from apps.admin.forms import LoginForm
from utils.captcha import create_validete_code


bp=Blueprint("admin", __name__, url_prefix="/admin")

@bp.route("/login", methods=["GET", "POST"])
def login():
    form=LoginForm(request.form)
    if form.validate():
        captcha=request.form.get("captcha")
        if session.get("image").lower() != captcha.lower():
            return render_template("admin/login.html", message="验证码错误")
        if request.method == "GET":
            return render_template("admin/login.html")
        else:
            user=request.form.get("username")
            pwd=request.form.get("password")
            users=Users.query.filter_by(username=user).first()
            if users:
                if user==users and users.check_password(pwd):
                    session["uid"]=users.uid
                    return redirect(url_for('admin/index.html'))
                else:
                    return render_template('admin/login.html', message="您输入的账号或密码错误，请重新输入")
            else:
                return render_template('admin/login.html', message="您输入的账号或密码错误，请重新输入")
    else:
        return render_template("admin/login.html", message=form.errors)
            
@bp.route("/code")
def get_code():
    code_img, strs=create_validete_code()
    buf=BytesIO()
    code_img.save(buf, "JPEG", quality=70)
    buf_str=buf.getvalue()
    response=make_response(buf_str)
    response.headers["Content-Type"]="image/jpeg"
    #将验证码字符串存在session中
    session["image"]=strs
    return response