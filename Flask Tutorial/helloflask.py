# -*- coding: utf-8 -*-
'''
    helloflask.py
    ~~~~~~~~~
    
    演示快速创建Flask应用项目.

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

'''
# 导入config.py脚本
import config
# 导入config.py配置脚本
app.config.from_object(config)

# 导入multiconfig脚本中的config字典对象
from multiconfig import config
# 导入开发模式配置
app.config.from_object(config['development'])
'''

# 通过装饰器设置函数URLs访问路径
@app.route('/')
# 定义设置网站首页的处理函数
def gotoIndex():
    res = 5 / 1 # 除零错误代码
    # 浏览器输出
    return '你好，Flask!'

# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用
