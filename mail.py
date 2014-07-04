from email.parser import HeaderParser
import email
import imaplib
import pdb
from datetime import datetime, date

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('theemailitestwith@gmail.com', 'm00nfruit')
mail.list()
mail.select("INBOX")

result, data = mail.uid('search', None, "ALL")
email_uids = data[0].split()
emails_length = len(email_uids)
latest_email_uid = email_uids[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')

raw_email = data[0][1]

def get_uid(id):
    return email_uids[id]

def get_raw_email(id):
    return mail.uid('fetch', get_uid(id), '(RFC822)')[0][1]

# for i in range(1, int(latest_email_uid)):
#     typ, msg_data = mail.fetch(str(i), '(RFC822)')
#     for response_part in msg_data:
#         if isinstance(response_part, tuple):
#             msg = email.message_from_string(response_part[1])
#             for header in [ 'subject', 'to', 'from' ]:
#                 print '%-8s: %s' % (header.upper(), msg[header])


def get_headers():
    typ, msg_data = mail.fetch(2, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            for header in [ 'subject', 'to', 'from' ]:
                print '%-8s: %s' % (header.upper(), msg[header])

def get_first_text_block(email_message_instance):
    message_block = email_message_instance.get_payload()
    result = traverse_block(message_block)
    return result


def traverse_block(msg):
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

def get_body(id):
    email_message = email.message_from_string()
    return get_first_text_block(email_message)


email_message = email.message_from_string(raw_email)

author = email.utils.parseaddr(email_message['From'])[1]

body = get_first_text_block(email_message)

#print "Author: " + author + "\n\n\n"
#print "Body: " + body + "\n\n\n"

get_headers()

def get_title(id):
    typ, msg_data = mail.fetch(id, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            for header in [ 'subject' ]:
                return '%s' % (msg[header])
    

def get_contents(id):
    return {
        title: get_title(id),
        body: get_body(id),
        author: get_author(id),
        timestamp: date().isoformat()
    }

for email_id in range(1, emails_length):
    #read the contents
    #send to db
    #mark as "read'
    #contents = get_contents(email_id)
    print "hello"
print get_title(1)
print get_body(1)
