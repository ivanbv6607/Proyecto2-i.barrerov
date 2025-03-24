from flask import Blueprint, render_template, request
from app.models.producto import Productos
from app.models.ingrediente import Ingredientes
from app.models.producto import producto_ingrediente
from app.config.db import db

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/")
def home():
    productos = []
    #for producto in db.query(Productos).all():
    productos = Productos.query.all()
    #productos =Productos.query.get_or_404(1)
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
    calorias = ig1.calorias + ig2.calorias + ig3.calorias
    if producto:
        return render_template('producto.html', producto = producto, ingredientes = ingredientes, calorias = calorias)

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


@home_blueprint.route("/abastecer_ingrediente/<int:id>", methods=["GET"])
def abastecer(id):
    ingrediente = Ingredientes.query.get_or_404(id)
    if ingrediente.tipo == 1:  # Base
        ingrediente.inventario += 10
    else: ingrediente.inventario += 5 # Complemento

    db.session.commit()

    if ingrediente.calorias < 100 or ingrediente.es_vegetariano:
        es_sano = "SI"
    else: es_sano ="NO"

    return render_template('ingrediente.html', ingrediente = ingrediente, es_sano = es_sano)


@home_blueprint.route('/renovar_id') 
def renovar_id(): 
    return render_template('renovar_ing.html')

@home_blueprint.route("/renovar")
def renovar():
    try:
        id = request.args.get("id")

        ingrediente = Ingredientes.query.filter_by(id=id).first()

        if ingrediente:
            ingrediente.inventario = 0
            db.session.commit()

        if ingrediente.calorias < 100 or ingrediente.es_vegetariano:
            es_sano = "SI"
        else: es_sano ="NO"

        return render_template('ingrediente.html', ingrediente = ingrediente, es_sano = es_sano)
    except: 
            #flash("PRODUCTO NO EXISTE")
            return render_template('renovar_ing.html')

