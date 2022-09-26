from flask import render_template

from src.models import Product


def index():
    products = Product.query.all()
    return render_template("index.html", products=products)
