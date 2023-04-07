import uuid
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import requests

from records.models import Record


class Command(BaseCommand):
    help = 'Fetches a given record by ID from the National Archives API, and stores the data in the database.'
    
    def add_arguments(self, parser):
        parser.add_argument('record_id', type=uuid.UUID)


    def handle(self, *args, **options):
        record_id = options['record_id']
        record_url = f"{settings.NA_API_BASE}{record_id}"
        
        # send GET request to URL to fetch the JSON data
        response = requests.get(record_url)

        # check if the record ID did not find a relevant record from the API
        if response.status_code == 204:
            raise CommandError(f"No record was found with ID {record_id}")
        
        # with a valid response, convert data to a Python dictionary and extract fields of interest
        record_data = response.json()
        model_data = {
            'id': record_data.get('id'),
            'title': record_data.get('title'),
            'citable_reference': record_data.get('citableReference'),
            'description': record_data.get('scopeContent', {}).get('description')
        }

        # Store data in the database if it doesn't already exist
        record, created = Record.objects.get_or_create(**model_data)

        if created:
            print("Record successfully added to the database.")
        else:
            print(f"Record with ID {record_id} already exists in the database.")