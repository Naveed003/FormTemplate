# Generated by Django 4.1.7 on 2023-02-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emplid', models.IntegerField()),
                ('pwd', models.CharField(max_length=255)),
            ],
        ),
    ]
