# Generated by Django 4.2.2 on 2023-06-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(default=9898989890, max_length=10)),
                ('position', models.CharField(default='xyd', max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
            ],
        ),
    ]
