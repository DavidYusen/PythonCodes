from flask import Flask
from flask_script import Manager

DBManager = Manager()


@DBManager.command
def init():
    print("DB inited")


@DBManager.command
def migrate():
    print("DB migrated")