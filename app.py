from flask import Flask, jsonify, request, render_template
from models import DatabaseWrapper

app = Flask(__name__)

db = DatabaseWrapper(
    host="mysql-27ce9d22-iisgalvanimi-ea47.i.aivencloud.com",
    user="avnadmin",
    port = 27034,
    password="AVNS_A52MbIJeDKtjHgT32C7",
    database="defaultdb"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/studenti", methods=["GET"])
def elenco_studenti():
    risultati = db.get_studenti()
    return jsonify(risultati)


@app.route("/studenti", methods=["POST"])
def aggiungi():
    nome = request.form["nome"]
    db.aggiungi_studente(nome)
    return jsonify({"messaggio": f"{nome} aggiunto"})

if __name__ == "__main__":
    app.run(debug=True)