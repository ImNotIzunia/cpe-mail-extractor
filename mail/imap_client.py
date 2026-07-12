import email
import imaplib

from mail.decoder import decode
from mail.model import Mail


class ImapClient:

    def __init__(self, host, port, email, password):
        self.client = imaplib.IMAP4_SSL(host, port)
        self.client.login(email, password)

    def unread(self) -> list[Mail]:
        self.client.select("INBOX")

        _, data = self.client.search(None, "UNSEEN")

        mails = []

        for uid in data[0].split():
            _, raw = self.client.fetch(uid, "(RFC822)")

            msg = email.message_from_bytes(raw[0][1])

            mails.append(
                Mail(
                    uid=int(uid),
                    sender=decode(msg["From"]),
                    subject=decode(msg["Subject"]),
                    date=msg["Date"],
                )
            )

        return mails

    def close(self):
        self.client.close()
        self.client.logout()