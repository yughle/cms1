#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 23:06
# @Author  : yuzhenyu
# @File    : manager.py

from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from app import create_app
from ext import db
from apps.admin import models as admin_models


app=create_app()
manager=Manager(app)
Migrate(app.db)
manager.add_command("db", MigrateCommand)

@manager.option("-u", "--username", dest="username")
@manager.option("-p", "--password", dest="password")
@manager.option("-e", "--email", dest="email")
def create_user(username, passwoed, email):
    user=admin_models.User(username=username, passwoed=passwoed, email=email)
    db.session.add(user)
    db.session.commit()
    
    
if __name__ == '__main__':
    app.run(debug=True)