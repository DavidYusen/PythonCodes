from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@manager.command
def hello():
    print("hello")


@manager.command
def helloworld():
    print("hello world")


if __name__ == "__main__":
    manager.run()
