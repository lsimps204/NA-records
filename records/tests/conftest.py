import uuid
from unittest import mock
import pytest



@pytest.fixture
def record_model_dict():
    return {
        'id': uuid.uuid4(),
        'title': 'xyz',
        'description': 'test description',
        'citation_reference': 'this is a citation'
    }