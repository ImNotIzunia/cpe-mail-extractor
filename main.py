import json
import os

from dotenv import load_dotenv

from filters.rules import is_important
from mail.imap_client import ImapClient
from notify.console import notify


load_dotenv()

STATE_FILE = "data/state.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {"last_uid": 0}
    
    with open(STATE_FILE) as f:
        return json.load(f)
    

def save_state(uid):
    with open(STATE_FILE, "w") as f:
        json.dump({"last_uid": uid}, f)


state = load_state()


client = ImapClient(
    os.getenv("IMAP_SERVER"),
    int(os.getenv("IMAP_PORT")),
    os.getenv("EMAIL"),
    os.getenv("PASSWORD")
)


mails = client.unread()

last = state["last_uid"]


for mail in mails:

    if mail["uid"] <= last:
        continue

    if is_important(mail):
        notify(mail)

    last = max(last, mail["uid"])


save_state(last)

client.close()


