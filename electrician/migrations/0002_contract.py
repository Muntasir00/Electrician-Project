# Generated by Django 4.0.4 on 2022-06-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electrician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
