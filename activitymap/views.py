from django.shortcuts import render
from django.utils import timezone
from .models import Marker

def post_list(request):
    marker = Marker.objects.filter(time__lte=timezone.now()).order_by('time')
    return render(request, 'activitymap/activity.html', {'marker':marker})
