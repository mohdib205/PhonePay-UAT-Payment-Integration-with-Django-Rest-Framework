# Generated by Django 5.0.7 on 2024-07-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayApp', '0003_alter_transactiondata_bank_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField()),
                ('code', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=255)),
                ('merchantId', models.CharField(max_length=100)),
                ('merchantTransactionId', models.CharField(max_length=100)),
                ('transactionId', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
                ('responseCode', models.CharField(max_length=100)),
                ('paymentInstrumentType', models.CharField(max_length=100)),
                ('utr', models.CharField(max_length=100)),
                ('upiTransactionId', models.CharField(max_length=100)),
                ('accountHolderName', models.CharField(max_length=100)),
                ('cardNetwork', models.CharField(blank=True, max_length=100, null=True)),
                ('accountType', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='TransactionData',
        ),
    ]
