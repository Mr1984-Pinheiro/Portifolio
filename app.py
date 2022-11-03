from socket import if_nameindex
from flask import Flask, render_template, redirect, request, flash
#from flask_mail import Mail, Message
import smtplib
import email.message
from config import mail, senha

app = Flask(__name__)
app.secret_key = 'carlosportifolio'

#mail_settings = {
    #"MAIL_SERVER": 'smtp.gmail.com',
    #"MAIL_PORT": 465,
    #"MAIL_USE_TLS": False,
    #"MAIL_USE_SSL": True, 
    #"MAIL_USERNAME": email,
    #"MAIL_PASSWORD": senha
#}

#app.config.update(mail_settings)
#mail = Mail(app)

class Contato: 
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
        if request.method == 'POST':
            formContato = Contato(
                request.form["nome"],
                request.form["email"],
                request.form["mensagem"],

            ) 

            body= f'''

                {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

                {formContato.mensagem}
                
                '''

            msg = email.message.Message()
            msg['Subject'] = f'{formContato.nome} te enviou uma mensagem no portfólio'
            msg['From'] = mail
            msg['To'] = 'obpccarlos.gmail.com', mail
            password = senha 
            msg.set_payload(body)
            msg.add_header('Content-Type', 'text/html') 
            
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'] + [msg['To']] + msg.as_string().encode('utf-8'))
            
            send()

            flash('Mensagem enviada com sucesso!')
        return redirect('/')


if __name__ == '__main__': 
    app.run(debug=True)