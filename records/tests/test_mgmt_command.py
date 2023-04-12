import pytest
from unittest.mock import Mock, patch
from django.core.management import call_command
from django.core.management.base import CommandError
from records.management.commands.get_record_data import Command
from records.models import Record

RECORD_ID = "a147aa58-38c5-45fb-a340-4a348efa01e6"


@patch("records.management.commands.get_record_data.requests.get")
def test_get_records_from_NA_api(mock_get, api_response_dict):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value = Mock()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = api_response_dict

    response_data = Command().call_api(RECORD_ID)
    assert response_data == api_response_dict


@patch("records.management.commands.get_record_data.requests.get")
def test_api_call_with_invalid_id_raises_command_error(mock_get):
    mock_get.return_value = Mock()
    mock_get.return_value.status_code = 204

    with pytest.raises(CommandError):
        Command().call_api(RECORD_ID)



@pytest.mark.django_db
@patch("records.management.commands.get_record_data.Command.call_api")
def test_api_call_creates_model_object(mock_response, api_response_dict):
    mock_response.return_value = api_response_dict
    
    # call the management command and assert that the API data is added to the DB
    call_command('get_record_data', RECORD_ID)
    assert Record.objects.count() == 1
    assert Record.objects.filter(pk=api_response_dict['id']).exists()

    # call command again and ensure a duplicate is not added
    call_command('get_record_data', RECORD_ID)
    assert Record.objects.count() == 1
    