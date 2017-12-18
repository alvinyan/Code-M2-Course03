# -*- coding: utf-8 -*-
'''
    ruote_variable.py
    ~~~~~~~~~
    
    演示路由配置变量规则.

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

# 通过装饰器设置函数URLs访问路径并携带参数
@app.route('/user/<username>')
# 定义显示用户信息的处理函数
def show_user_profile(username):
    # 页面显示用户姓名
    return '用户姓名：%s' % username

# 通过装饰器设置函数URLs访问路径并携带参数
@app.route('/post/<int:post_id>')
# 定义显示帖子编号的处理函数
def show_post(post_id):
    # 页面显示用户姓名
    return '帖子编号：%d' % post_id

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用