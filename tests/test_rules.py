from mail.model import Mail
from filters.rules import is_important


def create_mail(subject):

    return Mail(
        uid=1,
        sender="test@cpe.fr",
        subject=subject,
        date="",
    )


def test_urgent():

    assert is_important(
        create_mail("URGENT")
    )


def test_newsletter():

    assert not is_important(
        create_mail("Newsletter BDE")
    )