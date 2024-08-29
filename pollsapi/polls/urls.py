from rest_framework.routers import DefaultRouter
from django.urls import include, path, re_path
from .views import polls_list, polls_details
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate, Loginview

router = DefaultRouter()
router.register('polls', PollList, basename='polls')


urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name='choice_list'),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name='create_vote'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', Loginview.as_view(), name='login'),

]

urlpatterns += router.urls
