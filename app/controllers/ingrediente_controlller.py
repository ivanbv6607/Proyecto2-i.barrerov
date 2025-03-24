from flask import Blueprint, render_template, request, flash
from app.config.db import db
from app.models.ingrediente import Ingredientes

ingrediente_blueprint = Blueprint("Ingrediente", __name__, url_prefix="/ingrediente")

@ingrediente_blueprint.route('/id') 
def ingrediente_busqueda_id(): 
        return render_template('ing_id.html')


@ingrediente_blueprint.route('/bus_ingredienteid') 
def ingrediente_id():
    try:
        id = request.args.get("id")

        ingrediente = Ingredientes.query.filter_by(id=id).first()

        if ingrediente:
            if ingrediente.calorias < 100 or ingrediente.es_vegetariano:
                es_sano = "SI"
            else: es_sano ="NO"
            return render_template('ingrediente.html', ingrediente = ingrediente, es_sano = es_sano)
    except: 
        flash("PRODUCTO NO EXISTE")
        return render_template('ing_id.html')


@ingrediente_blueprint.route('/nombre') 
def ingrediente_busqueda_nom():
        return render_template('ing_nom.html')


@ingrediente_blueprint.route('/bus_ingredientenom') 
def ingrediente_nom():
    try:
        nombre = request.args.get("nombre")
 
        ingrediente = Ingredientes.query.filter_by(nombre=nombre).first()

        if ingrediente:
            if ingrediente.calorias < 100 or ingrediente.es_vegetariano:
                es_sano = "SI"
            else: es_sano ="NO"
            return render_template('ingrediente.html', ingrediente = ingrediente, es_sano = es_sano)
    except: 
        flash("PRODUCTO NO EXISTE")
        return render_template('ing_nom.html')


