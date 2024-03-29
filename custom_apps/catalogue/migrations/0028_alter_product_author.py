# Generated by Django 3.2.18 on 2023-05-08 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20230430_0203'),
        ('catalogue', '0027_auto_20230430_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='authors.painter', verbose_name='Автор'),
        ),
    ]
