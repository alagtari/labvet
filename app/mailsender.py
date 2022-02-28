

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
  
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

  <head>
    <meta charset="utf-8">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
    <title>Bienvenue à LABVET 👋</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700" rel="stylesheet" media="screen">
    <style lang="scss">
      .hover-underline:hover {{
        text-decoration: underline !important;
      }}

      @keyframes spin {{
        to {{
          transform: rotate(360deg);
        }}
      }}

      @keyframes ping {{

        75%,
        100% {{
          transform: scale(2);
          opacity: 0;
        }}
      }}

      @keyframes pulse {{
        50% {{
          opacity: .5;
        }}
      }}

      @keyframes bounce {{

        0%,
        100% {{
          transform: translateY(-25%);
          animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
        }}

        50% {{
          transform: none;
          animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
        }}
      }}

      @media (max-width: 600px) {{
        .sm-leading-32 {{
          line-height: 32px !important;
        }}

        .sm-px-24 {{
          padding-left: 24px !important;
          padding-right: 24px !important;
        }}

        .sm-py-32 {{
          padding-top: 32px !important;
          padding-bottom: 32px !important;
        }}

        .sm-w-full {{
          width: 100% !important;
        }}
      }}
    </style>
  </head>

  <body style="margin: 0; padding: 0; width: 100%; word-break: break-word; -webkit-font-smoothing: antialiased; --bg-opacity: 1; background-color: #eceff1; background-color: rgba(236, 239, 241, var(--bg-opacity));">
   
    <div role="article" aria-roledescription="email" aria-label="Bienvenue à LABVET 👋" lang="en">
      <table style="font-family: Montserrat, -apple-system, 'Segoe UI', sans-serif; width: 100%;" width="100%" cellpadding="0" cellspacing="0" role="presentation">
        <tr>
          <td align="center" style="--bg-opacity: 1; background-color: #eceff1; background-color: rgba(236, 239, 241, var(--bg-opacity)); font-family: Montserrat, -apple-system, 'Segoe UI', sans-serif;" bgcolor="rgba(236, 239, 241, var(--bg-opacity))">
            <table class="sm-w-full" style="font-family: 'Montserrat',Arial,sans-serif; width: 600px;" width="600" cellpadding="0" cellspacing="0" role="presentation">
              <tr>
                <td class="sm-py-32 sm-px-24" style="font-family: Montserrat, -apple-system, 'Segoe UI', sans-serif; padding: 48px; text-align: center;" align="center">
                  
                    <img src="https://i.ibb.co/PrNjTSt/labvet.png" width="155"  style="border: 0; max-width: 100%; line-height: 100%; vertical-align: middle;">
                  
                </td>
              </tr>
              <tr>
                <td align="center" class="sm-px-24" style="font-family: 'Montserrat',Arial,sans-serif;">
                  <table style="font-family: 'Montserrat',Arial,sans-serif; width: 100%;" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                    <tr>
                      <td class="sm-px-24" style="--bg-opacity: 1; background-color: #ffffff; background-color: rgba(255, 255, 255, var(--bg-opacity)); border-radius: 4px; font-family: Montserrat, -apple-system, 'Segoe UI', sans-serif; font-size: 14px; line-height: 24px; padding: 48px; text-align: left; --text-opacity: 1; color: #626262; color: rgba(98, 98, 98, var(--text-opacity));" bgcolor="rgba(255, 255, 255, var(--bg-opacity))" align="left">
                        <p style="font-weight: 600; font-size: 18px; margin-bottom: 0;">Bienvenue</p>
                        <p style="font-weight: 700; font-size: 20px; margin-top: 0; --text-opacity: 1; color: #130275; ">{self.NAME}</p>
                        <p class="sm-leading-32" style="font-weight: 600; font-size: 20px; margin: 0 0 24px; --text-opacity: 1; color: #263238; color: rgba(38, 50, 56, var(--text-opacity));">
                          🏆 Vous avez été ajouté dans notre plateforme.
                        </p>
                      
                          <img src="https://i.ibb.co/PrNjTSt/labvet.png" width="500"  style="border: 0; max-width: 100%; line-height: 100%; vertical-align: middle;">
                       
                       
                        <p style="font-weight: 500; font-size: 16px; margin-bottom: 0;">vous pouvez connecter maintenant a travers ce lien : <a href="http://www.abvet.tn">Labvet</a> 
                          <br>Avec l'acces suivant : </p>
                        <ul style="margin-bottom: 24px;">
                          <li
                            style="color: #130275;">Email :{self.EMAIL_ADDRESS_DEST}</li>
                          <li style="color: #130275;">
                             Mot de Passe :{self.PASSWORD}
                          </li>
                        </ul>
                     
                        <table style="font-family: 'Montserrat',Arial,sans-serif; width: 100%;" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                          <tr>
                            <td style="font-family: 'Montserrat',Arial,sans-serif; padding-top: 32px; padding-bottom: 32px;">
                              <div style="--bg-opacity: 1; background-color: #eceff1; background-color: rgba(236, 239, 241, var(--bg-opacity)); height: 1px; line-height: 1px;">&zwnj;</div>
                            </td>
                          </tr>
                        </table>
                        <p style="margin: 0 0 16px;">             
                            Vous ne savez pas pourquoi vous avez reçu cet e-mail ? Veuillez
                          <a href="mailto:support@example.com" class="hover-underline" style="--text-opacity: 1; color: #7367f0; color: rgba(115, 103, 240, var(--text-opacity)); text-decoration: none;">nous informer</a>.
                        </p>
                        <p style="margin: 0 0 16px;">Merci, <br>Labvet</p>
                      </td>
                    </tr>
                    <tr>
                      <td style="font-family: 'Montserrat',Arial,sans-serif; height: 20px;" height="20"></td>
                    </tr>
                  
                    <tr>
                      <td style="font-family: 'Montserrat',Arial,sans-serif; height: 16px;" height="16"></td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </div>
  </body>

</html>
      """  
      else :
        html = f"""
        
        <html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

  <head>
    <meta charset="utf-8">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
    <title>Bienvenue à LABVET 👋</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700" rel="stylesheet" media="screen">
    <style lang="scss">
      .hover-underline:hover {{
        text-decoration: underline !important;
      }}

      @keyframes spin {{
        to {{
          transform: rotate(360deg);
        }}
      }}

      @keyframes ping {{

        75%,
        100% {{
          transform: scale(2);
          opacity: 0;
        }}
      }}

      @keyframes pulse {{
        50% {{
          opacity: .5;
        }}
      }}

      @keyframes bounce {{

        0%,
        100% {{
          transform: translateY(-25%);
          animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
        }}

        50% {{
          transform: none;
          animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
        }}
      }}

      @media (max-width: 600px) {{
        .sm-leading-32 {{
          line-height: 32px !important;
        }}

        .sm-px-24 {{
          padding-left: 24px !important;
          padding-right: 24px !important;
        }}

        .sm-py-32 {{
          padding-top: 32px !important;
          padding-bottom: 32px !important;
        }}

        .sm-w-full {{
          width: 100% !important;
        }}
      }}
    </style>
  </head>

  <body style="margin: 0; padding: 0; width: 100%; word-break: break-word; -webkit-font-smoothing: antialiased; --bg-opacity: 1; background-color: #eceff1; background-color: rgba(236, 239, 241, var(--bg-opacity));">
   
    <div role="article" aria-roledescription="email" aria-label="Bienvenue à LABVET 👋" lang="en">
      <table style="font-family: Montserrat, -apple-system, 'Segoe UI', sans-serif; width: 100%;" width="100%" cellpadding="0" cellspacing="0" role="presentation">
        <tr>
          <td align="center" style="--bg-opacity: 1; background-color: #eceff1; background-color: rgba(236, 239, 241, var(--bg-opacity)); font-family: Montserrat, -apple-system, 'Segoe UI', sans-serif;" bgcolor="rgba(236, 239, 241, var(--bg-opacity))">
            <table class="sm-w-full" style="font-family: 'Montserrat',Arial,sans-serif; width: 600px;" width="600" cellpadding="0" cellspacing="0" role="presentation">
              <tr>
                <td class="sm-py-32 sm-px-24" style="font-family: Montserrat, -apple-system, 'Segoe UI', sans-serif; padding: 48px; text-align: center;" align="center">
                  
                    <img src="https://i.ibb.co/PrNjTSt/labvet.png" width="155"  style="border: 0; max-width: 100%; line-height: 100%; vertical-align: middle;">
                  
                </td>
              </tr>
              <tr>
                <td align="center" class="sm-px-24" style="font-family: 'Montserrat',Arial,sans-serif;">
                  <table style="font-family: 'Montserrat',Arial,sans-serif; width: 100%;" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                    <tr>
                      <td class="sm-px-24" style="--bg-opacity: 1; background-color: #ffffff; background-color: rgba(255, 255, 255, var(--bg-opacity)); border-radius: 4px; font-family: Montserrat, -apple-system, 'Segoe UI', sans-serif; font-size: 14px; line-height: 24px; padding: 48px; text-align: left; --text-opacity: 1; color: #626262; color: rgba(98, 98, 98, var(--text-opacity));" bgcolor="rgba(255, 255, 255, var(--bg-opacity))" align="left">
                        <p style="font-weight: 600; font-size: 18px; margin-bottom: 0;">Bienvenue</p>
                        <p style="font-weight: 700; font-size: 20px; margin-top: 0; --text-opacity: 1; color: #130275; ">{self.NAME}</p>
                        <p class="sm-leading-32" style="font-weight: 600; font-size: 20px; margin: 0 0 24px; --text-opacity: 1; color: #263238; color: rgba(38, 50, 56, var(--text-opacity));">
                           Vos données de connection ont été modifiés
                        </p>
                      
                          <img src="https://i.ibb.co/PrNjTSt/labvet.png" width="500"  style="border: 0; max-width: 100%; line-height: 100%; vertical-align: middle;">
                       
                       
                        <p style="font-weight: 500; font-size: 16px; margin-bottom: 0;">vous pouvez connecter maintenant
                          <br>Avec l'acces suivant : </p>
                        <ul style="margin-bottom: 24px;">
                          <li
                            style="color: #130275;">Email :{self.EMAIL_ADDRESS_DEST}</li>
                          <li style="color: #130275;">
                             Mot de Passe :{self.PASSWORD}
                          </li>
                        </ul>
                     
                        <table style="font-family: 'Montserrat',Arial,sans-serif; width: 100%;" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                          <tr>
                            <td style="font-family: 'Montserrat',Arial,sans-serif; padding-top: 32px; padding-bottom: 32px;">
                              <div style="--bg-opacity: 1; background-color: #eceff1; background-color: rgba(236, 239, 241, var(--bg-opacity)); height: 1px; line-height: 1px;">&zwnj;</div>
                            </td>
                          </tr>
                        </table>
                        <p style="margin: 0 0 16px;">             
                            Vous ne savez pas pourquoi vous avez reçu cet e-mail ? Veuillez
                          <a href="mailto:support@example.com" class="hover-underline" style="--text-opacity: 1; color: #7367f0; color: rgba(115, 103, 240, var(--text-opacity)); text-decoration: none;">nous informer</a>.
                        </p>
                        <p style="margin: 0 0 16px;">Merci, <br>Labvet</p>
                      </td>
                    </tr>
                    <tr>
                      <td style="font-family: 'Montserrat',Arial,sans-serif; height: 20px;" height="20"></td>
                    </tr>
                  
                    <tr>
                      <td style="font-family: 'Montserrat',Arial,sans-serif; height: 16px;" height="16"></td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </div>
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

  


 






