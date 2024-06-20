# Generated by Django 4.2.9 on 2024-05-13 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chained', '0005_chainedtemplate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chainedtemplate',
            name='templated_chain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chained_templates', to='chained.templatedchain'),
        ),
    ]