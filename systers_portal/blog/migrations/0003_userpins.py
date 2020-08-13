# Generated by Django 3.0.9 on 2020-08-10 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('blog', '0002_auto_20200724_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pins', models.ManyToManyField(blank=True, related_name='pins', to='blog.Resource', verbose_name='pins')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.SystersUser')),
            ],
        ),
    ]