from flask_script import Manager
from flask import Flask
from db_script import DBManager

app = Flask(__name__)

manager = Manager(app)


@manager.command
def test():
    print("hello flask script")


manager.add_command('db', DBManager)

if __name__ == '__main__':
    manager.run()