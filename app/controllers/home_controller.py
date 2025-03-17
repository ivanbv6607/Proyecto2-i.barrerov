from flask import Blueprint, render_template, request
from models.producto import Productos
from models.ingrediente import Ingredientes
from models.ingrediente_producto import producto_ingrediente
from config.db import db

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    productos = []
    productos = Productos.query.all()
    return render_template("index.html", productos = productos)


@home_blueprint.route("/productos")
def producto_todos():
    productos = []
    productos = Productos.query.all()
    return render_template("productos.html", productos = productos)

@home_blueprint.route("/producto/<int:id>", methods=["GET"])
def producto(id):
    producto = Productos.query.get_or_404(id)
    ig1 = Ingredientes.query.get_or_404(producto.ing1)
    ig2 = Ingredientes.query.get_or_404(producto.ing2)
    ig3 = Ingredientes.query.get_or_404(producto.ing3)
    ingredientes = []
    ingredientes.append(ig1)
    ingredientes.append(ig2)
    ingredientes.append(ig3)
    return render_template('producto.html', producto = producto, ingredientes = ingredientes)


@home_blueprint.route("/producto_ingredientre/<int:id>", methods=["GET"])
def pedir_producto(id):
    producto = Productos.query.get_or_404(id)
    ingredientes = []
    ingredientes.append(Ingredientes.query.get_or_404(producto.ing1))
    ingredientes.append(Ingredientes.query.get_or_404(producto.ing2))
    ingredientes.append(Ingredientes.query.get_or_404(producto.ing3))
    return render_template('producto.html', producto = producto, ingredientes = ingredientes)

@home_blueprint.route("/ingredientes")
def ingrediente_todos():
    ingredientes = []
    ingredientes = Ingredientes.query.all()
    return render_template("ingredientes.html", ingredientes = ingredientes)

@home_blueprint.route('/ingrediente') 
def ingrediente():
    return render_template('ingrediente.html')


@home_blueprint.route("/vender_producto/<int:id>", methods=["GET"])
def vender(id):
    producto = Productos.query.get_or_404(id)
    ingredientes = []
    ingredientes.append(Ingredientes.query.get_or_404(producto.ing1))
    ingredientes.append(Ingredientes.query.get_or_404(producto.ing2))
    ingredientes.append(Ingredientes.query.get_or_404(producto.ing3))
    nombre_ingrediente = ""
    for ingrediente in ingredientes:
        if ingrediente.inventario<1: # No hay existencia de ingrediente
            nombre_ingrediente = ingrediente.nombre
            break
        
    if len(nombre_ingrediente)>0:
        print(nombre_ingrediente)
        ValueError (f"El ingrediente {nombre_ingrediente} no esta disponible para vender") 
    else:   
            for ingrediente in ingredientes:
                ing = Ingredientes.query.get_or_404(ingrediente.id)
                existencia = ing.inventario - 1
                ing.inventario = existencia
                db.session.commit()
    if len(nombre_ingrediente)>0:
        return f'No hay existencia de ingrediente {nombre_ingrediente}'
    else:     return 'Vendido!'

     