from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.contrib.sitemaps import ping_google
from PIL import Image

RELEASE_TYPE = (
    # In-system value - Show value
    ('pre-release', 'Pre-release'),
    ('stable', 'Stable')
)


class Changelog(models.Model):
    version = models.CharField(default='', max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    type = models.TextField(choices=RELEASE_TYPE, default='stable')
    note = MDTextField()

    def __str__(self):
        return f'{self.version} changelog ({self.type})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass


class Ruleset(models.Model):
    creator = models.CharField(default="0", max_length=10)
    owner = models.CharField(default="0", max_length=10)

    name = models.CharField(default="", max_length=20)
    slug = models.SlugField(default="", max_length=20)
    description = models.CharField(default="", max_length=150)
    icon = models.ImageField(default='default_icon.png', upload_to='rulesets_icon', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    logo = models.ImageField(default='default_logo.jpeg', upload_to='rulesets_logo', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    cover_image = models.ImageField(default='default_wiki_cover.jpeg', upload_to='wiki_cover', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    opengraph_image = models.ImageField(default='default_wiki_cover.jpeg', upload_to='rulesets_opengraph_image', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    recommend_beatmap_cover = models.ImageField(default='default_recommend_beatmap_cover.png', upload_to='recommend_beatmap_cover', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])

    content = MDTextField()

    source = models.URLField(default="")

    last_edited_by = models.CharField(default="0", max_length=10)
    last_edited_at = models.DateTimeField(auto_now=True, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass
        # Use pillow to resize profile image and cover image
        img = Image.open(self.cover_image.path)
        if img.height > 1080 or img.width > 1920:
            img.thumbnail((1920, 1080))
            img.save(self.cover_image.path)
        opengraph = Image.open(self.opengraph_image.path)
        if opengraph.height > 1080 or opengraph.width > 1920:
            opengraph.thumbnail((1920, 1080))
            opengraph.save(self.opengraph_image.path)
        recommend_beatmap = Image.open(self.recommend_beatmap_cover.path)
        if recommend_beatmap.height > 1080 or recommend_beatmap.width > 1920:
            recommend_beatmap.thumbnail((1920, 1080))
            recommend_beatmap.save(self.recommend_beatmap_cover.path)


class Subpage(models.Model):
    ruleset_id = models.CharField(default="0", max_length=10)

    title = models.CharField(default="", max_length=50)
    slug = models.SlugField(default="", max_length=50)

    content = MDTextField()

    creator = models.CharField(default="0", max_length=10)
    last_edited_by = models.CharField(default="0", max_length=10)
    last_edited_at = models.DateTimeField(auto_now=True, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} (Subpage of {Ruleset.objects.get(id=int(self.ruleset_id)).name})'


class RecommendBeatmap(models.Model):
    ruleset_id = models.CharField(default="0", max_length=10)
    user_id = models.CharField(default="0", max_length=10)

    beatmap_id = models.IntegerField(default=75)
    beatmapset_id = models.IntegerField(default=1)

    title = models.CharField(default="DISCO PRINCE", max_length=100)
    artist = models.CharField(default="Kenji Ninuma", max_length=100)
    source = models.CharField(default="", max_length=100)
    creator = models.CharField(default="peppy", max_length=100)
    approved = models.CharField(default="1", max_length=10)
    difficultyrating = models.FloatField(default="2.39774")
    bpm = models.CharField(default="119.999", max_length=10)
    version = models.CharField(default="Normal", max_length=50)

    url = models.URLField(default="https://osu.ppy.sh/beatmapsets/1#osu/75")

    beatmap_cover = models.ImageField(default='default_beatmap_cover.jpeg', upload_to='beatmap_cover', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    beatmap_thumbnail = models.ImageField(default='default_beatmap_thumbnail.jpeg', upload_to='beatmap_thumbnail', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])

    comment = models.CharField(default=None, max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} [{self.version}] (Recommend of {Ruleset.objects.get(id=int(self.ruleset_id)).name})'


class CustomWiki(models.Model):
    title = models.CharField(default="", max_length=100)

    time = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True, editable=True)

    creator = models.CharField(default="0", max_length=10)
    last_edited_by = models.CharField(default="0", max_length=10)

    content = MDTextField()

    def __str__(self):
        return f'{self.version} changelog ({self.type})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass