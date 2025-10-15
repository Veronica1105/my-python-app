from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义一个路由，意思是当有人访问网站根目录 ("/") 时，执行下面的函数
@app.route('/')
def hello_world():
    # 这个函数返回一个字符串，这个字符串就是用户在浏览器上看到的内容
    return 'Hello from Jenkins CI/CD v3.0! 2025/10/15' # 以后你可以修改这里的版本号来测试

# 这是一个标准的 Python 写法，意思是如果这个文件是直接被运行的，
# 而不是被其他文件导入的，就执行下面的代码
if __name__ == '__main__':
    # 启动这个 Web 应用
    # host='0.0.0.0' 让你的应用可以被局域网内的其他设备访问
    # port=5000 指定应用在 5000 端口上运行
    app.run(host='0.0.0.0', port=5000)

