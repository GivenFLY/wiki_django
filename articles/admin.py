from django import forms
from django.contrib import admin

from .models import Article
from .models import ArticleVersion


class ArticleVersionForm(forms.ModelForm):
    class Meta:
        model = ArticleVersion
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ArticleVersionAdmin(admin.ModelAdmin):
    form = ArticleVersionForm

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=256)
    text = forms.CharField(widget=forms.Textarea({"cols": 80}))

    class Meta:
        model = Article
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            versions = ArticleVersion.objects.filter(article_obj=self.instance)
            self.fields["current_version"].queryset = versions

            self.fields["title"].initial = self.instance.current_version.title
            self.fields["text"].initial = self.instance.current_version.text

        else:
            self.fields["current_version"].queryset = ArticleVersion.objects.none()
            self.fields["current_version"].widget = forms.HiddenInput()


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

    def save_model(self, request, obj, form, change):
        av_id = request.POST.get("current_version")
        if not ArticleVersion.objects.filter(article_obj=obj):
            title = request.POST.get("title")
            text = request.POST.get("text")

            v = ArticleVersion(title=title, text=text)
            obj.add_version(v)

        else:
            if "current_version" in form.changed_data:
                if not av_id:
                    raise forms.ValidationError("You should select a valid version", code="invalid_version")

                v = ArticleVersion.objects.filter(id=av_id, article_obj=obj)[0]
                obj.current_version = v
                obj.save()

            elif "title" in form.changed_data or "text" in form.changed_data:
                title = request.POST.get("title")
                text = request.POST.get("text")
                v = ArticleVersion(title=title, text=text)
                obj.add_version(v)
        


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleVersion, ArticleVersionAdmin)