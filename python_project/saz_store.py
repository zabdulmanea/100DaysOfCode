from flask import Flask, render_template

app = Flask(__name__)


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
    return render_template('viewProducts.html')


if __name__ == '__main__':
    app.run(debug=True)
