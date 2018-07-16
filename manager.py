from flask_script import Manager

from apps import create_app

# 先创建app
app = create_app()

# 再用manager进行接管
manager = Manager(app)


# 如果是主文件，把当前文件当做web服务器使用的话
if __name__ == '__main__':
    manager.run()
