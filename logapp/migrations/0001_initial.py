# Generated by Django 4.1.2 on 2022-10-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(choices=[('0', 'Patient'), ('1', 'Doctor')], max_length=50)),
                ('mobile_number', models.CharField(max_length=10, unique=True, verbose_name='phone number')),
                ('gender', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(upload_to='images/')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='user address')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('state', models.CharField(max_length=100, verbose_name='state')),
                ('postal_code', models.IntegerField(verbose_name='postal_code')),
            ],
        ),
    ]