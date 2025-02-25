# Generated by Django 3.2 on 2023-06-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_janmform'),
    ]

    operations = [
        migrations.CreateModel(
            name='AadhaarForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar_number', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('photo', models.ImageField(null=True, upload_to='photo')),
                ('gender', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.CharField(max_length=100, null=True)),
                ('relation', models.CharField(max_length=100, null=True)),
                ('father_husband_name', models.CharField(max_length=100, null=True)),
                ('house_number', models.CharField(max_length=100, null=True)),
                ('street', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pin_code', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('local_language', models.CharField(max_length=100, null=True)),
                ('local_name', models.CharField(max_length=100, null=True)),
                ('local_address', models.CharField(max_length=100, null=True)),
                ('enrollment_number', models.CharField(max_length=100, null=True)),
                ('issue_date', models.CharField(max_length=100, null=True)),
                ('download_date', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
