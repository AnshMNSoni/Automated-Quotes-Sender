# Sending quotes to friends:

import smtplib as st
import datetime as dt, random


# Day of Week:
now = dt.datetime.now()
day_of_week = now.weekday()


if (day_of_week == 0):
    # Choosing Random quote from the quote.txt:
    with open('quotes.txt', 'r', encoding='utf-8') as data_file:
        data = data_file.readlines()
        quote = random.choice(data)
    
    # Sending Mail to Ourself:
    my_email = 'anshsoni702@gmail.com'
    password = 'hnae syae ioqr rney'
    
    with st.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        message = f'Subject:Motivational Quote\n\n{quote}'
        encoded_string = message.encode('utf-8')
        connection.sendmail(from_addr=my_email, to_addrs='anshsoni702@gmail.com', msg=encoded_string)