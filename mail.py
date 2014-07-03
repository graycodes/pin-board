import email
import imaplib

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
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        # for part in email_message_instance.get_payload():
        #     if part.get_content_maintype() == 'text':
        #         return part.get_payload()
        return traverse_multipart(email_message_instance.get_payload())
    elif maintype == 'text':
        return email_message_instance.get_payload()

def traverse_multipart(message_block):
	for part in message_block:
		print part.get_content_maintype()
		if part.get_content_maintype() == 'multipart':
			traverse_multipart(part.get_payload())
		elif part.get_content_maintype() == 'text':
			print part.get_payload()

print get_first_text_block(email_message)
