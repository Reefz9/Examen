from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/calculotarros', methods=['GET', 'POST'])
def calculoTarros():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = float(request.form['edad'])
        tarro = float(request.form['tarro'])
        total = 9000 * tarro
        desc = 0

        if 18 <= edad <= 30:
            desc = total * 0.15
            total_desc = total - desc
        elif edad > 30:
            desc = total * 0.25
            total_desc = total - desc
        else:
            desc = total
            total_desc = total - desc

        return render_template('calculotarros.html', nombre=nombre, total=total,desc=desc,total_desc=total_desc)
    return render_template('calculotarros.html')


@app.route('/iniciosesion', methods=['GET', 'POST'])
def inicioSesion():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        contra = str(request.form['contra'])

        if nombre == "juan" and contra == "admin":
            mensaje = "Bienvenido administrador juan"
        elif nombre == "pepe" and contra == "user":
            mensaje ="Bienvenido usuario pepe"
        else:
            mensaje ="Usuario o contraseña incorrectos"

        return render_template('iniciosesion.html', mensaje=mensaje)
    return render_template('iniciosesion.html')


if __name__ == '__main__':
    app.run(debug=True)