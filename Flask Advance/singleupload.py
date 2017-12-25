# -*- coding: utf-8 -*-
'''
    singleupload.py
    ~~~~~~~~~
    
    演示文件上传.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
# 导入request对象
from flask import render_template, request
import os
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 定义文件上传请求处理函数
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # 获取上传文件对象
        f = request.files['uploadfile']
        # 获取上传文件路径
        uploadpath = os.path.dirname(os.path.realpath(__file__))
        # 上传文件
        f.save(uploadpath + '/upload/' + f.filename)
        return "文件上传成功"
    else:
        # 跳转至上传页面
        return render_template('singleupload.html')

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用