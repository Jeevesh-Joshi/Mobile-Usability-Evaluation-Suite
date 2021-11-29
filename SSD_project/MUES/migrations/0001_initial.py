# Generated by Django 3.2.9 on 2021-11-28 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pp', to='MUES.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=6)),
                ('problems', models.TextField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MUES.projects')),
                ('tasks', models.ManyToManyField(to='MUES.Tasks')),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=500)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MUES.tasks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MUES.users')),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='tasks',
            field=models.ManyToManyField(to='MUES.Tasks'),
        ),
    ]
