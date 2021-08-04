from flask import Flask, render_template, request, config, redirect, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'blue'
mail_settings = {
    
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'lucas.soruz.dev@gmail.com',
    "MAIL_PASSWORD": 'soruz.dev'
}

app.config.update(mail_settings)

mail = Mail(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ftscrvix:7YN3Tyulj-1CSrWxfzHoyyB478qSCPs9@kesavan.db.elephantsql.com/ftscrvix'


class Contato:

    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem
#--------------------------------------
 #Cada class representa uma tabela sendo criada dentro do DB

class Projeto(db.Model):
    #Aqui é construido as colunas do DB
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    imagem = db.Column(db.String(7000),nullable=False) #Aqui será usado apenas URLS de imagens, não serão feitos uploads.    
    descricao = db.Column(db.String(600), nullable=False)
    link = db.Column(db.String(1000), nullable=False)


    def __init__(self, nome, imagem, descricao, link):
            self.nome = nome
            self.imagem =imagem                 
            self.descricao = descricao                #Os atributos devem ter ter os mesmos nomes das colunas.
            self.link = link



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def adm():
    return render_template('admin.html')
     # no CRUD esse é o READ



@app.route('/back_index')
def back():
    return redirect('/#projetos')


#CRUD - CREATE
@app.route('/new', methods=['GET','POST'])
def novo_projeto():
    if request.method == 'POST':
        projeto = Projeto(

            request.form['nome'],
            request.form['imagem'],
            request.form['descricao'],
            request.form['link']
        )
        db.session.add(projeto)
        db.session.commit()
        flash('Deu bom, confia!')
        projetos = Projeto.query.all()
        return render_template('admin.html', link = projeto.imagem, projetos = projetos )


@app.route('/send', methods =['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['mensagem']

        )
        
        msg = Message(

            subject= "Contato Portfólio",
            sender = app.config.get('MAIL_USERNAME'),
            recipients = [app.config.get('MAIL_USERNAME'), 'lucasmbrute614@gmail.com'], 
            body = f'''
                O {formContato.nome} com o e-mail {formContato.email}, envigou a seguinte mensagem:
                {formContato.mensagem}
            '''

        
        )
        mail.send(msg)
    return render_template('send.html', formContato = formContato)





if __name__ == "__main__":  
    db.create_all()
    app.run(debug=True)








