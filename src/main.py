import os
import imaplib
from dotenv import load_dotenv

load_dotenv()

serveur = os.environ.get("SERVER")
utilisateur = os.environ.get("EMAIL")
mot_de_passe = os.environ.get("PASSWORD")

print("Serveur :", serveur)
print("Utilisateur :", utilisateur)

try:
    mail = imaplib.IMAP4_SSL(serveur, 993)

    mail.login(utilisateur, mot_de_passe)

    print("Connexion réussie !")

    mail.select("INBOX")

    status, messages = mail.search(None, "UNSEEN")

    print("Mails non lus :", messages[0].split())

    mail.logout()

except Exception as e:
    print("Erreur :", e)