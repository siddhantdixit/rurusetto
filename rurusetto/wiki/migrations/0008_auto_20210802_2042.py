# Generated by Django 3.2.5 on 2021-08-02 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0007_alter_ruleset_last_edited_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruleset',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ruleset_page_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ruleset',
            name='last_edited_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ruleset_last_edited_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ruleset',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ruleset_ruleset_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]