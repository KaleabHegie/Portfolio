# Generated by Django 5.0.6 on 2024-06-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0004_alter_workexperience_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_type',
            field=models.CharField(blank=True, choices=[('React', 'react'), ('Django', 'django'), ('PHP', 'php'), ('Python', 'python'), ('JavaScript', 'javascript')], max_length=50, null=True),
        ),
    ]
