#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 23:02
# @Author  : yuzhenyu
# @File    : models.py


from ext import db

from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = "jg_user"
    __password = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, raw_password):
        self.__password=generate_password_hash(raw_password)
        
    def check_password(self, raw_password):
        result=check_password_hash(self.password, raw_password)
        return result