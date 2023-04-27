from flask import Flask

app = Flask(__name__)

@app.route('/') # @ decorator
def homepage():
    return 'Meu primeiro site no ar'


@app.route('/perfil')
def perfil():
   return 'Perfil do usuario'




















if __name__ == '__main__': # so executa qdo o main estiver sendo executado, se for algum import nao execulta
  app.run(debug=True)# debug == True, qualquer alteração no cod ja reflete no site