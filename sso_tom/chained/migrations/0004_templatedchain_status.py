# Generated by Django 4.2.9 on 2024-05-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chained', '0003_alter_templatedchain_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatedchain',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('FINALIZED', 'FINALIZED')], default='DRAFT', max_length=20),
        ),
    ]
