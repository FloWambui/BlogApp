from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Quote,Role,Blog
from  flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect
import app



# Creating app instance
app = create_app('production')
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "eureka"
app.config['WTF_CSRF_SECRET_KEY'] = "eureka"
csrf.init_app(app)

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Quote = Quote, Role=Role, Blog=Blog )


if __name__ == '__main__':
    manager.run()