# Generated by Django 2.0.7 on 2018-07-31 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20180731_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productanswer',
            options={'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='productquestion',
            options={'verbose_name_plural': 'Product_Questions'},
        ),
        migrations.RenameField(
            model_name='productanswer',
            old_name='question',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='productanswer',
            old_name='Status',
            new_name='status',
        ),
    ]
