from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("sort_order", "name")
        verbose_name_plural = "Blog categories"

    def __str__(self) -> str:
        return self.name


class BlogPost(models.Model):
    category = models.ForeignKey(
        BlogCategory, related_name="posts", on_delete=models.PROTECT
    )
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    excerpt = models.CharField(max_length=400, blank=True)
    body = models.TextField()
    cover_image_path = models.CharField(max_length=500, blank=True)
    author_display_name = models.CharField(max_length=120, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-published_at", "-id")

    def __str__(self) -> str:
        return self.title

    @property
    def approved_comment_count(self) -> int:
        return self.comments.filter(is_approved=True).count()


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.post.slug} / {self.name}"
