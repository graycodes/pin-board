import email
import imaplib
import pdb

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('theemailitestwith@gmail.com', 'm00nfruit')
mail.list()
mail.select("INBOX")

result, data = mail.uid('search', None, "ALL")
latest_email_uid = data[0].split()[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
raw_email = data[0][1]

email_message = email.message_from_string(raw_email)

author = email.utils.parseaddr(email_message['From'])[1]


def get_first_text_block(email_message_instance):
    message_block = email_message_instance.get_payload()
    result = gray(message_block)
    print result


def gray(msg):
    if msg[0].get_content_maintype() == 'multipart':
        return find_txt(msg[0].get_payload())
    else:
        return msg[0].get_payload()


def find_txt(msg):
    text = ''
    for part in msg:
        if part.get_content_type() == 'text/plain':
            text = part.get_payload()
    return text

get_first_text_block(email_message)
