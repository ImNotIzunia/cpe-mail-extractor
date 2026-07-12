from filters.rules import is_important
from mail.model import Mail


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