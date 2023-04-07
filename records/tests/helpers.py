from io import StringIO
from django.core.management import call_command


def call_api_command(self, *args, **kwargs):
    call_command(
        "get_record_data",
        *args,
        stdout=StringIO(),
        stderr=StringIO(),
        **kwargs,
    )