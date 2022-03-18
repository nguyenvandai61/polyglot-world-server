from django.urls import include, path
from .api import QuestionApi, QuestionDetail, QuestionRandom, QuestionUpvote, QuestionDownvote, QuestionSubmitAnswer, QuestionTypeApi


urlpatterns = [
    path('', QuestionApi.as_view(), name='question'),
    path('<int:pk>/', QuestionDetail.as_view(), name='question_detail'),
    path('<int:pk>/upvote/', QuestionUpvote.as_view(), name='question_upvote'),
    path('<int:pk>/downvote/', QuestionDownvote.as_view(), name='question_downvote'),
    path('<int:pk>/submit/', QuestionSubmitAnswer.as_view(), name='question_submit'),
    path('random/', QuestionRandom.as_view(), name='question_random'),
    path('type/', QuestionTypeApi.as_view(), name='question_type'),
]