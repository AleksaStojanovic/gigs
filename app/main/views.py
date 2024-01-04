from flask import Blueprint, flash, redirect, render_template, url_for, session
from flask_login import AUTH_HEADER_NAME, login_user

from app.models import User, Role, Gig
from app.auth.views import current_user

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
def home():
    musicians = gigs = None
    if current_user.is_role(Role.MUSICIAN):
        gigs = Gig.query.all()
    if current_user.is_role(Role.EMPLOYER):
        musicians = User.query.filter_by(role_id=Role.MUSICIAN).all()
    return render_template("home.html", gigs=gigs, musicians=musicians)
