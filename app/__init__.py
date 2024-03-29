import os
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from celery import Celery


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
mail = Mail()
celery = Celery()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or "prc9FWjeLYh_KsPGm0vJcg",
        SQLALCHEMY_DATABASE_URI="sqlite:///"
        + os.path.join(basedir, "globomantics.sqlite"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=True,
        MAIL_SERVER="127.0.0.1",
        MAIL_PORT=1025,
        CELERY_BROKER_URL="redis://127.0.0.1:6379/0",
        SEND_MAILS_WITH_CELERY=True,
    )

    db.init_app(app)
    mail.init_app(app)
    init_celery(app)
    Migrate(app, db)

    from app.auth.views import auth
    from app.main.views import main
    from app.account.views import account
    from app.gig.views import gig
    from app.admin.views import admin

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(account, url_prefix="/user")
    app.register_blueprint(gig, url_prefix="/gig")
    app.register_blueprint(admin, url_prefix="/admin")

    from app.main.errors import page_not_found

    app.register_error_handler(404, page_not_found)

    return app


def init_celery(app):
    celery.conf.broker_url = app.config["CELERY_BROKER_URL"]

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
