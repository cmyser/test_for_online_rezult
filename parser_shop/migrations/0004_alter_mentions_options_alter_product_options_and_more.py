# Generated by Django 4.0.2 on 2022-02-23 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_shop', '0003_alter_mentions_mention_text_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mentions',
            options={'verbose_name': 'мнение', 'verbose_name_plural': 'мнения'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='product_info',
            options={'verbose_name': 'Информация о продукте', 'verbose_name_plural': 'Информация о продуктах'},
        ),
    ]
