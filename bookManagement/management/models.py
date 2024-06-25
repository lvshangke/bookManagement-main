from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=128, verbose_name='书籍名称')
    author = models.CharField(max_length=64, verbose_name='作者')
    price = models.FloatField(default=.0, verbose_name='定价')
    publish_date = models.DateField(null=True, blank=True, verbose_name='出版日期')
    category = models.CharField(max_length=32, default='未分类', verbose_name='书籍分类')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=128, verbose_name='图片名称')
    description = models.TextField(default='', verbose_name='图片描述')
    img = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='图片')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='所属书籍')

    def __str__(self):
        return self.name

# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='书籍')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
#     review_text = models.TextField(verbose_name='评论内容')
#     review_date = models.DateTimeField(auto_now_add=True, verbose_name='评论日期')
#
#     def __str__(self):
#         return f"{self.user.username} - {self.book.name}"
#
# class Score(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='书籍')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
#     score_value = models.PositiveSmallIntegerField(verbose_name='评分值', choices=[(i, i) for i in range(1, 6)])
#     score_date = models.DateTimeField(auto_now_add=True, verbose_name='评分日期')
#
#     def __str__(self):
#         return f"{self.user.username} - {self.book.name} ({self.score_value})"


class Intro(models.Model):
    introduction = models.TextField(default='', verbose_name='书籍简介')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='所属书籍')
    #created_at = models.DateTimeField(auto_now_add=True)  # 时间戳字段

    def __str__(self):
        return f"{self.book.name} - Intro"

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联到用户
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(
        choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.book.name}'

    def get_rating_range(self):
        return range(self.rating)