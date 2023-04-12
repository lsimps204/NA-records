from django.shortcuts import render
from records.models import Record

# Create your views here.
def record_detail(request, record_id):
    try:
        record = Record.objects.get(id=record_id)
    except Record.DoesNotExist:
        record = None
    
    return render(request, 'records/record-detail.html', {'record': record})