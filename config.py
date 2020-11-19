#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/11/18 20:24 
# filename: config.py
# development_tool： PyCharm


host="localhost"
port=3306
account="root"
password="qweasd@753.."
db_name="db"
db_url="mysql+pymysql://{}:{}@{}:{}/{}charset=utf-8".format(account, password, host, port, db_name)
SQLALCHEMY_DATABASE_URL=db_url
SQLALCHEMY_TRACK_MODIFICATTIONS=False