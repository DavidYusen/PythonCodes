import os


class Config(object):

    # The secret key is used internally by Flask to encrypt session data stored
    # in cookies. Make this unique for your app.
    SECRET_KEY = 'shhh,secret!'

    ADMIN_PASSWORD = 'limeiyun'

    DEBUG = False

    # This is used by micawber, which will attempt to generate rich media
    # embedded objects with max width=800.
    SITE_WIDTH = 800

    # The playhouse.flask_utils.FlaskDB object accepts database URL configuration.
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
