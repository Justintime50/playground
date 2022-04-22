from roverio import phone_email_searcher


def test_phone_searcher():
    result = phone_email_searcher.PhoneEmailSearcher.search_for_phone(path='./roverio')

    assert [any('8015551234' in item for item in result)]


def test_email_searcher():
    result = phone_email_searcher.PhoneEmailSearcher.search_for_email('./roverio')

    assert [any('anything@anything.anything' in item for item in result)]
