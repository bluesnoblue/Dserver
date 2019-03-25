from django.urls import path
from .views import IndexView,DetailView,ResultsView,vote
from .apiview import QuestionList, QuestionDetail,ChoiceList

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('api/',QuestionList.as_view(),name='polls_list'),
    path('api/<int:pk>/',QuestionDetail.as_view(),name='poll_detail'),
    path('api/<int:pk>/choices', ChoiceList.as_view(), name='choices_list')
]
