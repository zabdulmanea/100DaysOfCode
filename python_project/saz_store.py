from flask import (Flask, render_template, request,
                   redirect, url_for, flash, jsonify)
from flaskext.mysql import MySQL
import datetime
import json

app = Flask(__name__)

# Mysql database config
app.config['MYSQL_DATABASE_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_DATABASE_USER'] = 'sql12312605'
app.config['MYSQL_DATABASE_PASSWORD'] = 'wjtXsLSNCm'
app.config['MYSQL_DATABASE_DB'] = 'sql12312605'

mysql = MySQL(app)

# Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# About us
@app.route('/about')
def aboutUs():
    return render_template('about.html')

# Display products
@app.route('/products/<int:subcat_id>/')
def viewProducts(subcat_id):
    subcat_name = ''
    cursor = mysql.get_db().cursor()

    # Read all categories
    sql = '''SELECT * FROM category;'''
    cursor.execute(sql)
    categories = cursor.fetchall()

    # Read all subcategories
    sql = '''SELECT * FROM sub_category;'''
    cursor.execute(sql)
    subcategories = cursor.fetchall()

    if subcat_id == 0:
        # Read all products
        sql = '''SELECT * FROM product_item;'''
        cursor.execute(sql)
        items = cursor.fetchall()
        # items = json.dumps(result, indent=4).encode('utf-8').decode('unicode-escape')
    else:
        # Read products under specific subcategory
        sql = "SELECT * FROM product_item WHERE sub_cat_id = %s;" % subcat_id
        cursor.execute(sql)
        items = cursor.fetchall()

        sql = "SELECT name FROM sub_category WHERE id = %s LIMIT 1;" % subcat_id
        cursor.execute(sql)
        subcat_name = cursor.fetchone()

    return render_template('viewProducts.html', 
    items=items, categories=categories, subcategories=subcategories, 
    subcat_id=subcat_id, subcat_name=subcat_name)

# Order products
@app.route('/order/<int:order_id>/', methods=['GET', 'POST'])
def orderProducts(order_id):
    cursor = mysql.get_db().cursor()

    if request.method == 'GET':
        # Read all categories to set as options in the dropdown list
        sql = '''SELECT * FROM category;'''
        cursor.execute(sql)
        categories = cursor.fetchall()

        # if there is an order 
        if order_id != 0:
            # view all the information about the ordered product
            sql = "SELECT category.name, sub_category.name, product_item.name, product_item.price, order_item.quantity \
                FROM category, sub_category, product_item, order_item \
                WHERE product_item.sub_cat_id = sub_category.id AND sub_category.category_id = category.id \
                AND order_item.product_id = product_item.id \
                AND order_item.order_id = %s;" % (order_id)
            cursor.execute(sql)
            orderView = cursor.fetchall()

            # calculate the total price 
            total = 0
            for order in orderView:
                total += int(order[3]) * int(order[4])

            # calculate the total price with taxes
            totaltax = total * 1.05

            return render_template('orderProducts.html', order_id=order_id, categories=categories, 
                                   orders=orderView, total=total, totaltax=totaltax)

        return render_template('orderProducts.html', order_id=order_id, categories=categories)

    elif request.method == 'POST':

        if request.form['action'] == '+ أضف المنتج':
            # read the user options
            product_id = request.form.get('selected-product')
            quantity = request.form['product-quantity']

            # create an order id if there is no one
            if order_id == 0:
                # create order id
                sql = "INSERT INTO orders (order_date) VALUES (%s)"
                now_date = datetime.datetime.now()
                formatted_date = now_date.strftime('%Y-%m-%d %H:%M:%S')
                val = (formatted_date,)
                cursor.execute(sql, val)
                mysql.get_db().commit()
                order_id = cursor.lastrowid

            # create order item
            sql = "INSERT INTO order_item (order_id, product_id, quantity) VALUES (%s, %s, %s)"
            val = (order_id, product_id, quantity)
            cursor.execute(sql, val)
            mysql.get_db().commit()

            return redirect(url_for('orderProducts', order_id=order_id))

        elif request.form['action'] == 'إرسال الطلب':
            if order_id != 0:
                flash("تم إرسال طلبك بنجاح!")
                return redirect(url_for('viewProducts', subcat_id=0))
            else:
                return redirect(url_for('orderProducts', order_id=0))

        elif request.form['action'] == 'إلغاء الطلب':
            sql = "DELETE FROM orders WHERE id = %s" % order_id
            cursor.execute(sql)
            mysql.get_db().commit()
            flash("تم إلغاء طلبك !")
            return redirect(url_for('viewProducts', subcat_id=0))

# ------------------- JSON Endpoints -------------------------
@app.route('/categories/JSON')
def categoriesJSON():
    cursor = mysql.get_db().cursor()
    # Read all categories
    sql = '''SELECT * FROM category;'''
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]  # entities
    categories = cursor.fetchall()
    json_data = []
    for cat in categories:
        json_data.append(dict(zip(row_headers, cat)))
    return json.dumps(json_data, indent=4).encode('utf-8').decode('unicode-escape')


@app.route('/subcategories/<int:category_id>/JSON')
def subcategoriesJSON(category_id):
    cursor = mysql.get_db().cursor()
    # Read subcategories of specific category
    sql = '''SELECT * FROM sub_category WHERE category_id = %s;''' % category_id
    cursor.execute(sql)    
    subcategories = cursor.fetchall()

    subcategoryArr = []

    for subcategory in subcategories:
        subcategoryObj = {}
        subcategoryObj['id'] = subcategory[0]
        subcategoryObj['name'] = subcategory[2]
        subcategoryArr.append(subcategoryObj)

    return jsonify({'subcategories' : subcategoryArr})



@app.route('/products/<int:sub_cat_id>/JSON')
def productsJSON(sub_cat_id):
    cursor = mysql.get_db().cursor()
    # Read products related to specific subcategory
    sql = '''SELECT * FROM product_item WHERE sub_cat_id = %s;''' % sub_cat_id
    cursor.execute(sql)
    products = cursor.fetchall()


    productArr = []

    for product in products:
        productArrObj = {}
        productArrObj['id'] = product[0]
        productArrObj['name'] = product[2]
        productArrObj['price'] = product[3]
        productArr.append(productArrObj)

    return jsonify({'products' : productArr})


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
