from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal', '0003_expresscheckouttransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expresscheckouttransaction',
            name='status',
            field=models.CharField(max_length=255),
        ),
    ]