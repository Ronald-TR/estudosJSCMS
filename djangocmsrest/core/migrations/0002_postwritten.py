# Generated by Django 2.0 on 2018-02-25 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostWritten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textdata', models.CharField(max_length=1000)),
                ('postdata', models.DateTimeField(auto_now_add=True)),
                ('writter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Writer')),
            ],
        ),
    ]
