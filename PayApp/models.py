from django.db import models

# Create your models here.
from django.db import models

# class TransactionData(models.Model):
class PaymentResponse(models.Model):
    success = models.BooleanField()
    code = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    merchantId = models.CharField(max_length=100)
    merchantTransactionId = models.CharField(max_length=100)
    transactionId = models.CharField(max_length=100)
    amount = models.IntegerField()
    state = models.CharField(max_length=100)
    responseCode = models.CharField(max_length=100)
    paymentInstrumentType = models.CharField(max_length=100, null=True, blank=True)
    utr = models.CharField(max_length=100 , null=True, blank=True)
    upiTransactionId = models.CharField(max_length=100 , null=True, blank=True)
    accountHolderName = models.CharField(max_length=100 , null=True, blank=True)
    cardNetwork = models.CharField(max_length=100, null=True, blank=True)
    accountType = models.CharField(max_length=100 , null=True, blank=True)



