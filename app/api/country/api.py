import json
from django.http.response import JsonResponse

from rest_framework.views import APIView


class CountryList(APIView):

    def get(self, request, *args, **kwargs):
        """
        Return a list of all the countries.
        """
        json_file = 'app/data/countries.json'
        countries = self.__load_all_contries(json_file)
        if countries:
            return JsonResponse(countries['countries'], safe=False)
        return JsonResponse({'error': 'No countries found'}, safe=False)

    def __load_all_contries(self, json_file):
        """
        Load all the countries from the json file.
        """
        with open(json_file) as f:
            data = json.load(f)
        return data