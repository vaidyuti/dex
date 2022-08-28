# Generated by Django 4.0.6 on 2022-08-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prosumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, editable=False, help_text='Whether the record is deleted or not (soft-delete)')),
                ('location', models.CharField(help_text='The coordinated of the prosumer', max_length=255, verbose_name='latitude_longitude')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]