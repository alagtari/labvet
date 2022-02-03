

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText   

class SendMail():
    msg = EmailMessage()
    def __init__(self,EMAIL_ADDRESS,EMAIL_PASSWORD,EMAIL_ADDRESS_DEST,PASSWORD,NAME,status):
        self.NAME = NAME
        self.EMAIL_ADDRESS = EMAIL_ADDRESS
        self.EMAIL_PASSWORD = EMAIL_PASSWORD
        self.EMAIL_ADDRESS_DEST = EMAIL_ADDRESS_DEST
        self.PASSWORD = PASSWORD
        self.status = status


    def setMsg(self):
      msg = EmailMessage()
      msg['Subject'] = "Message Officiel de LABVET: Votre nouveau compte"
      msg['From'] = self.EMAIL_ADDRESS
      msg['To'] = self.EMAIL_ADDRESS_DEST
      if self.status == 'new':
            html = f"""
      <html>
        <body>
          <h1>Bienvenue <span style="color:Red;">{self.NAME}</span>,<br>Vous avez été ajouté dans notre plateforme.</h1><br>
           <h3 style="font-weight: normal;"> vous pouvez connecter maintenant a travers ce lien : http://www.abvet.tn <br>
           Avec l'acces suivant : <br>
           email :{self.EMAIL_ADDRESS_DEST} <br>
           password :{self.PASSWORD}
           </h3>
        </body>
      </html>
      """
      else :
        html = f"""
      <html>
        <body>
          <h1>Bienvenue <span style="color:Red;">{self.NAME}</span>,<br> votre données de connection ont été modifiés</h1><br>
           <h3 style="font-weight: normal;"> vous pouvez connecter maintenant avec l'acces suivant : <br>
           email :{self.EMAIL_ADDRESS_DEST} <br>
           password :{self.PASSWORD}
           </h3>
        </body>
      </html>
      """  
          
      part = MIMEText(html, "html")
      msg.set_content(part)
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

  


 






