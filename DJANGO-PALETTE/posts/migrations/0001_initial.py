# Generated by Django 4.0.6 on 2022-08-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('01', 'gray'), ('02', 'blue'), ('03', 'green'), ('04', 'yellow'), ('05', 'orange'), ('06', 'red'), ('07', 'pink')], max_length=10)),
                ('writer', models.CharField(max_length=10, verbose_name='작성자')),
                ('color', models.CharField(max_length=7, verbose_name='본문색상')),
                ('title', models.CharField(max_length=20, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('pup_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
