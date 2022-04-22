from roverio import file_extension


def test_file_extension():
    result = file_extension.FileExtension.search_file_extensions('roverio', '.py')

    assert 'roverio/file_extension.py' in result


def test_file_extension_no_results():
    result = file_extension.FileExtension.search_file_extensions('roverio', '.txt')

    assert result == []
