import os
import smtplib

from_email = "billykim618@gmail.com"
to_email = "billykim618@gmail.com"
pw = "itifgftmgzgljsnn"
message = "this is a test"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(from_email, pw)
server.sendmail(from_email, to_email, message)