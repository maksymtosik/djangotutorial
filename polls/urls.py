from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'), # /polls/
    # path('', views.construction, name='construction'),
    path('<int:questionID>/', views.details, name = 'details'), # /polls/x/
    path('<int:questionID>/results/', views.results, name = 'results'), # /polls/x/results
    path('<int:questionID>/votes/', views.votes, name = 'votes'), # /polls/x/votes
    path('choices/<int:choiceID>/', views.choices, name = 'choices' ) #/polls/choices/x 
    ]