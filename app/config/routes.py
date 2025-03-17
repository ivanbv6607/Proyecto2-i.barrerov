from controllers.home_controller import home_blueprint
#from controllers.home_controller import app_route
#from controllers.todo_controller import todo_blueprint

def register_routes(app):
    app.register_blueprint(home_blueprint)
    #app.register_blueprint(app_route)
    #app.register_blueprint(todo_blueprint)
