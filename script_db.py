import sqlite3, re
conn = sqlite3.connect('database/mydb.db')
c = conn.cursor()

## Patrones de regex para encontrar coincidencias
pattern_suppliers = '\n\n'
pattern_name_suppliers = '([A-Z]{3})\n'
pattern_data = '\d.+\.\d{2}'

## Función para eliminar tabla productos
def delete_table():
    c.execute("""DROP TABLE IF EXISTS products""")

## Función para crear tabla productos
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS products (
        id INTEGER primary key,
        name TEXT,
        name_supplier TEXT,
        volume REAL,
        metrics TEXT,
        price REAL,
        date TEXT
        )"""
    )

## Función para sanitizar el nombre de los productos
def sanitize_name(name):
    name = name.replace('á','a')
    name = name.replace('é','e')
    name = name.replace('í','i')
    name = name.replace('ó','o')
    name = name.replace('ú','u')
    name = name.replace('ü','u')
    name = name.replace('ñ','ñ')
    name = name.replace('_','')
    name = name.replace('-','')
    name = name.replace('$','')
    name = name.replace(' ','')
    name = name.replace('*','')
    name = name.upper()
    return name

## Función para dar formato de fecha ISO al campo fecha
def format_date(date):
    dates = date.split('-')
    day = dates[0]
    month = '01'
    year = dates[2]

    if dates[1].lower() == 'feb':
        month = '02'
    elif dates[1].lower() == 'mar':
        month = '03'
    elif dates[1].lower() == 'abr':
        month = '04'
    elif dates[1].lower() == 'may':
        month = '05'
    elif dates[1].lower() == 'jun':
        month = '06'
    elif dates[1].lower() == 'jul':
        month = '07'
    elif dates[1].lower() == 'ago':
        month = '08'
    elif dates[1].lower() == 'sep':
        month = '09'
    elif dates[1].lower() == 'oct':
        month = '10'
    elif dates[1].lower() == 'nov':
        month = '11'
    elif dates[1].lower() == 'dic':
        month = '12'

    date_ISO = year +'-'+ month + '-'+ day
    return date_ISO

## Función para insertar datos a la tabla productos
def insert_data(filename):

    file = open(filename, "r")
    f = file.read()

    suppliers = re.split(pattern_suppliers, f)

    for supplier in suppliers:
        name_supplier = re.findall(pattern_name_suppliers,supplier)
        data = re.findall(pattern_data, supplier)

        for item in data:
            values = item.strip().split('|')
            name = sanitize_name(values[3].strip())
            date = format_date(values[0])
            c.execute(
                'insert into products (name,name_supplier,volume,metrics,price,date) values(?,?,?,?,?,?)',
                (name,name_supplier[0],values[1],values[2],values[4],date)
            )
            conn.commit()

delete_table()
create_table()
insert_data('mydb.txt')