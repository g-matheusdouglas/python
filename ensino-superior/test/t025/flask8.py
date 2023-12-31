from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indice.html')

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome = nome_recebido):
    return 'Olá, ', nome

if __name__ == '__main__':
    app.run()