# Generated by Django 3.2.25 on 2024-08-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('bio', models.TextField()),
                ('phone_number', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='technicians', to='Technicians_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('technician', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='technician_reviews', to='Technicians_app.technician')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='Technicians_app.user')),
            ],
        ),
    ]
