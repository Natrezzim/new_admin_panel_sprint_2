# Generated by Django 3.2 on 2022-02-09 06:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='description')),
                ('creation_date', models.DateField(null=True, verbose_name='release date')),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='rating')),
                ('type', models.TextField(choices=[('movie', 'movie'), ('tv_show', 'tv_show')], default='movie', max_length=50, verbose_name='type')),
            ],
            options={
                'verbose_name': 'film work',
                'verbose_name_plural': 'film works',
                'db_table': 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.TextField(max_length=50, verbose_name='person name')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'person',
                'db_table': 'content"."person',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('role', models.TextField(choices=[('actor', 'actor'), ('writer', 'writer'), ('director', 'director')], default='actor', max_length=50, verbose_name='role')),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='film_work')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='person')),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['id', 'full_name'], name='person_idx'),
        ),
        migrations.AddField(
            model_name='genrefilmwork',
            name='film_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork', verbose_name='film_work'),
        ),
        migrations.AddField(
            model_name='genrefilmwork',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmWork', to='movies.Person'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=models.Index(fields=['film_work_id', 'person_id'], name='person_film_work_idx'),
        ),
        migrations.AddIndex(
            model_name='genrefilmwork',
            index=models.Index(fields=['film_work_id', 'genre_id'], name='genre_film_work_idx'),
        ),
        migrations.AddIndex(
            model_name='filmwork',
            index=models.Index(fields=['id', 'title', 'creation_date'], name='film_work_idx'),
        ),
    ]