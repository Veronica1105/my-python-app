# 告诉 Docker，我们的应用需要在一个已经安装了 Python 3.9 的轻量级环境里运行
FROM python:3.9-slim

# 在容器（未来的运行环境）里创建一个叫 /app 的工作目录
WORKDIR /app

# 把我们本地的 requirements.txt 文件复制到容器的 /app 目录里
COPY requirements.txt .

# 在容器里运行 pip 命令，根据 requirements.txt 来安装依赖库
RUN pip install --no-cache-dir -r requirements.txt

# 把本地项目文件夹里的所有文件（. 代表所有）都复制到容器的 /app 目录里
COPY . .

# 告诉 Docker，我们的应用会使用 5000 端口
EXPOSE 5000

# 定义当容器启动时，需要执行的默认命令： "python app.py"
CMD ["python", "app.py"]
    