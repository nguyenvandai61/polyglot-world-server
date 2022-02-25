from rest_framework import generics
from rest_framework.response import Response

from app.api.predict.predictnextword_services import PredictNextWordServices


class PredictNextWordDict(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        last_word = kwargs['last_word']
        try:
            results = PredictNextWordServices().predict_next_word_dict(last_word)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)})
        return Response({
            'results': results
        })
