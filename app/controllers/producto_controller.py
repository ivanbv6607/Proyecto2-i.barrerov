from flask import Blueprint, render_template, request, flash
from app.models.producto import Productos
from app.config.db import db
from app.models.ingrediente import Ingredientes
from flask_login import login_user, login_required, logout_user, current_user


producto_blueprint = Blueprint("Producto", __name__, url_prefix="/producto")

@producto_blueprint.route('/productoid') 
def producto_busqueda_id():
        return render_template('prd_id.html')

@producto_blueprint.route('/id') 
def producto_id():
    try:
        id = request.args.get("id")
 
        producto = Productos.query.filter_by(id=id).first()

        ig1 = Ingredientes.query.get_or_404(producto.ing1)
        ig2 = Ingredientes.query.get_or_404(producto.ing2)
        ig3 = Ingredientes.query.get_or_404(producto.ing3)
        ingredientes = []
        ingredientes.append(ig1)
        ingredientes.append(ig2)
        ingredientes.append(ig3)
        calorias = ig1.calorias + ig2.calorias + ig3.calorias
        rentabilidad = producto.precio - ig1.costo - ig2.costo - ig3.costo
        costo =  ig1.costo + ig2.costo + ig3.costo
        if producto:
            return render_template('producto.html', producto = producto, ingredientes = ingredientes, calorias = calorias,
                                rentabilidad = rentabilidad, costo = costo)
    except: 
        flash("PRODUCTO NO EXISTE")
        return render_template('ing_id.html')
    return render_template('ing_id.html')

@producto_blueprint.route('/nombre') 
def producto_busqueda_nombre():
        return render_template('nombre_producto.html')

@producto_blueprint.route('/bus_nombre_producto') 
def producto_nombre():
    try:
        nombre = request.args.get("nombre")

        producto = Productos.query.filter_by(nombre=nombre).first()

        ig1 = Ingredientes.query.get_or_404(producto.ing1)
        ig2 = Ingredientes.query.get_or_404(producto.ing2)
        ig3 = Ingredientes.query.get_or_404(producto.ing3)
        ingredientes = []
        ingredientes.append(ig1)
        ingredientes.append(ig2)
        ingredientes.append(ig3)
        calorias = ig1.calorias + ig2.calorias + ig3.calorias
        rentabilidad = producto.precio - ig1.costo - ig2.costo - ig3.costo
        costo =  ig1.costo + ig2.costo + ig3.costo
        if producto:
            return render_template('producto.html', producto = producto, ingredientes = ingredientes, calorias = calorias,
                               rentabilidad = rentabilidad, costo = costo)
    except: 
        flash("PRODUCTO NO EXISTE")
        return render_template('nombre_producto.html')   
    return render_template('nombre_producto.html')

@producto_blueprint.route('/venderid') 
def producto_vender_id():
        return render_template('vender.html')

@producto_blueprint.route('/venderid_producto')
def venderid_producto():

    id = request.args.get("id")
    producto = Productos.query.filter_by(id=id).first()
    #producto = Productos.query.get_or_404(id)
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