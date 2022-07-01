from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("home.html")

@app.route('/listado')
def listado():
  paises = []
  conn = sqlite3.connect('co_emissions.db')
  q = f"""SELECT Country FROM emissions WHERE Series = "pcap" ORDER BY Value DESC LIMIT 10 """
  a = conn.execute(q)

  for fila in a:
    paises.append(fila)
  
  return render_template("listado.html", listado = paises)
  
@app.route('/listado/<pais>')
def paises(pais):
  if pais == "top":
    paises = []
    conn = sqlite3.connect('co_emissions.db')
    q = f"""SELECT Country FROM emissions WHERE Series = "total" ORDER BY Value DESC LIMIT 10 """
    a = conn.execute(q)

    for fila in a:
      paises.append(fila)
    return render_template("top.html", listado = paises)
  else:
    conn = sqlite3.connect('co_emissions.db')
    ql = f"""SELECT Value FROM emissions WHERE Country = '{pais}'       and Series = "total" """
    qlt = f"""SELECT Value FROM emissions WHERE Country = '{pais}'       AND Series = "pcap" """
    b = conn.execute(ql)
    c = conn.execute(qlt)
    return render_template("paises.html", caracteristicasb = b, caracteristicasc = c, paish = pais)
    conn.close()

@app.route('/ayuda')
def ayuda():
    return render_template("ayuda.html")
  
app.run(host='0.0.0.0', port=81)
