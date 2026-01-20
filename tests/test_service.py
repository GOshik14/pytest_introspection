import pytest
from requests import HTTPError
import sys
sys.path.append("/home/egor/Python/pytest_introspection/source")
import source.service as service
import unittest.mock as mock

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_df(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked_Alice"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked_Alice"

@mock.patch("source.service.get_users_json")
def test_get_users_json(mock_get_users_json):
    mock_get_users_json.return_value = {1: "Mocked_user_1", 
                                        2: "Mocked_user_2",
                                        3: "Mocled_user_3"}

    expected_responce = {1: "Mocked_user_1", 
                        2: "Mocked_user_2",
                        3: "Mocled_user_3"}
    
    assert mock_get_users_json(service.GET_JSON_HTTPS_ADDR) == expected_responce

@mock.patch("requests.get")
def test_get_users(mock_requests_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}

    mock_requests_get.return_value = mock_response

    data = service.get_users_json()
    
    expected_json = {"id": 1, "name": "John Doe"}

    assert data == expected_json

@mock.patch("requests.get")
def test_get_users_http_err(mock_requests_get):
    mock_responce_error = mock.Mock()
    mock_responce_error.status_code = 404 
    
    mock_requests_get.return_value = mock_responce_error

    with pytest.raises(HTTPError):
        service.get_users_json()          
