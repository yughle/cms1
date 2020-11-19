#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/11/18 20:26 
# filename: views.py
# development_tool： PyCharm

from flask import Blueprint


bp=Blueprint("admin", __name__)

@bp.route("/admin")
def index():
    return "这是后台首页"