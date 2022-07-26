# Generated by Django 4.0.6 on 2022-07-24 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('category', models.CharField(blank=True, choices=[('Fashion', 'Fashion'), ('Mobiles and Tablets', 'Mobiles and Tablets'), ('Consumer Electronics', 'Consumer Electronics'), ('Books', 'Books'), ('movie_tickets', 'Movie Tickets'), ('baby_products', 'Baby Products'), ('Groceries', 'Groceries')], max_length=95)),
                ('tags', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('description', models.TextField(blank=True, default='', max_length=900, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='post-images')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('product_comment', models.CharField(blank=True, max_length=400, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]