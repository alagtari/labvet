

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText   

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
      msg['Subject'] = "Message Officiel de LABVET: Votre nouveau compte LABVET"
      msg['From'] = self.EMAIL_ADDRESS
      msg['To'] = self.EMAIL_ADDRESS_DEST
      html = """
      <html>
        <body>
          <p><b>Python Mail Test</b><br>
            This is HTML email with attachment.<br>
            Click on <a href="https://fedingo.com">Fedingo Resources</a> 
            for more python articles.
          </p>
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

   
    
    



 






