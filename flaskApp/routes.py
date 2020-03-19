from flask import Flask,jsonify,request
from flaskApp import app
from flaskApp.others import scrapyFile
from flaskApp.others.geoLokacije import Lokacija


@app.route('/getStats',methods=['GET'])
def getStats():
    return jsonify({'Statistika':scrapyFile.redoviTabele()})

@app.route('/getNews',methods=['GET'])
def getNews():
    return jsonify({'Vesti':scrapyFile.vestiNaslovi(0,20)})

@app.route('/getDomaceVesti',methods=['GET'])
def getDomaceVesti():
    return jsonify({'Vesti':scrapyFile.domaceVesti()})

@app.route('/getDomaceInfo',methods=['GET'])
def getInfo():
    return jsonify({'Informacije':scrapyFile.stanjeSrbija()})

@app.route('/postCountry',methods=['POST'])
def postCoordinates():
    data=request.get_json()
    return jsonify({'Koordinate':Lokacija.vratiKoordinate(data['drzava'])})

    