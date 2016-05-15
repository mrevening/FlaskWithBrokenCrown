from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    plec = db.Column(db.Text, nullable=False)
    wiek = db.Column(db.Text)
    wiekonset = db.Column(db.Text)
    wiekdiagnosis = db.Column(db.Text)
    czastrwania = db.Column(db.Text)
    edss = db.Column(db.Text)
    lastMS = db.Column(db.Text)
    nawrot12 = db.Column(db.Text)
    nawrot24 = db.Column(db.Text)

    def __init__(self, plec, wiek, wiekonset, wiekdiagnosis, czastrwania, edss, lastMS, nawrot12, nawrot24):
        self.plec = plec
        self.wiek = wiek
        self.wiekonset = wiekonset
        self.wiekdiagnosis = wiekdiagnosis
        self.czastrwania = czastrwania
        self.edss = edss
        self.lastMS = lastMS
        self.nawrot12 = nawrot12
        self.nawrot24 = nawrot24
db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)

@app.route("/result")
#scrapy runspider crawl.py -o ..\..\..\FlaskWithBrokenCrown\unit5\crawl_data.json
#scrapy runspider ..\..\CrawlingBrokenCrown\dirbot\spiders\crawl.py -o crawl_data2.json




def show_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions
    plec = []
    wiek = []
    wiekonset = []
    for el in fd_list:
        plec.append(el.plec)
        wiek.append(el.wiek)
        wiekonset.append(el.wiekonset)



    # Prepare data for google charts
    data = [['Plec', plec], ['Wiek', wiek], ['Wiek rozpoczecia choroby', wiekonset]]

    return render_template('result.html', data=data)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    plec = request.form['plec']
    wiek = request.form['wiek']
    wiekonset = request.form['wiekonset']
    wiekdiagnosis = request.form['wiekdiagnosis']
    czastrwania = request.form['czastrwania']
    edss = request.form['edss']
    lastMS = request.form['lastMS']
    nawrot12 = request.form['nawrot12']
    nawrot24 = request.form['nawrot24']


    # Save the data
    fd = Formdata(plec, wiek, wiekonset, wiekdiagnosis, czastrwania, edss, lastMS, nawrot12, nawrot24)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')

#@app.route("/crawler")
#def runcrawler



if __name__ == "__main__":
    app.debug = True
    app.run()