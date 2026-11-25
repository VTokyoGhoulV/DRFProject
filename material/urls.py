from django.urls import path
from rest_framework import routers

from material.views import CourseViewSet, LessonCreateView, LessonListView, LessonDetailView, LessonDeleteView, \
    LessonUpdateView

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [
    path("lesson/create/", LessonCreateView.as_view(), name="lesson-create"),
    path("lessons/", LessonListView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonDetailView.as_view(), name="lesson-detail"),
    path("lesson/<int:pk>/delete/", LessonDeleteView.as_view(), name="lesson-delete"),
    path("lesson/<int:pk>/update/", LessonUpdateView.as_view(), name="lesson-update"),
              ] + router.urls