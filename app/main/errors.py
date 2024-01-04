from flask import render_template
from app.main.views import main


def page_not_found(e):
    return render_template("errors/404.html")
