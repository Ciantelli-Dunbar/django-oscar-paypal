from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal', '0002_auto_20190412_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpressCheckoutTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255)),
                ('authorization_id', models.CharField(blank=True, max_length=255, null=True)),
                ('capture_id', models.CharField(blank=True, max_length=255, null=True)),
                ('refund_id', models.CharField(blank=True, max_length=255, null=True)),
                ('payer_id', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currency', models.CharField(blank=True, max_length=8, null=True)),
                ('status', models.CharField(max_length=8)),
                ('intent', models.CharField(max_length=9)),
                ('address_full_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]