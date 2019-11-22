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
@app.route('/products')
def viewProducts():
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

    subcat_id = request.args.get('subcat_id', default=None, type=int)

    if subcat_id is None:
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

        # Read the sub category name
        sql = "SELECT name FROM sub_category WHERE id = %s LIMIT 1;" % subcat_id
        cursor.execute(sql)
        subcat_name = cursor.fetchone()

    return render_template('viewProducts.html',
                           items=items, categories=categories, subcategories=subcategories,
                           subcat_id=subcat_id, subcat_name=subcat_name)


orders = []
# Order products
@app.route('/order/', methods=['GET', 'POST'])
def orderProducts():
    cursor = mysql.get_db().cursor()

    if request.method == 'GET':
        # Read all categories to set as options in the dropdown list
        sql = '''SELECT * FROM category;'''
        cursor.execute(sql)
        categories = cursor.fetchall()

        product_id = request.args.get('product_id', default=None, type=int)
        quantity = request.args.get('quantity', default=None, type=int)

        # if there is any order request
        if product_id is not None:
            # read the information about the selected product
            sql = "SELECT * FROM order_view WHERE product_id = %s;" % product_id
            cursor.execute(sql)
            orderView = cursor.fetchone()

            # save the order info into dictionary
            keys = ["product_id", "product_name", "subcategory_name",
                    "category_name", "price", "quantity"]
            order = dict(zip(keys, [None]*len(keys)))

            order["product_id"] = product_id
            order["product_name"] = orderView[1]
            order["subcategory_name"] = orderView[2]
            order["category_name"] = orderView[3]
            order["price"] = orderView[4]
            order["quantity"] = quantity

            # save all selected products in a list
            if order not in orders:
                orders.append(order)

                # calculate the total price
                total = 0
                for order in orders:
                    total += order["quantity"] * float(order["price"])

                # calculate the total price with taxes
                totaltax = total * 1.05

            return render_template('orderProducts.html', categories=categories, product_id=product_id,
                                   orders=orders, total=total, totaltax=totaltax)
        else:
            orders.clear()
        return render_template('orderProducts.html', categories=categories, product_id=product_id)

    elif request.method == 'POST':

        if request.form['action'] == '+ أضف المنتج':
            # read the user options
            product_id = request.form.get('selected-product')
            quantity = request.form['product-quantity']

            return redirect(url_for('orderProducts', product_id=product_id, quantity=quantity))

        elif request.form['action'] == 'إرسال الطلب':
            if len(orders) is not 0:
                # create an order id
                sql = "INSERT INTO orders (order_date) VALUES (%s)"
                now_date = datetime.datetime.now()
                formatted_date = now_date.strftime('%Y-%m-%d %H:%M:%S')
                val = (formatted_date,)
                cursor.execute(sql, val)
                mysql.get_db().commit()
                # get the order id
                order_id = cursor.lastrowid

                # insert order items into db
                sql = "INSERT INTO order_item (order_id, product_id, quantity) VALUES (%s, %s, %s)"
                val = []
                for order in orders:
                    val.append(
                        (order_id, order["product_id"], order["quantity"]))
                cursor.executemany(sql, val)
                mysql.get_db().commit()

                flash("تم إرسال طلبك بنجاح!")
                orders.clear()
                return redirect(url_for('viewProducts'))
            else:
                return redirect(url_for('orderProducts'))

        elif request.form['action'] == 'إلغاء الطلب':
            orders.clear()
            return redirect(url_for('viewProducts'))


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

    return jsonify({'subcategories': subcategoryArr})


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

    return jsonify({'products': productArr})


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
