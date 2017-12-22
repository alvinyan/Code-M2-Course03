# -*- coding: utf-8 -*-
'''
    search.py
    ~~~~~~~~~
    
    演示静态HTML模板数据提交POST方式.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
# 导入request对象
from flask import request, render_template
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 定义搜索请求处理函数
@app.route('/search', methods=['GET', 'POST'])
def search():
    # 判断是否为POST请求访问
    if request.method == 'POST':
        # 处理POST请求数据
        keyword = request.form['keyword'] # 接受表单数据keyword
        return '您搜索的关键字：%s' % keyword 
    else: # 否则为GET请求
        # GET请求则返回搜索表单页面(请求转发模式)
        return render_template('search.html')

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用
