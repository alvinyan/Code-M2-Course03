# -*- coding: utf-8 -*-
'''
    ruote_basic.py
    ~~~~~~~~~
    
    演示路由配置的最基本表现形式.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 通过装饰器设置函数URLs访问路径
@app.route('/')
# 定义设置网站首页的处理函数
def index():
    return 'Index Page'

# 通过装饰器设置函数URLs访问路径
@app.route('/hello')
# 定义设置网站首页的处理函数
def hello():
    return '你好，Flask'

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用
