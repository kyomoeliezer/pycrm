# Generated by Django 4.2 on 2024-09-07 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('ticketNo', models.CharField(max_length=300, unique=True, verbose_name='TicketNo')),
                ('orderno', models.IntegerField(unique=True, verbose_name='OrderNo')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Attended', 'Attended'), ('Escalated', 'Escalated'), ('Closed', 'Closed')], max_length=300, verbose_name='TicketStatus')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='useragentservice', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='catgory', to='core.category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('escalatedto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='escalationuser', to=settings.AUTH_USER_MODEL)),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userauth', to='core.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatusTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Attended', 'Attended'), ('Escalated', 'Escalated'), ('Closed', 'Closed')], max_length=300, verbose_name='TicketStatus')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usertracker', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customerquery', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='query', to='servicedesk.customerquery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=400, verbose_name='Full Name')),
                ('mobile', models.CharField(max_length=300, verbose_name='Main Mobile')),
                ('mobile2', models.CharField(blank=True, max_length=300, null=True, verbose_name='Mobile 2')),
                ('mobile3', models.CharField(blank=True, max_length=300, null=True, verbose_name='Mobile 3')),
                ('institution', models.CharField(blank=True, max_length=300, null=True, verbose_name='Institution')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='locationdata', to='core.location')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
