#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 23:05
# @Author  : yuzhenyu
# @File    : app.py


from flask import Flask, render_template
from apps.admin.views import bp as admin_bp
from apps.common.views import bp as common_bp
from apps.front.views import bp as front_bp
from ext import db


app = Flask(__name__)


def create_app():
    app.register_blueprint(admin_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    app.config.from_object("config")
    db.init_app(app)
    return app

if __name__ == '__main__':
    app=create_app()
    app.run(debug=True)
