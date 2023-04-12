import uuid
from unittest import mock
import pytest

from records.models import Record
from records import response_utils


@pytest.fixture
def api_response_dict():
    """ Fixture that exposes data that mimics the API response from NA """
    return {
        'id': uuid.uuid4(),
        'title': 'xyz',
        'scopeContent': {'description': 'test description'},
        'citableReference': 'this is a citation'
    }


@pytest.mark.django_db
@pytest.fixture
def record_instance(api_response_dict):
    """ Fixture that returns a Record database object """
    data = response_utils.map_json_data_to_modelfields(api_response_dict)
    return Record.objects.create(**data)


@pytest.fixture
def record_factory():
    """ Factory fixture allowing flexible creation of Record instances. """
    def create(title="Title1", description="Description", citable_reference="MyRef"):
        id = uuid.uuid4()
        return Record.objects.create(id=id, title=title, description=description, citable_reference=citable_reference)
    
    return create