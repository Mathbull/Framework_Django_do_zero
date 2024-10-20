# Generated by Django 5.1.2 on 2024-10-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='Pergunta')),
                ('pub_date', models.DateField(verbose_name='Data de publicação')),
            ],
        ),
    ]
