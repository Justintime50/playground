import pytest


@pytest.fixture
def mock_path():
    mock_path = './'

    return mock_path


@pytest.fixture
def mock_csv_path():
    mock_csv_path = './test_csv.csv'

    return mock_csv_path


@pytest.fixture
def mock_headers():
    mock_headers = [
        ['header1'],
        ['header2'],
        ['header3'],
    ]

    return mock_headers


@pytest.fixture
def mock_data():
    mock_data = [
        ['data1'],
        ['data2'],
        ['data3'],
    ]

    return mock_data
