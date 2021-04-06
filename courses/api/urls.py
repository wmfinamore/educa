from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)
app_name = 'courses'
urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/',
         views.SubjectDetailView.as_view(), name='subjects_detail'),
    path('',
         include(router.urls)),
]
