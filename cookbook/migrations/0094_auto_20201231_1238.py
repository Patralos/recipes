# Generated by Django 3.1.4 on 2020-12-31 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0093_auto_20201231_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppinglistrecipe',
            old_name='multiplier',
            new_name='servings',
        ),
    ]
