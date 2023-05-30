# Generated by Django 4.1.3 on 2023-05-25 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "product_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("brand", models.CharField(blank=True, max_length=200, null=True)),
                ("category", models.CharField(blank=True, max_length=200, null=True)),
                ("reviews_num", models.IntegerField(blank=True, default=0, null=True)),
                ("rating", models.DecimalField(decimal_places=2, max_digits=7)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("stock", models.IntegerField(blank=True, default=0, null=True)),
                ("addedTime", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
