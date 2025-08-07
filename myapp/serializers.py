# serializers.py
from datetime import datetime
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    is_due_over = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'is_completed',
            'due_date',
            'is_due_over',
        ]

    def get_is_due_over(self, obj):
        if obj.due_date:
            return obj.due_date > datetime.now(obj.due_date.tzinfo)
        return False
    
class TaskSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'due_date',
        ]
 