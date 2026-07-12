from mail.decoder import decode


def test_decode():

    subject = "=?utf-8?Q?Remise_des_dipl=C3=B4mes?="

    assert decode(subject) == "Remise des diplômes"
