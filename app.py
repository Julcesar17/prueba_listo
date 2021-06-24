from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/mydb.db'
db = SQLAlchemy(app)

## Modelo de la tabla Productos
class Products(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  name_supplier = db.Column(db.String(50))
  volume = db.Column(db.Float)
  metrics = db.Column(db.String(10))
  price = db.Column(db.Float)
  date = db.Column(db.String(50))

## Función para dar formato de moneda através de un filtro
@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.2f}".format(value)

## Ruta home muestra el listado de productos
@app.route('/')
def index():
  sql = text('select name,sum(volume) as total_volume, metrics, avg(price) as price_prom, sum(price) as total_price from products group by name order by total_volume desc')
  products = db.engine.execute(sql)
  return render_template('index.html', products = products)

## Ruta productos/nombre_producto muestra el detalle de un producto
@app.route('/products/<name>')
def product(name):
  product = Products.query.filter_by(name=name).order_by('date').all()
  return render_template('product.html', product = product, name=name)

if __name__ == '__main__':
  app.run(debug=True)