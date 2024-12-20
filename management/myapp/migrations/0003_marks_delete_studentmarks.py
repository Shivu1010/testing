# Generated by Django 5.1.2 on 2024-11-07 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_studentmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20)),
                ('subject1', models.IntegerField()),
                ('subject2', models.IntegerField()),
                ('subject3', models.IntegerField()),
                ('subject4', models.IntegerField()),
                ('subject5', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='StudentMarks',
        ),
    ]
