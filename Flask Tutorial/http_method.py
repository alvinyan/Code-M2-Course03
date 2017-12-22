# -*- coding: utf-8 -*-
'''
    http_method.py
    ~~~~~~~~~
    
    演示HTTP提交方法的使用.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类,request对象
from flask import Flask, request
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 说那个methods属性设置该地址可以通过GET和POST两种方式访问
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return '使用POST方式访问Urls'
    else:
        return '使用非POST方式访问Urls'

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用