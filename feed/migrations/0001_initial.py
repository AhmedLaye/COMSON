# Generated by Django 4.1.7 on 2023-02-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
