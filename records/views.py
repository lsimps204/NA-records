from django.shortcuts import render, get_object_or_404
from records.models import Record

# Create your views here.
def record_detail(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    context = {
        'record': record
    }
    return render(request, 'records/record-detail.html', context)