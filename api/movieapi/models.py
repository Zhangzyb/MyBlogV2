from django.db import models

class Movie(models.Model):
    movieId = models.BigIntegerField('电影Id', primary_key=True)
    title = models.CharField('电影名', max_length=150)
    year = models.IntegerField('上映时间')
    directors = models.CharField('导演', max_length=100)
    casts = models.CharField('演员', max_length=500)
    region = models.CharField('地区', max_length=100)
    types = models.CharField('类型', max_length=50)
    duration = models.CharField('片长', max_length=30)
    rate = models.FloatField('评分')
    rating_num = models.IntegerField('评分人数')
    cover = models.CharField('图片链接', max_length=100)

    def __str__(self):
        return self.title + self.directors + self.casts

    class Meta:
        db_table = 'movie'
        verbose_name = '电影'
        verbose_name_plural = verbose_name


class DoubanComment(models.Model):
    movie = models.IntegerField(verbose_name='电影Id')
    username = models.CharField('用户名', max_length=100)
    avatar = models.CharField('用户头像', max_length=100)
    rate = models.IntegerField('用户评价', default=0)
    time = models.CharField('评价时间', max_length=100)
    content = models.TextField('评论内容', default='无')

    def __str__(self):
        return self.movie + self.username

    class Meta:
        db_table = 'movie_comment'
        verbose_name = '电影评论'
        verbose_name_plural = verbose_name
        constraints = [models.UniqueConstraint(
            fields=['username', 'movie', 'time'], name='unique_comment')]
