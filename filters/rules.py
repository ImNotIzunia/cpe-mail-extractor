KEYWORDS = [

]

IGNORED = [
    "newsletter",
]


def is_important(mail):

    subject = mail.subject.lower()

    if any(word in subject for word in IGNORED):
        return False

    if not KEYWORDS:
        return True
    
    else:
        return any(word in subject for word in KEYWORDS)
