from django.http import JsonResponse
from .models import Drink
from serializers import DrinkSerializer


def drink_list(request):

#get drinks
    drinks = Drink.objects.all
    #serialize
    serializer = DrinkSerializer(drinks, many=True)
    #return json
    return JsonResponse(serializer.data)



