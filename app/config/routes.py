from app.controllers.home_controller import home_blueprint
from app.controllers.user_controller import login_blueprint
from app.controllers.producto_controller import producto_blueprint
from app.controllers.ingrediente_controlller import ingrediente_blueprint

def register_routes(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(producto_blueprint)
    app.register_blueprint(ingrediente_blueprint)

