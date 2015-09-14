import emailer, sys

txt  = 'The message body'

to = ['vic.genty@gmail.com'] # List of emails

e = emailer.Email(to)
e.message(txt)
e.send("SUBJECT LINE")

sys.exit()
