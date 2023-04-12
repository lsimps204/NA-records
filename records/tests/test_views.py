import uuid
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_valid_record_is_in_context(client, record_instance):
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': record_instance.id}
    )
    response = client.get(detail_endpoint)
    assert response.context['record'] == record_instance

@pytest.mark.django_db
def test_response_with_record_id_that_does_not_exist(client):
    invalid_uuid = uuid.uuid4()
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': invalid_uuid}
    )
    response = client.get(detail_endpoint)
    assert response.context['record'] is None
    assert f"No record found" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_title_shown_on_record(client, record_factory):
    record_with_title = record_factory()
    record_without_title = record_factory(title=None)

    # ensure title shown when the field is non-null on the record
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': record_with_title.id}
    )
    response = client.get(detail_endpoint)
    assert f"Title: {record_with_title.title}" in response.content.decode("utf-8")

    # ensure title is NOT shown when the field is null on the record
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': record_without_title.id}
    )
    response = client.get(detail_endpoint)
    assert f"Title:" not in response.content.decode("utf-8")


@pytest.mark.django_db
def test_description_shown_on_record(client, record_factory):
    record_with_description = record_factory(title=None)
    record_without_description = record_factory(title=None, description=None)

    # ensure description shown when the field is non-null on the record
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': record_with_description.id}
    )
    response = client.get(detail_endpoint)
    assert f"Description: {record_with_description.description}" in response.content.decode("utf-8")

    # ensure description is NOT shown when the field is null on the record
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': record_without_description.id}
    )
    response = client.get(detail_endpoint)
    assert f"Description:" not in response.content.decode("utf-8")


@pytest.mark.django_db
def test_reference_is_shown_on_record(client, record_factory):
    record_with_reference = record_factory(title=None, description=None)
    record_without_reference = record_factory(title=None, description=None, citable_reference=None)

    # ensure reference is shown when the field is non-null on the record
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': record_with_reference.id}
    )
    response = client.get(detail_endpoint)
    assert f"Citable Reference: {record_with_reference.citable_reference}" in response.content.decode("utf-8")

    # ensure reference is NOT shown when the field is null on the record
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': record_without_reference.id}
    )
    response = client.get(detail_endpoint)
    assert f"Citable Reference:" not in response.content.decode("utf-8")


@pytest.mark.django_db
def test_not_sufficient_information_is_displayed_when_fields_are_null(client, record_factory):
    record_with_null_fields = record_factory(title=None, description=None, citable_reference=None)
    detail_endpoint = reverse(
        'record-detail', kwargs={'record_id': record_with_null_fields.id}
    )
    response = client.get(detail_endpoint)
    assert f"Not sufficient information" in response.content.decode("utf-8")