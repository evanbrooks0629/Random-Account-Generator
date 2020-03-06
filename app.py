import requests
from bs4 import BeautifulSoup
import random
import csv
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


names = []
emails = []
passwords = []
numbers = []


def random_name_generator(num, is_rand, name):
    if is_rand:
        for e in range(0, num):
            name_file = requests.get('https://www.name-generator.org.uk/quick/').text
            soup = BeautifulSoup(name_file, 'html.parser')
            name = soup.find('div', class_ = 'name_heading').text
            names.append(name)
    else:
        for e in range(0, num):
            names.append(name)
    return names


def random_email_generator(num):
    for e in range(0, num):
        email_file = requests.get('http://www.yopmail.com/en/email-generator.php').text
        soup = BeautifulSoup(email_file, 'html.parser')
        email = soup.find('input', id = 'login')['value']
        emails.append(email)
    return emails


def random_password_generator(num):
    for e in range(0, num):
        MAX = 12
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                             'z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                             'Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                   '*', '(', ')', '<']
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        rand_any = random.choice(COMBINED_LIST)
        password = ""
        for e in range(0, MAX):
            password = password + rand_any
            rand_any = random.choice(COMBINED_LIST)
        passwords.append(password)
    return passwords


def random_number_generator(num):
    for e in range(0, num):
        number_file = requests.get('https://www.randomphonenumbers.com/').text
        soup = BeautifulSoup(number_file, 'html.parser')
        number_blocks = soup.find('li', class_ = 'col-md-6 col-sm-6 col-xs-12')
        for number_block in number_blocks:
            phone_num = number_block.find('a').text
            numbers.append(phone_num)
    return numbers


def write_csv_file(fields, name, email, password, number, client_email):
    rows = []

    for e in range(0, len(name)):
        row = [name[e], email[e], password[e], number[e]]
        rows.append(row)

    file_name = 'accounts.csv'

    with open(file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    email_user = 'pydev789@gmail.com'
    email_password = 'EvanSoccer$34$'
    email_send = client_email

    subject = 'Accounts'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'The file below has the accounts. To check the emails, go to http://www.yopmail.com/en/ and type in the email in the search bar.'
    msg.attach(MIMEText(body, 'plain'))

    filename = 'accounts.csv'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.ehlo()
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()

    os.remove('accounts.csv')
