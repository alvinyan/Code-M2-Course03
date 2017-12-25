# -*- coding: utf-8 -*-
'''
    download.py
    ~~~~~~~~~
    
    演示文件下载-接口返回真实文件.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
# 导入request对象
from flask import send_file, send_from_directory, make_response
# 导入os模块库
import os

# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 定义文件下载请求处理函数
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = os.getcwd() + '/Flask Advance/download/'  # 假设在当前目录
    # return send_from_directory(directory, filename, as_attachment=True)

    # 使用make_response()函数创建response对象
    response = make_response(send_from_directory(directory, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}" \
                                              .format(filename.encode().decode('latin-1'))
    return response

# 启动脚本
if __name__ == '__main__':
    app.run()