# Generated by Django 5.1 on 2025-05-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('idade', models.CharField(max_length=100)),
                ('profissao', models.CharField(max_length=100)),
            ],
        ),
    ]
