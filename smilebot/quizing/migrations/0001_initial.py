# Generated by Django 4.2 on 2023-08-03 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='quiz_images/')),
                ('option_1', models.CharField(max_length=200)),
                ('option_2', models.CharField(max_length=200)),
                ('option_3', models.CharField(max_length=200)),
                ('option_4', models.CharField(max_length=200)),
                ('correct_ans', models.CharField(max_length=200)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quizing.quiz')),
            ],
        ),
    ]
