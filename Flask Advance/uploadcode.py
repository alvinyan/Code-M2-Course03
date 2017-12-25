# -*- coding: utf-8 -*-
'''
    uploadcode.py
    ~~~~~~~~~
    
    演示文件上传原生方式实现完整示例.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
# 导入request对象
from flask import request, render_template, url_for, send_from_directory
# 导入os系统模块库
import os
# 导入werkzeug中的 secure_filename
from werkzeug import secure_filename

# 设置文件上传参数
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# 创建Flask类实例app
app = Flask(__name__)
# 设置上传文件服务器文件夹
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/Flask Advance/upload/'
# 设置上传文件大小限制
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

'''
 定义验证上传文件后缀名的脚本函数
'''
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

'''
 获取上传文件服务器地址的脚本函数
'''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


'''
 定义处理客户端上传请求的函数
'''
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    error = ''
    # POST方式提交
    if request.method == 'POST':
        file = request.files['uploadfile']
        # 判断客户端上传文件是否存在并且扩展名符合限制要求
        if file and allowed_file(file.filename):
            # 为上传文件名称加密
            filename = secure_filename(file.filename)
            # 调用save方法完成文件写入服务器指定地址
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # 获取上传文件的地址
            file_url = url_for('uploaded_file', filename=filename)
            # 输出显示
            return '图片上传成功!<br><img src=' + file_url + '>'
        else:
            error = '错误:上传文件类型错误!(允许后缀名：jpg、jpeg、png、gif)'
            return render_template('uploadcode.html', error = error)
    # GET方式提交
    return render_template('uploadcode.html')

# 启动脚本
if __name__ == '__main__':
    app.run()

