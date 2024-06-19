from rest_framework import viewsets, permissions
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import TaskItem, TaskRecord
from .serializers import TaskItemSerializer, TaskRecordSerializer


class TaskItemViewSet(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer


class TaskRecordViewSet(viewsets.ModelViewSet):
    queryset = TaskRecord.objects.all()
    serializer_class = TaskRecordSerializer

    def get_queryset(self):
        return TaskRecord.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SummaryViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def daily(self, request):
        date_str = request.query_params.get('date', datetime.now().strftime('%Y-%m-%d'))
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        records = TaskRecord.objects.filter(user=request.user, date_completed=date)
        total_time = sum(record.time_spent for record in records)
        priorities = {
            'low': records.filter(task__priority='low').count(),
            'medium': records.filter(task__priority='medium').count(),
            'high': records.filter(task__priority='high').count(),
        }
        summary = {
            'total_tasks': records.count(),
            'total_time_spent': total_time,
            'priorities': priorities,
        }

        return Response(summary)
