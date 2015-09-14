import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText


class Email:

    def __init__(self,to):
        # Bill's wiki stays..
        # https://twiki.nevis.columbia.edu/twiki/bin/view/Main/ConfigureMail
        #
        # If your e-mail address ends in nevis.columbia.edu you must use the
        # Nevis mail server mail.nevis.columbia.edu to send mail.
        # Do not use the Nevis mail server if you want your e-mail address
        # to end in anything except nevis.columbia.edu.
        
        self.sender  = "sender@email.com"
        self.to      = to

        self.msg = MIMEMultipart()
        

    def message(self,mes):
        txt = MIMEText(mes)
        self.msg.attach(txt)


    def send(self,subject):

        self.msg['Subject'] = subject
        self.msg['From']    = self.sender
        self.msg['To']      = ",".join(self.to)

        # Not SSL
        s = smtplib.SMTP("mail.domain.com")
        s.starttls()

        # SSL (different port)
        # s = smtplib.SMTP_SSL("mail.domain.com")
                             
        s.login('username','password')
        s.sendmail(self.sender,self.to, self.msg.as_string())

        s.quit()
