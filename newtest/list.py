
from django.shortcuts import render_to_response

address = [
    {'name':'zhansan ', 'address':'我靠'},
    {'name':'死定了你', 'address':'我靠'}
    ]

def index(request):
    return render_to_response('list.html', {'address': address})