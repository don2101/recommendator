from django.db import models

# Create your models here.
class Question(models.Model) :
    title = models.CharField(max_length=100)
    
    def __repr__(self) :
        return f"<{self.title}>"
    
    def __str__(self) :
        return f"<{self.title}>"
    
    
class Choice(models.Model) :
    content = models.CharField(max_length=100)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    
    def __repr__(self) :
        return f"<{self.content}, {self.votes}>"
    
    def __str__(self) :
        return f"<{self.content}, {self.votes}>"