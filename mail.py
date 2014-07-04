from pymongo import MongoClient
from email.parser import HeaderParser
import email
import imaplib
import pdb
from datetime import datetime, date

## MONGO CONFIG
client = MongoClient('eagle', 27017)
db = client['fullstack-dev']
collection = db.notifications

###IMAP CONFIG
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
    id = id - 1#FIXME?
    return email_uids[id]

def get_raw_email(id):
    result, data = mail.uid('fetch', get_uid(id), '(RFC822)')
    return data[0][1]

def move_to_done(id):
    print "rar:"
    print id

    typ, data = mail.uid('STORE', get_uid(id), '+X-GM-LABELS', 'DONE')
    print "typ"
    print typ

    # result = mail.uid('COPY', get_uid(id), 'Deleted')
    # print result[0]
    # if result[0] == 'OK':
    #     mov, data = mail.uid('STORE', get_uid(id) , '+FLAGS', '(\Deleted)')
    #     print "mov"
    #     print mov
    #     mail.expunge()

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
    email_message = email.message_from_string(get_raw_email(id))
    return get_first_text_block(email_message)


email_message = email.message_from_string(raw_email)

author = email.utils.parseaddr(email_message['From'])[1]

body = get_first_text_block(email_message)

#print "Author: " + author + "\n\n\n"
#print "Body: " + body + "\n\n\n"

#get_headers()

def get_author(id):
    typ, msg_data = mail.fetch(id, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            for header in [ 'from' ]:
                return '%s' % (msg[header])
    

def get_title(id):
    typ, msg_data = mail.fetch(id, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            for header in [ 'subject' ]:
                return '%s' % (msg[header])

def get_labels(id):
    typ, data = mail.uid('FETCH', get_uid(id), '(X-GM-LABELS)')
    return data

def get_contents(id):
    return dict([
        ('title', get_title(id)),
        ('body', get_body(id)),
        ('author', get_author(id)),
        ('timestamp', datetime.now().isoformat())
    ])

for email_id in range(1, emails_length + 1):

    #IFF THE EMAIL DOESN'T HAVE THE "DONE" FLAG
    print get_labels(email_id)
    if get_labels(email_id)[0].find('DONE') != -1:
        print 'found that thing'
        continue

    #read the contents
    contents = get_contents(email_id)
    print contents

    #send to db
    post_id = collection.insert(contents)
    print post_id

    #mark as "read"
    move_to_done(email_id)

mail.logout()
