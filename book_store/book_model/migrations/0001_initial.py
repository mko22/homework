# Generated by Django 3.0.4 on 2020-03-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('publishing_length', models.IntegerField()),
                ('author_name', models.CharField(max_length=20)),
                ('book_genre', models.CharField(max_length=20)),
            ],
        ),
    ]
