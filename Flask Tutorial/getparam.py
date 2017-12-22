# -*- coding: utf-8 -*-
'''
    getparam.py
    ~~~~~~~~~
    
    演示接受GET请求参数问号传参处理.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
# 导入request请求对象
from flask import request
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 定义按主键删除用户信息的请求处理函数
@app.route('/usermanager/delete/')
def userdelete():
    # 接受客户端参数,类型转换
    userid = int(request.args.get('userid'))
    # 浏览器输出
    return '删除 userid: %d' % userid

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用
