# Generated by Django 2.2.4 on 2019-08-06 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Category description', max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Description for subCategory', max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restdjango.Category')),
            ],
            options={
                'verbose_name_plural': 'SubCategories',
                'unique_together': {('category', 'description')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Product Description', max_length=100, unique=True)),
                ('created_date', models.DateTimeField()),
                ('selled', models.BooleanField(default=False)),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restdjango.SubCategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]