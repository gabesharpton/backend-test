# Generated by Django 3.0.1 on 2019-12-27 04:55

from django.db import migrations, models

def create_data(apps,schema_editor):
    Task = apps.get_model('task', 'Task')

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=400)),
                ('task', models.CharField(max_length=400)),
                ('assigned', models.CharField(max_length=200)),
            ],
        ),
    ]
