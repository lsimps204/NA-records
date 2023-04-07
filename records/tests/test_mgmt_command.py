import pytest
from unittest.mock import Mock, patch
from django.core.management.base import CommandError
from records.management.commands.get_record_data import Command

RECORD_ID = 'a147aa58-38c5-45fb-a340-4a348efa01e6'

@patch('records.management.commands.get_record_data.requests.get')
def test_get_records_from_NA_api(mock_get, record_model_dict):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value = Mock()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = record_model_dict

    response_data = Command().call_api(RECORD_ID)
    assert response_data == record_model_dict


@patch('records.management.commands.get_record_data.requests.get')
def test_api_call_with_invalid_id_raises_command_error(mock_get, record_model_dict):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value = Mock()
    mock_get.return_value.status_code = 204

    with pytest.raises(CommandError):
        Command().call_api(RECORD_ID)