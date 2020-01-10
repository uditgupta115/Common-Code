# __author__ = 'Udit Gupta'
import base64
import logging
import os
from datetime import datetime
from logging.handlers import SMTPHandler

from decouple import config

from utils import check_or_create_path, EmailServer

admin_email = config('admin_email')
password = base64.decodebytes(config('password').encode()).decode()
hostname = config('hostname')
port = config('port')
to_email = config('user_email')
is_mail_triggered = bool(config('mail_trigger') == 'True')
admins = [to_email]

# create logger
dt_fmt = "%d-%m-%Y %H:%M:%S"
log_folder = os.getcwd() + os.sep + 'logs' + os.sep
check_or_create_path(log_folder)
file_path = f'{log_folder}onslowcountync_{datetime.now().strftime(dt_fmt)}'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f'{file_path}.log', mode='a')
file_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", dt_fmt)
# add formatter to ch
ch.setFormatter(formatter)
file_handler.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(file_handler)

smtp_loggger_handler = SMTPHandler(
    mailhost=(hostname, port),
    fromaddr=admin_email,
    credentials=(admin_email, password),
    toaddrs=admins,
    subject=u"Zillow OnSlowCounty Parsing Error"
)

if is_mail_triggered:
    smtp_loggger_handler.setLevel(logging.ERROR)
    logger.addHandler(smtp_loggger_handler)


def trigger_email(subject, msg, to=None, cc=None, bcc=None):
    if not is_mail_triggered:
        return
    if to is None:
        to = admins[0]
    email = EmailServer(hostname, port, admin_email, password)
    email.send(subject=subject, msg=msg, to=to, cc=cc, bcc=bcc)
    logger.info(f"Email sent to {to} with {subject}")
