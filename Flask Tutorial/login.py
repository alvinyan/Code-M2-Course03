# -*- coding: utf-8 -*-
'''
    login.py
    ~~~~~~~~~
    
    演示表单POST提交处理.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入flask模块库中的Flask类
from flask import Flask
# 导入处理对象
from flask import render_template, request, redirect, url_for, session
# 导入werkzeug安全模块security
from werkzeug.security import generate_password_hash, check_password_hash
# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '123456'

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    # 若为POST模式提交则处理请求参数
    if request.method == 'POST':
        # 加密后的密码
        pw_hash = generate_password_hash(request.form['password'])
        print('加密后的密码：%s' % pw_hash)    
        pw_hash = 'pbkdf2:sha256:50000$nRpndPFw$f08e7bcc0874043c0a2f5a9d01f7561548a7e047b0ffee1504d9153231f77e45'
        flag = check_password_hash(pw_hash, request.form['password'])
        print(flag)
        # 判断账号和密码是否正确
        if request.form['account'] == 'admin' and check_password_hash(pw_hash, request.form['password']):
            session['account'] = request.form['account']
            return redirect(url_for('home'))
        else:
            error = "登录失败"
    # 使用GET访问则返回登陆表单
    return render_template('login.html', error = error)

@app.route('/home')
def home():
    account = session.get('account', None)
    #return render_template('home.html', account = request.args.get('account'))
    return render_template('home.html', account = account)

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用
