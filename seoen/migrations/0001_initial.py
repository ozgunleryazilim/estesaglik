# Generated by Django 2.2 on 2021-10-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordsEn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100, verbose_name='Anahtar Kelime')),
            ],
            options={
                'verbose_name': 'EN Anahtar Kelime',
                'verbose_name_plural': 'EN Anahtar Kelimeler',
            },
        ),
        migrations.CreateModel(
            name='HomeSeoEn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Başlığı:')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Açıklaması:')),
                ('cover_image', models.ImageField(upload_to='cover', verbose_name='Kapak Görseli:')),
                ('meta_keywords', models.ManyToManyField(to='seoen.KeywordsEn', verbose_name='Anahtar Kelimeler')),
            ],
            options={
                'verbose_name': 'EN Landing Page',
                'verbose_name_plural': 'EN Landing Page',
            },
        ),
    ]
