from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import strip_tags
from mdeditor.fields import MDTextField
import markdown


class Category(models.Model):
    name = models.CharField('分类', max_length=50)

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签', max_length=50)

    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=200)
    image = models.CharField('图片', max_length=500)
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')
    author = models.ForeignKey(
        User, verbose_name='作者', on_delete=models.CASCADE)
    abstract = models.CharField('摘要', max_length=1000)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    category = models.ForeignKey(
        Category, verbose_name='分类', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0, editable=False)
    likes = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)


class ArticleDetail(models.Model):
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, verbose_name='文章')
    text = MDTextField('正文')

    class Meta:
        db_table = 'article_detail'
        verbose_name = '文章详情'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.article.modified_time = timezone.now()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        self.article.abstract = strip_tags(md.convert(self.text))[:200]
        self.article.save()
        super().save(*args, **kwargs)


class Comment(models.Model):
    username = models.CharField('用户名', max_length=30)
    avatar = models.CharField('头像', max_length=100)
    email = models.EmailField('邮箱')
    text = models.TextField('评论内容')
    created_time = models.DateTimeField('评论时间', default=timezone.now)
    article = models.ForeignKey(
        'Article', verbose_name='所属文章', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父级评论')
    reply_name = models.CharField('回复名称', max_length=100, null=True)
    agree = models.IntegerField('赞成数', default=0)
    disagree = models.IntegerField('反对数', default=0)
    status = models.IntegerField('类别', default=0)
    images = models.CharField('动态图片', max_length=150,
                              null=True, blank=True, default=None)

    class Meta:
        ordering = ['-created_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        qq = self.email.split('@')[0]
        self.avatar = f'https://q.qlogo.cn/headimg_dl?dst_uin={qq}&spec=100'
        super().save(*args, **kwargs)
