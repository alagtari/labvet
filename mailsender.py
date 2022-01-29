

import smtplib
from email.message import EmailMessage

class SendMail():
    msg = EmailMessage()
    def __init__(self,EMAIL_ADDRESS,EMAIL_PASSWORD,EMAIL_ADDRESS_DEST,PASSWORD,NAME):
        self.NAME = NAME
        self.EMAIL_ADDRESS = EMAIL_ADDRESS
        self.EMAIL_PASSWORD = EMAIL_PASSWORD
        self.EMAIL_ADDRESS_DEST = EMAIL_ADDRESS_DEST
        self.PASSWORD = PASSWORD


    def setMsg(self):
      msg = EmailMessage()
      msg.set_content(f"Bonjour {self.NAME},\n LABVET a le plaisir de vous annoncer la mise en place de la solution LABVET pour vous simplifier et améliorez le travail à l'aide d'outils simples, flexibles et sécurisés. \n Email :{self.EMAIL_ADDRESS_DEST} \n Mot de passe :{self.PASSWORD}")
      msg['Subject'] = "Message Officiel de LABVET: Votre nouveau compte LABVET"
      msg['From'] = self.EMAIL_ADDRESS
      msg['To'] = self.EMAIL_ADDRESS_DEST
      return msg
    def send(self):
        msg = self.setMsg()
        try:
         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
         server.ehlo()
         server.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
         server.send_message(msg)
         server.close()
        except Exception:
         print(Exception)

   
    
    



 






