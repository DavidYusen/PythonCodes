from flask_script import Shell, Manager


def _make_context():
    return dict(app=app, db=db, models=models)


manager = Manager()
manager.add_command("shell", Shell(make_context=_make_context))
