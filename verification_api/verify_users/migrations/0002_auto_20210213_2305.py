# Generated by Django 3.1.4 on 2021-02-13 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('verify_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driving_License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dl_no', models.CharField(max_length=50)),
                ('date_of_issue', models.DateField()),
                ('date_of_expiry', models.DateField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PanCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pancard_no', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='passport',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='passport',
            name='date_of_expiry',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='passport',
            name='date_of_issue',
            field=models.DateField(),
        ),
    ]
