# Generated by Django 3.1 on 2020-09-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapi', '0003_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=60)),
                ('score', models.CharField(max_length=60)),
            ],
        ),
    ]
