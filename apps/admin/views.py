#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/11/18 20:26 
# filename: views.py
# development_tool： PyCharm

from flask import Blueprint, render_template, session, request, redirect, url_for
from .models import Users
from .forms import LoginForm


bp=Blueprint("admin", __name__, url_prefix="/admin")

@bp.route("/login", methods=["GET", "POST"])
def login():
    form=LoginForm(request.form)
    if form.validate():
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
            
@bp.route("/")
def index():
    return render_template("admin/login.html")
