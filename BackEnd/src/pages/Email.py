import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import MAIL_PASS

def send_email(subject, message, to_email):

    # Настройки для подключения к серверу SMTP mail.ru
    smtp_server = 'smtp.mail.ru'
    port = 587
    sender_email = 'akentev.dima@bk.ru'  # Ваш адрес электронной почты на mail.ru
    sender_password = MAIL_PASS  # Ваш пароль от электронной почты на mail.ru

    # Создание объекта сообщения
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Добавление текста письма
    msg.attach(MIMEText(message, 'plain'))

    # Подключение к серверу SMTP
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
