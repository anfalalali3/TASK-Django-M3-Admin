# Generated by Django 4.0.4 on 2022-10-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('WA', 'Water'), ('GR', 'Grass'), ('GH', 'Ghost'), ('ST', 'Steel'), ('FA', 'Fairy')], default='GRASS', max_length=10)),
                ('hp', models.PositiveIntegerField()),
                ('active', models.BooleanField(default=True)),
                ('name_fr', models.CharField(max_length=30)),
                ('name_ar', models.CharField(max_length=30)),
                ('name_jp', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
