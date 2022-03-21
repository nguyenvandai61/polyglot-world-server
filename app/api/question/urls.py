from django.urls import include, path
from .api import QuestionApi, QuestionDetail, QuestionMyApi, QuestionRandom, QuestionUpvote, QuestionDownvote, QuestionSubmitAnswer, QuestionTypeApi


urlpatterns = [
    path('', QuestionApi.as_view(), name='question'),
    path('me/', QuestionMyApi.as_view(), name='question_detail'),
    path('<int:pk>/', QuestionDetail.as_view(), name='question_detail'),
    path('<int:pk>/upvote/', QuestionUpvote.as_view(), name='question_upvote'),
    path('<int:pk>/downvote/', QuestionDownvote.as_view(), name='question_downvote'),
    path('<int:pk>/submit/', QuestionSubmitAnswer.as_view(), name='question_submit'),
    path('random/', QuestionRandom.as_view(), name='question_random'),
    path('type/', QuestionTypeApi.as_view(), name='question_type'),
]