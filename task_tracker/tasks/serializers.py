from rest_framework import serializers
from .models import TaskItem, TaskRecord


class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = [
            'id',
            'title',
            'description',
            'priority',
            'due_date'
        ]


class TaskRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRecord
        fields = [
            'id',
            'user',
            'task',
            'date_completed',
            'time_spent'
        ]
