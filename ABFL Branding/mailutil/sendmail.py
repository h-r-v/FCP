import smtplib

def sendmail( to_mail, SUBJECT, BODY):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('princessbananahammock1999@gmail.com', 'myraa1sep2020')

        subject = SUBJECT
        body = BODY

        msg = f"Subject: {subject}\n\n{body}"
        smtp.sendmail("Princess Consuela Bananahammock", to_mail, msg)

if __name__=="__main__":
    sendmail('toharshrocks1@gmail.com', "Very very concerned", "I am very very concerned.")