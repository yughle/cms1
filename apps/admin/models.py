#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 23:02
# @Author  : yuzhenyu
# @File    : models.py


from ext import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "jg_user"
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)