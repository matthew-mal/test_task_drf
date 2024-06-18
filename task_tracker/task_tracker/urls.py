from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import SummaryViewSet, TaskItemViewSet, TaskRecordViewSet


router = DefaultRouter()
router.register(r'task', TaskItemViewSet)
router.register(r'task_record', TaskRecordViewSet)
router.register(r'summary', SummaryViewSet, basename='summary')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
