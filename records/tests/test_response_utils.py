import pytest 
from records.response_utils import map_json_data_to_modelfields
from records.models import Record


@pytest.mark.django_db
def test_mapping_creates_valid_record_model(api_response_dict):
    # test that the structure as returned by API raises an error
    with pytest.raises(TypeError):
        Record.objects.create(**api_response_dict)

    # test the mapping allows Record creation.
    data = map_json_data_to_modelfields(api_response_dict)
    record = Record.objects.create(**data)
    assert Record.objects.filter(id=record.id).exists()