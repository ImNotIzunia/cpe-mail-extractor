import requests


def notify(mail, webhook):

    payload = {
        "embeds": [
            {
                "title": "Nouveau mail recu",
                "description": mail.subject,

                "fields": [
                    {
                        "name": "Expéditeur",
                        "value": mail.sender,
                        "inline": False,
                    },
                    {
                        "name": "Date",
                        "value": mail.date,
                        "inline": False,
                    },
                    {
                        "name": "UID",
                        "value": str(mail.uid),
                        "inline": False,
                    },
                ],
            }
        ]
    }


    response = requests.post(
        webhook,
        json=payload,
        timeout=10,
    )


    response.raise_for_status()