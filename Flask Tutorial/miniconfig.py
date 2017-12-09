# -*- coding: utf-8 -*-
'''
    miniconfig.py 脚本
    ~~~~~~~~~
    
    演示Flask配置模式（直接写入脚本）.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
# 创建Flask类实例app
app = Flask(__name__)

'''
脚本中直接写入
使用app.config['key']=value 配置
'''
app.config['SECRET_KEY'] = 'some secret words'
app.config['DEBUG'] = True
app.config['ITEMS_PER_PAGE'] = 10

'''
脚本直接写入
使用 app.config.update()配置更加精简
'''
app.config.update(
    SECRET_KEY = 'some secret words',
    DEBUG = True,
    ITEMS_PER_PAGE = 10,
)



