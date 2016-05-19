import os
from pandas import json
from pprint import pprint
import pandas as pd
from subprocess import call

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
def show_result():
    print ("before")
    os.system("python ../dirbot/spiders/crawlmycrownspider.py 1")
    print ("after")
    # call(['python ../dirbot/spiders/crawlmycrownspider.py shell=True'])
    with open('result.json') as data_file:
        data = json.load(data_file)

        gender = []
        age = []
        ageonset = []
        agediagnosis = []
        durationms = []
        edss = []
        lastms = []
        relapse12 = []
        relapse24 = []

        for x in data:
            v1 = x["type"]
            v2 = x["description"]
            v3 = x["count"]
            v1 = " ".join(str(v) for v in v1)
            v2 = " ".join(str(v) for v in v2)
            v3 = " ".join(str(v) for v in v3)
            if v1 == "Distribution of gender":
                gender.extend([[v2, int(v3)]])
            if v1 == "Age":
                age.extend([[v2,int(v3)]])
            if v1 == "Age at onset":
                ageonset.extend([[v2,int(v3)]])
            if v1 == "Age at diagnosis":
                agediagnosis.extend([[v2, int(v3)]])
            if v1 == "Duration of MS":
                durationms.extend([[v2, int(v3)]])
            if v1 == "EDSS at last visit":
                edss.extend([[v2, int(v3)]])
            if v1 == "Last MSCourse":
                lastms.extend([[v2, int(v3)]])
            if v1 == "Relapse count over last 12 months":
                relapse12.extend([[v2, int(v3)]])
            if v1 == "Relapse count over last 24 months":
                relapse24.extend([[v2, int(v3)]])

        my_dict={'gender': gender, 'age': age, 'ageonset':ageonset, 'agediagnosis': agediagnosis,'durationms':durationms, 'edss': edss,'lastms': lastms,'relapse12': relapse12,'relapse24':relapse24}
        return render_template('result.html', my_dict=my_dict)

@app.route("/this_result")
def show_this_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions
    plec = []
    wiek = []
    wiekonset = []
    for el in fd_list:
        plec.append(el.plec)
        wiek.append(el.wiek)
        wiekonset.append(el.wiekonset)



    #Prepare data for google charts
    data = [['Plec', plec], ['Wiek', wiek], ['Wiek rozpoczecia choroby', wiekonset]]
    # pprint(data)
    return render_template('this_result.html', data=data)

@app.route("/results")
def show_results():
    fd_list = db.session.query(Formdata).all()

    id_name = 'ID'
    plec_name = 'Plec'
    wiek_name = 'Wiek'
    wiekonset_name = 'Wiek rozpoczecia choroby'
    wiekdiagnosis_name = 'Wiek diagnozy'
    czastrwania_name = 'Czas trwania choroby'
    edss_name = 'Ostatni wynik EDSS'
    lastMS_name = 'Ostatni kurs MS'
    nawrot12_name = 'Liczba nawrotow w ostatnich 12 miesiacach'
    nawrot24_name = 'Liczba nawrotow w ostatnich 24 miesiacach'

    tableNames = [id_name, plec_name, wiek_name, wiekonset_name, wiekdiagnosis_name,
             czastrwania_name, edss_name, lastMS_name, nawrot12_name, nawrot24_name]

    ID = []
    plec = []
    wiek = []
    wiekonset = []
    wiekdiagnosis = []
    czastrwania = []
    edss = []
    lastMS = []
    nawrot12 = []
    nawrot24 = []
    for el in fd_list:
        ID.append(str(el.id))
        plec.append(str(el.plec))
        wiek.append(str(el.wiek))
        wiekonset.append(str(el.wiekonset))
        wiekdiagnosis.append(str(el.wiekdiagnosis))
        czastrwania.append(str(el.czastrwania))
        edss.append(str(el.edss))
        lastMS.append(str(el.lastMS))
        nawrot12.append(str(el.nawrot12))
        nawrot24.append(str(el.nawrot24))

    dane = {id_name: ID,
            plec_name: plec,
            wiek_name: wiek,
            wiekonset_name: wiekonset,
            wiekdiagnosis_name: wiekdiagnosis,
            czastrwania_name: czastrwania,
            edss_name: edss,
            lastMS_name: lastMS,
            nawrot12_name: nawrot12,
            nawrot24_name: nawrot24
            }
    data =[]
    j = 1
    for x in tableNames:
        index = str(j)+") "
        for i in range(0,len(dane[x])):
            if j%2 == 1:
                v = [index+x,index+x+" - "+str(dane[x][i]), 1]
                data.append(v)
                w = [index+x+" - "+str(dane[x][i]), "Pacjent "+ str(dane["ID"][i]), 1]
                data.append(w)
            else:
                v = [index + x + " - " + str(dane[x][i]), index + x, 1]
                data.append(v)
                w = ["Pacjent " + str(dane["ID"][i]), index + x + " - " + str(dane[x][i]), 1]
                data.append(w)
        j += 1



    print (dane)


    # dane_noduplicate = {}
    # dane_noduplicate.fromkeys(dane.keys(), [])
    # # for x in tableNames:
    # #     # dane_noduplicate[x].append(None)
    # #     dane_noduplicate[x].apend(list(set(dane[x])))
    #
    # # for x in tableNames:
    # #     dane_noduplicate.append(list(set(dane[x])))
    # print (dane_noduplicate)



    # data = [
    #     ["1) Distribution of gender","1) Female",1],
    #     ["1) Distribution of gender", "1) Male",1],
    #     ["2) Age", "2) < 20", 1],
    #     ["2) Age", "2) 20-29", 1],
    #     ["1) Female", "ID 1" ,1],
    #     ["1) Male","ID 2",1],
    #     ["2) < 20","ID 1",1],
    #     ["2) 20-29", "ID 2", 1],
    #     ["3) 0.0","3) Ostatni wynik EDSS",1],
    #     ["3) 1.0", "3) Ostatni wynik EDSS", 1],
    #     ["ID 1","3) 0.0",1],
    #     ["ID 2","3) 1.0",1],
    #     ["4) RR", "4) Last MSCourse",1],
    #     ["4) SP", "4) Last MSCourse",1],
    #     ["ID 1", "4) RR", 1],
    #     ["ID 2", "4) SP", 1],
    #     ]




    # for x in tableNames:
    #     licznik = 0
    #     for y in range(0,len(dane_noduplicate[licznik])):
    #         data.append[dane_noduplicate[x][y]]
    #         licznik +=1



    return render_template('results.html', data=data)













# [id_name, dane[id_name][1], 1],
# [id_name, dane[id_name][2], 1],
# [wiek_name, dane[wiek_name][1], 1],]
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
    # app.debug = True
    # app.run()

    app.debug = False
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)