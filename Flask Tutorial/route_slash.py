# -*- coding: utf-8 -*-
'''
    ruote_slash.py
    ~~~~~~~~~
    
    演示路由配置特殊URLs/重定向动作行为.

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

# 定义带有尾斜杠的path路径地址
@app.route('/projects/')
def projects():
    return 'The project page'

# 定义不携带尾斜杠的path路径地址
@app.route('/about')
def about():
    return 'The about page'

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用