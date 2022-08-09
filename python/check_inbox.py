
# pip install imapclient
# pip install pyzmail36

import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('gmail_address','password') # Enter gmail address and password
conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE DD-MM-YYYY'])   # Enter date
UIDS

conn.fetch([xxxx],['BODY[]', 'FLAGS'])  #xxxx stands for one of UIDs key
rawMessage = conn.fetch([xxxx],['BODY[]', 'FLAGS'])

import pyzmail
pyzmail.PyzMessage.factory(rawMessage[xxxx][b'BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessage[xxxx][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')

message.get_addresses('bcc')

message.text_part
message.html_part
message.html_part == None

message.text_part.get_payload().decode('UTF-8')

message.text_part.chartset
message.text_part.chartset == None

conn.list_folders()

conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['ON DD-MM-YYYY'])    # Enter date
UIDs
# Delete all UIDs
conn.delete_messages([UIDs])
