def isPhoneNumber(text):   # 414-555-
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no are code
    if text[3] != '-':
        return False # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no fitst 3 digits
    if text[7] != '-':
        return False # missing dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True


message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Cound not find any phone numbers.')
    
