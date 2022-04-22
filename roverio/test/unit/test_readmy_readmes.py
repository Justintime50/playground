import os
import tempfile
from unittest.mock import patch

import pytest

from roverio.readmy_readmes import ReadmyReadmes


@patch('roverio.readmy_readmes.ReadmyReadmes.iterate_readmes')
def test_run_cli(mock_iterate_readmes, mock_path):
    temp = tempfile.NamedTemporaryFile(delete=False, dir='test/unit')
    temp.write(b'install\nusage\ntodo\ntest')
    temp.close()

    _ = ReadmyReadmes.run_cli(mock_path, temp)

    mock_iterate_readmes.assert_called_once_with(mock_path, temp, False, 'readmy_readmes.csv', False)
    os.unlink(temp.name)


def test_iterate_readmes(mock_path):
    temp = tempfile.NamedTemporaryFile(delete=False, dir='test/unit')
    temp.write(b'install\nusage\ntodo\ntest')
    temp.close()

    table = ReadmyReadmes.iterate_readmes(mock_path, temp.name)

    # fmt: off
    assert table == (
        '| README File | install | usage | todo | test |\n'
        '| ----------- | ------- | ----- | ---- | ---- |\n'
        '| README.md   | True    | True  | True | True |'
    )
    # fmt: on
    os.unlink(temp.name)


@patch('roverio.readmy_readmes.ReadmyReadmes._create_csv')
def test_iterate_readmes_calls_create_csv(mock_csv, mock_path):
    temp = tempfile.NamedTemporaryFile(delete=False, dir='test/unit')
    temp.write(b'install\nusage\ntodo\ntest')
    temp.close()

    _ = ReadmyReadmes.iterate_readmes(mock_path, temp.name, True, 'readmy_readmes.csv', False)

    mock_csv.assert_called_once()
    os.unlink(temp.name)


def test_find_readmes_success(mock_path):
    readme_list = ReadmyReadmes.find_readmes(mock_path)

    assert 'README.md' in readme_list[0]


def test_find_readmes_error():
    mock_path = './test'
    with pytest.raises(FileNotFoundError) as error:
        _ = ReadmyReadmes.find_readmes(mock_path)

    assert 'No README files were found with the specified path.' in str(error.value)


def test_check_rules_in_readme_not_lazy(mock_path):
    readme_contents = ReadmyReadmes._open_readme_file('README.md')
    result = ReadmyReadmes._check_rules_in_readme(readme_contents, 'test')

    assert result is True


@pytest.mark.parametrize(
    'lazy, rule, expected_value',
    [
        # This is flakey, but we test that we can either find the uppercase
        # word `coverage` or not depending on the `lazy` flag
        (True, 'coverage', True),
        (False, 'coverage', False),
        (True, 'bad-string', False),
    ],
)
def test_check_rules_in_readme(lazy, rule, expected_value, mock_path):
    """Tests that we properly can find rules by lazy searching
    (case insensitive) as well as explicitly matching (non-case-sensitive)
    """
    readme_contents = ReadmyReadmes._open_readme_file('README.md')
    result = ReadmyReadmes._check_rules_in_readme(readme_contents, rule, lazy)

    assert result is expected_value


@patch('builtins.open')
@patch('csv.writer')
def test_create_csv(mock_csv, mock_open, mock_headers, mock_data, mock_csv_path):
    ReadmyReadmes._create_csv(mock_headers, mock_data, mock_csv_path)

    mock_csv.assert_called_once()


@patch('csv.writer')
def test_create_csv_exception(mock_csv, mock_headers, mock_data, mock_path):
    # We use "mock_path" here as it's a directory and not a file path
    with pytest.raises(Exception) as error:
        ReadmyReadmes._create_csv(mock_headers, mock_data, mock_path)

    assert '[Errno 21] Is a directory: \'./\'' in str(error.value)
