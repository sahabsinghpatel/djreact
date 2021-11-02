# Generated by Django 3.2.8 on 2021-11-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Varify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=30)),
                ('otp', models.IntegerField(blank=True)),
            ],
        ),
    ]