#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from config import mail, senha


import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <h1>Parágrafo1</h1>
    <p>Parágrafo2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = mail
    msg['To'] = mail
    password = senha 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()

