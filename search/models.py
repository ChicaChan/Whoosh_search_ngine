from django.db import models
from django.utils import timezone

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class SearchHistory(models.Model):
    query = models.CharField(max_length=200)
    search_time = models.DateTimeField(default=timezone.now)
    results_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-search_time']
        verbose_name_plural = "Search Histories"
    
    def __str__(self):
        return f"{self.query} ({self.search_time})" 