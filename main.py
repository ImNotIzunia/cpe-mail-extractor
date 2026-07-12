import logging

from config import settings
from utils.logger import setup_logger

from mail.imap_client import ImapClient
from filters.rules import is_important
from notify.discord import notify

from data.state import (
    load_state,
    save_state,
    is_processed,
    mark_processed,
)


setup_logger()
logger = logging.getLogger(__name__)


def main():

    logger.info("Starting CMA")

    state = load_state()

    client = None

    try:
        client = ImapClient(
            settings.imap_server,
            settings.imap_port,
            settings.email,
            settings.password,
        )

        logger.info("Connected to IMAP server")

        mails = client.unread()

        logger.info(
            "Found %s unread mails",
            len(mails),
        )

        important_count = 0

        for mail in mails:

            if is_processed(mail.uid, state):
                logger.debug(
                    "Mail %s already processed",
                    mail.uid,
                )
                continue


            if is_important(mail):

                logger.info(
                    "Important mail detected: %s",
                    mail.subject,
                )

                notify(
                    mail,
                    settings.discord_webhook
                )

                important_count += 1

            else:

                logger.info(
                    "Ignored mail: %s",
                    mail.subject,
                )


            mark_processed(
                mail.uid,
                state
            )


        save_state(state)

        logger.info(
            "Processed %s important mails",
            important_count,
        )


    except Exception:
        logger.exception(
            "CMA crashed"
        )

        raise


    finally:

        if client:
            client.close()

            logger.info(
                "IMAP connection closed"
            )


if __name__ == "__main__":
    main()


    