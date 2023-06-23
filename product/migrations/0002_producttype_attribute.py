# Generated by Django 4.2.2 on 2023-06-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="producttype",
            name="attribute",
            field=models.ManyToManyField(
                related_name="product_type_attr",
                through="product.ProductTypeAttribute",
                to="product.attribute",
            ),
        ),
    ]