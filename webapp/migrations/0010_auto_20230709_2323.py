# Generated by Django 3.2 on 2023-07-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20230629_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='aadhaar',
            name='qr',
            field=models.ImageField(null=True, upload_to='qr'),
        ),
        migrations.AlterField(
            model_name='aadhaar',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='janm',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=50),
        ),
    ]
