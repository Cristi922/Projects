import smtplib
import datetime as dt
import pandas as pd
import random

# # cont si parola email
# # my_email = 'test@gmail.com'
# # password = 'test'
#
my_email = 'test@yahoo.ca'
password = 'test'
#
# # connection.login(user=my_email, password="mwvwmtxkttbttfyi")
#
#
# with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password="mwvwmtxkttbttfyi")
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="test@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )




















# ========== AUTOMATED MOTIVATIONAL QUOTES SENDER ==========

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 2:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)
#     with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password="mwvwmtxkttbttfyi")
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="test@gmail.com",
#             msg=f"Subject:Monday motivation\n\n{quote}"
#         )



















