from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)


class db_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable = False)
    category = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return '<db_item %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


@app.route('/itempage')
def itempage():
    return render_template('itempage.html')


@app.route('/admin', methods = ['POST', 'GET'])
def admin():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        price = request.form['price']
        description = request.form['description']

        item = db_item(title = title, category = category, price = price, description = description)

        try: 
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error'
    else:
        return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True)
