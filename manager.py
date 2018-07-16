from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps import create_app
from apps.models.base import db

# 先创建app
app = create_app()
migrate = Migrate(app, db)

# 再用manager进行接管
manager = Manager(app)
# 注册迁移命令
manager.add_command('db', MigrateCommand)


# 如果是主文件，把当前文件当做web服务器使用的话
if __name__ == '__main__':
    manager.run()
