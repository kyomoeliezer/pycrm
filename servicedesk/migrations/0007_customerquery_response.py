# Generated by Django 4.2 on 2024-09-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicedesk', '0006_alter_customerquery_escalatedto'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerquery',
            name='response',
            field=models.TextField(blank=True, null=True, verbose_name='Response'),
        ),
    ]
