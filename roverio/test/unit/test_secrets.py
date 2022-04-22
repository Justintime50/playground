from roverio import secrets


def test_secrets_no_gitignore():
    """This test isn't great but asserts against something that should
    hopefully stay pretty constant - `setup.py`.
    """
    result = secrets.Secrets.search_for_secrets('roverio', 22)

    assert 'File: roverio/sequential_renamer.py\nSecret: IMG_2462_proc_592015324\nLine: 57\n' in result


def test_secrets_gitignore():
    """This test isn't great but asserts against something that should
    hopefully stay pretty constant - `setup.py`.
    """
    result = secrets.Secrets.search_for_secrets('./', 20)

    assert 'File: ./setup.py\nSecret: long_description_content_type\nLine: 27\n' in result
