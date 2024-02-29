from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, skillsearch

migrate = Migrate(app, skillsearch)
manager = Manager(app)

manager.add_command('skillsearch', MigrateCommand)

if __name__ == '__main__':
    manager.run()