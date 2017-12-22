# -*- coding: utf-8 -*-
'''
    staticfile.py
    ~~~~~~~~~
    
    演示静态文件的使用方法.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类,render_template对象
from flask import Flask, render_template
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 定义函数的Urls地址为一下任何一种方式均可接受
@app.route('/hello')
@app.route('/hello/<name>')
# 定义hello函数，并设置name关键字参数（默认为None）
def hello(name=None):
    # 返回静态页面
    return render_template('helloFlask.html', name=name)

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用