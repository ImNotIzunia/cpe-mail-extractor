import logging

from config import settings
from mail.imap_client import ImapClient
from filters.rules import is_important
from notify.discord import notify

from data.state import (
    load_state,
    save_state,
    is_processed,
    mark_processed,
)


logging.basicConfig(
    level=logging.INFO,
)


state = load_state()


client = ImapClient(
    settings.imap_server,
    settings.imap_port,
    settings.email,
    settings.password,
)


mails = client.unread()


for mail in mails:

    if is_processed(mail.uid, state):
        continue

    if is_important(mail):

        notify(
            mail,
            settings.discord_webhook
        )

    mark_processed(
        mail.uid,
        state
    )


save_state(state)

client.close()