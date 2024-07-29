# Generated by Django 5.0.7 on 2024-07-28 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
