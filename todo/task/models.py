from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    task_name = models.CharField(max_length=50, verbose_name='Task Name', help_text='Enter the task name.')
    task_description = models.TextField(max_length=500, verbose_name='Description', help_text='Provide a task description.')
    task_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING)
    task_created = models.DateField(default=date.today, verbose_name='Created Date')
    task_completed = models.DateField(null=True, blank=True, verbose_name='Completed Date')

    # def clean(self):
    #     if self.task_completed and self.task_completed < self.task_created:
    #         raise ValidationError("Completion date cannot be earlier than creation date.")

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-task_created']
