from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # your registration logic here
        return JsonResponse({'message': 'User registered'}, status=201)
    return JsonResponse({'error': 'POST required'}, status=400)