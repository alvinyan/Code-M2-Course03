# -*- coding: utf-8 -*-
'''
    ruote_urlfor.py
    ~~~~~~~~~
    
    演示URL构建方式相互调用.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
from flask import redirect, url_for
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 定义访问项目根目录的请求处理函数
@app.route('/')
def index():
    return 'Index Page'

# 定义不携带尾斜杠的path路径地址
@app.route('/add')
def add():
    print('do add operation……')
    return 'The about page'

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用