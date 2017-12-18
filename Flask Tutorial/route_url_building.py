# -*- coding: utf-8 -*-
'''
    ruote_url_building.py
    ~~~~~~~~~
    
    演示路由URL构建模式.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类,url_for函数
from flask import Flask, url_for
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(usenrame): pass

# 使用with关键字调用url_for()函数构建URLs路径
with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login', next='/'))
    print (url_for('profile', username='John Doe'))

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用