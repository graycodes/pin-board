import email
import imaplib
import pdb

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('theemailitestwith@gmail.com', 'm00nfruit')
mail.list()
mail.select("INBOX")

result, data = mail.search(None, "ALL")
ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

# result, data = mail.fetch(latest_email_id, "(RFC822)")

result, data = mail.uid('search', None, "ALL")
                        # search and return uids instead
latest_email_uid = data[0].split()[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
raw_email = data[0][1]
# print raw_email
email_message = email.message_from_string(raw_email)

print email.utils.parseaddr(email_message['From'])[1]


def get_first_text_block(email_message_instance):
    message_block = email_message_instance.get_payload()
    #result = traverse_multipart(message_block)
    
    result = gray(message_block)

    print result

def traverse_multipart(message_block):
    result = ''
    #pdb.set_trace()
    #for part in message_block:
    part = message_block.pop(0)
    if part.get_content_maintype() == 'multipart':
        traverse_multipart(part.get_payload())
    elif part.get_content_type() == 'text/plain':
    	result = part.get_payload()
    # print result
    return result

def gray(msg):
	if msg[0].get_content_maintype() == 'multipart':
		return find_txt(msg[0].get_payload())
	else:
		return msg.get_payload()

def find_txt(msg):
	text = ''
	for part in msg:
		if part.get_content_type() == 'text/plain':
			text = part.get_payload()
	return text

get_first_text_block(email_message)
# print traverse_multipart(email_message.get_payload())
 	