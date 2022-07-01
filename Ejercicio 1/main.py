from flask import Flask, render_template
import random


app = Flask(__name__)

dado = random.randint(1,6)

año = random.randint(1970, 2100)
mes = random.randint(1, 12)
dia = random.randint(1,31)
fecha = str(dia) + "/" + str(mes) + "/" + str(año)

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]

@app.route('/')
def start():
  return "hola"

@app.route('/dado/')
def index():
  return  render_template('resu.html',listilla = dado)
 
  
@app.route('/fecha')
def darFecha():
  return  str(fecha)

@app.route('/color')
def darColor():
  return render_template('color.html',colour = str(color))


@app.route('/dado/<n>')
def buscar(n):
  lista = []
  if (int(n) > 0 and int(n) < 10):
    while len(lista) < int(n):
      x = random.randint(1,6)
      lista.append(x)
    return render_template('resu.html',listilla = lista)
  else:
    return render_template('error.html')
      
@app.route('/fecha/<y>/')
def año(y):
  mes = random.randint(1,12)
  return render_template('fecha.html', day =  dia, month = mes, year = y)  


@app.route('/fecha/<y>/<m>')
def mes(y , m):
  if (int(m) < 13 and int(m) > 0):
    return render_template('fecha.html', day =  dia, month = m, year = y)
  else: 
    return render_template('error.html')



app.run(host='0.0.0.0', port=81)

#return render_template('resu.html',resultado= int(uno) + int(dos))




