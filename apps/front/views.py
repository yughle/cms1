#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 23:04
# @Author  : yuzhenyu
# @File    : views.py


from flask import Blueprint

bp=Blueprint("front", __name__)

@bp.route("/")
def index():
    return "这是前台首页"