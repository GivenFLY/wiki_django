from django.db import models


class Article(models.Model):
    current_version = models.OneToOneField("ArticleVersion", blank=True, null=True, on_delete=models.CASCADE)

    def add_version(self, version):
        if not self.id:
            self.save()

        versions = self.articleversion_set.all()

        try:
            version.number = versions.latest().number + 1
        except ArticleVersion.DoesNotExist:
            version.number = 1

        version.article_obj = self
        version.save()
        self.current_version = version
        self.save()

    def __str__(self):
        if not self.current_version: return "Empty Article"
        else: return f"Article {self.id} (ver: {self.current_version.number}): {self.current_version.title!r}"


class ArticleVersion(models.Model):
    article_obj = models.ForeignKey("Article", on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=False, blank=False)
    text = models.TextField()
    number = models.IntegerField(editable=False)

    def __str__(self):
        return f"Article {self.article_obj.id} (ver: {self.number})"

    class Meta:
        get_latest_by = "number"






