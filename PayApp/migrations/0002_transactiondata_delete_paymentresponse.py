# Generated by Django 5.0.7 on 2024-07-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.CharField(max_length=100)),
                ('merchant_transaction_id', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('response_code', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pg_transaction_id', models.CharField(max_length=100)),
                ('pg_service_transaction_id', models.CharField(max_length=100)),
                ('bank_transaction_id', models.CharField(max_length=100)),
                ('bank_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='PaymentResponse',
        ),
    ]
