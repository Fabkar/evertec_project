# Generated by Django 3.2 on 2021-04-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costumer_name', models.CharField(max_length=80)),
                ('costumer_email', models.EmailField(max_length=120)),
                ('costumer_mobile', models.IntegerField()),
                ('status', models.CharField(choices=[('CRT', 'CREATED'), ('PD', 'PAYED'), ('RD', 'REJECTED')], default='CRT', max_length=3)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
