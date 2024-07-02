# Generated by Django 4.2.9 on 2024-06-24 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tom_targets', '0020_alter_targetname_created_alter_targetname_modified'),
        ('sso_alerts', '0003_alertstreams_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=255)),
                ('target', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stream', to='tom_targets.target')),
            ],
        ),
    ]