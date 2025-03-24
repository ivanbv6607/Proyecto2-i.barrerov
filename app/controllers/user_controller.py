from flask import Blueprint, render_template, request
from app.models.user import User
from app.config.db import db
from flask_login import login_user, login_required, logout_user, current_user
from app.config.auth import login_manager

@login_manager.user_loader
def load_user(id:int):
    return User.query.get(int(id))

login_blueprint = Blueprint("User", __name__, url_prefix="/")

@login_blueprint.route("/login")
def login():
    return render_template("login.html")

@login_blueprint.route('/auth') 
def auth():
    username = request.args.get("username")
    password = request.args.get("password")
    user = User.query.filter_by(username=username, password=password).first()

    print(user)
    if user:
        login_user(user)
        return render_template('dashboard.html')
    
    return render_template('login.html')

@login_blueprint.route('/auth/profile') 
@login_required
def auth_profile():
    if current_user.es_admin == True:
        permisos = "Administrador"
    else: permisos ="usuario"   
    
    if current_user.genero=="Masculino":
        usuario = "Bienvenido"
    else: usuario ="Bienvenida"   

    return f'{usuario}: {current_user.username} eres: {permisos}'

@login_blueprint.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')