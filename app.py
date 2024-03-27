from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义一个路由，当访问根路径时返回一个简单的欢迎消息
@app.route('/')
def hello():
    return 'Hello, World!'

# 运行应用
if __name__ == '__main__':
    app.run(debug=True)  # 启动 Flask 应用，开启调试模式
