# Generated by Django 3.2.6 on 2021-09-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b2project', '0016_contract_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4000)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]