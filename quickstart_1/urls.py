from django.urls import path
from . import views

app_name='quickstart_1'

urlpatterns = [
    path('userview/',views.UserSerailazerView.as_view(),name='userview'),
    path('userview_1/',views.UserSerializerView_1.as_view(),name='userview_1'),
    path('companyview/',views.CompanySerializerView.as_view(),name='companyview'),
    path('highscore/',views.highscore_view,name='highscore'),
    path('hignscore1/<int:pk>/',views.highscore_view_1,name='hignscore1'),
    path('highrepresent/',views.highscore_represent,name='highrepresent'),
    path('highscorview/',views.HighScoreSerializerView.as_view(),name='highscorview'),
    path('hospitalview/',views.HospitalSerializerView.as_view(),name='hospitalview'),
    path('hospital_1/',views.hospital_1,name='hospital_1'),
    path('patient1/',views.patient_1,name='patient1')
]
