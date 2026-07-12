from filters.rules import is_important


def test_urgent():

    assert is_important(
        {"subject": "URGENT"}
    )


def test_newsletter():

    assert not is_important(
        {"subject": "Newsletter BDE"}
    )
