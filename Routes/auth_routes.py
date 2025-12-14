from flask import Blueprint, session, redirect
from Auth.google_auth import login_google, google_callback

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login/google")
def google_login():
    return login_google()

@auth_bp.route("/auth/google/callback")
def google_callback_route():
    return google_callback()

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
