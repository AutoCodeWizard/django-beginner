from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(),
        ),
    ]
