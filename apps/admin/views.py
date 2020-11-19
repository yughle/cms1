#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/11/18 20:26 
# filename: views.py
# development_tool： PyCharm

from flask import Blueprint
from flask import render_template


bp=Blueprint("admin", __name__)

@bp.route("/admin", methods=["GET"])
def index():
    return render_template('admin/login.html')
