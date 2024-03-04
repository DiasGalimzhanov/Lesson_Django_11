from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'