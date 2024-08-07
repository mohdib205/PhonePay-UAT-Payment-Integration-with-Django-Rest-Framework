# Generated by Django 5.0.7 on 2024-07-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayApp', '0004_paymentresponse_delete_transactiondata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentresponse',
            name='accountHolderName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentresponse',
            name='accountType',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentresponse',
            name='paymentInstrumentType',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentresponse',
            name='upiTransactionId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymentresponse',
            name='utr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
