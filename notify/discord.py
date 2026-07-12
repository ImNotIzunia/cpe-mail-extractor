import requests


def notify(mail, webhook):

    data = {
        "content":
        f""" Nouvel email de CPE
        
        **De :** {mail.sender}
        **Objet :** {mail.subject}
        **Date :** {mail.date}*
        """
    }

    requests.post(
        webhook,
        json=data,
        timeout=10,
    )
