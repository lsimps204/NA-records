import uuid
from unittest import mock
import pytest



@pytest.fixture
def api_response_dict():
    """ Fixture that exposes data that can be used to create a Record database object """
    return {
        'id': uuid.uuid4(),
        'title': 'xyz',
        'scopeContent': {'description': 'test description'},
        'citableReference': 'this is a citation'
    }