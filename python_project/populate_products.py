from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)


app.config['MYSQL_DATABASE_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_DATABASE_USER'] = 'sql12312605'
app.config['MYSQL_DATABASE_PASSWORD'] = 'wjtXsLSNCm'
app.config['MYSQL_DATABASE_DB'] = 'sql12312605'

mysql = MySQL(app)


# READ/SELECT
@app.route('/')
@app.route('/read')
def read():
    cursor = mysql.get_db().cursor()
    sql = '''SELECT * FROM category;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    return str(result)

# CREATE/INSERT
@app.route('/create')
def create():
    cursor = mysql.get_db().cursor()
    sql = "INSERT INTO category (name) VALUES (%s)"
    val = ("تجربة",)
    cursor.execute(sql, val)
    mysql.get_db().commit()

    return "New records INSERTED!!"

# UPDATE
@app.route('/update')
def update():
    cursor = mysql.get_db().cursor()
    sql = "UPDATE category SET name = 'تجربة بعد التعديل' WHERE name = 'تجربة'"
    cursor.execute(sql)
    mysql.get_db().commit()
    return "Records UPDATED!!"

# DELETE
@app.route('/delete')
def delete():
    cursor = mysql.get_db().cursor()

    sql = "DELETE FROM category WHERE name = 'تجربة بعد التعديل' OR name = 'تجربة'"
    cursor.execute(sql)
    mysql.get_db().commit()

    return "Records DELETED!!"

# INSERT product items
@app.route('/insert_all_items')
def insert_items():
    cursor = mysql.get_db().cursor()
    sql = "INSERT INTO product_item (sub_cat_id, name, img_src, price) VALUES (%s, %s, %s, %s)"
    val = [
        (9, 'شرارة نجوم الليل', '/static/images/party_light.jpg', 1),
        (9, 'شرارة نجوم الليل', '/static/images/heart_light.jpg', 4),
        (4, 'الشجرة المضيئة', '/static/images/light_tree.jpg', 110),
        (6, 'البالونة الشفافة المضيئة', '/static/images/trans_baloon.jpg', 25),
        (1, 'الستارة المضيئة', '/static/images/light_curtain.jpg', 120),
        (3, 'الشموع الثلاثية المضيئة', '/static/images/3_colored_candle.jpg', 35),
        (2, 'سلسة إضاءة البيبي لايت', '/static/images/baby_light.jpg', 35),
        (2, 'سلك الليزر المضيء', '/static/images/led_light.jpg', 80),
        (3,'الشموع المضيئة الصغيرة','/static/images/small_candles.jpg',35),
        (6,'البالونات المضيئة في الظلام','/static/images/light_baloons.jpg',10),
        (2,'سلسة إضاءة كرة القطن ','/static/images/cotton_ball.jpg',35),
        (1,'ستارة النجوم','/static/images/star_light.jpg',100),
        (5,'صندوق الأحرف المضيء','/static/images/light_board.jpg',170),
        (1,'ستارة الشلال المضيء','/static/images/waterfall_curtain.jpg',110),
        (10,'المايكروفون المتنقل المضيء','/static/images/light_mic.jpg',80),
        (2,'سلسة إضاءة الفوانيس','/static/images/fanoos_light1.jpg',35),
        (1,'ستارة الشبكة المضيئة','/static/images/web_curtain.jpg',110),
        (10,'المايكروفون المتنقل','/static/images/mic.jpg',80),
        (2,'سلسة إضاءة الفوانيس والنجوم','/static/images/star_moon_light.jpg',35),
        (2,'سلسة إضاءة عقد الفانوس','/static/images/fanoos_light.jpg',35),
        (4,'شجرة الفوانيس المضيئة','/static/images/fanoos_tree.jpg',110),
        (7,'مكعبات الثلج المضيئة','/static/images/ice_cubes.jpg',35),
        (8,'الحذاء الرياضي المضيء','/static/images/light_shoes.jpg',50),
        (10,'كريستالة الليزر','/static/images/crystal_light.jpg',60),
        (7,'مكعبات الثلج الفسفورية','/static/images/phosphoric_ice_cubes.jpg',30),
        (10,'السماعات الهرمية المضيئة','/static/images/headphones1.jpg',90),
        (7,'الكوب المضيء','/static/images/light_cups.jpg',15),
        (10,'سماعة النافورة الراقصة','/static/images/two_headphones.jpg',100),
        (11,'السبورة المضيئة','/static/images/light_blackboard.jpg',175),
        (8,'الأساور الفسفورية','/static/images/phosphoric_bracelet.jpg',1)
    ]
    cursor.executemany(sql, val)
    mysql.get_db().commit()

    return "New records inserted!!"


if __name__ == '__main__':
    app.run(debug=True)
