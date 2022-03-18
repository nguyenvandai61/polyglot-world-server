from rest_framework import generics
from rest_framework.response import Response
from app.api.predict.language_predictor_serivces import LanguagePredictorServices

from app.api.predict.predictnextword_services import PredictNextWordServices
from app.mserializers.PredictSerialzers import PredictLanguageSerializer
from drf_yasg.utils import swagger_auto_schema


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

class GetWordDict(generics.GenericAPIView):

		def get(self, request, *args, **kwargs):
				try:
						results = PredictNextWordServices().get_word_in_dict(kwargs['substart_word'])
				except Exception as e:
						return Response({'status': 'error', 'message': str(e)})
				return Response({
						'results': results
				})
    
    
class PredictLanguageApi(generics.GenericAPIView):
    
    @swagger_auto_schema(request_body=PredictLanguageSerializer)
    def post(self, request, *args, **kwargs):
        paragraph = request.data['paragraph']
        try:
            results = LanguagePredictorServices().predict(paragraph)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)})
        return Response({
            'results': results
        })