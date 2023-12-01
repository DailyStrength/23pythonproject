import imaplib
import email
from email import policy

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode =info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL(``)