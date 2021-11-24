import smtplib

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    # <EMAIL> <PASSWORD>
    # serc.mobileusability@gmail.com
    smtp.login('serc.mobileusability@gmail.com','serc@ssd')

    subject='TESTING'
    body='This mail is simply to test the working of the script.'

    msg=f'Subject: {subject}\n\n{body}'
    # <SENDER EMAIL> <RECEIVER EMAIL> <MESSAGE>
    smtp.sendmail('serc.mobileusability@gmail.com','nvsmaneesh8@gmail.com',msg)
