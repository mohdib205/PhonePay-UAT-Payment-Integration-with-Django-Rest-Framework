from phonepe.sdk.pg.payments.v1.payment_client import PhonePePaymentClient
from phonepe.sdk.pg.env import Env
import uuid  
from phonepe.sdk.pg.payments.v1.models.request.pg_pay_request import PgPayRequest

from rest_framework.response import Response    
from rest_framework.decorators import api_view 
import base64
import json
from .models import * 
from .serializers import *





@api_view(["GET" , "POST"])
def phonepay(request):
    merchant_id = "PGTESTPAYUAT86"  
    salt_key = "96434309-7796-489d-8924-ab56988a6076"  
    salt_index = 1 
    env = Env.UAT
    should_publish_events = True

    phonepe_client = PhonePePaymentClient(merchant_id=merchant_id, salt_key=salt_key, salt_index=salt_index, env=env)
    unique_transaction_id = str(uuid.uuid4())[:-2]
    base_url = request.build_absolute_uri('/')[:-1]
    ui_redirect_url = f"{base_url}/redirect/?merchentTransactionId={unique_transaction_id}"
    s2s_callback_url = f"https://uqc5vu6s9yhv.share.zrok.io/redirect/callback/"
    print(ui_redirect_url , s2s_callback_url)
    amount = 1
    id_assigned_to_user_by_merchant = 'YOUR_USER_ID'  
    pay_page_request = PgPayRequest.pay_page_pay_request_builder(merchant_transaction_id=unique_transaction_id,  
                                                                amount=amount,  
                                                                merchant_user_id=id_assigned_to_user_by_merchant,  
                                                                callback_url=s2s_callback_url,
    redirect_url=ui_redirect_url, callback_mode="POST")  
    pay_page_response = phonepe_client.pay(pay_page_request)  
    pay_page_url = pay_page_response.data.instrument_response.redirect_info.url
    pay_page_response = phonepe_client.pay(pay_page_request) 
    pay_page_url = pay_page_response.data.instrument_response.redirect_info.url
    return Response({"url": pay_page_url})

@api_view(["GET" , "POST"])
def payment_callback(request):
    if request.method == 'POST':

        print(request.data)
        print("\n\n")
        print(request.headers)
        return Response("dattb")
    return Response("dattb")




@api_view(["POST"])
def callbackv(request):
    if request.method == 'POST':
        merchant_id = "PGTESTPAYUAT86"  
        salt_key = "96434309-7796-489d-8924-ab56988a6076"  
        salt_index = 1 
        env = Env.UAT
        client = PhonePePaymentClient(merchant_id=merchant_id, salt_key=salt_key, salt_index=salt_index, env=env)
        response=request.data["response"]
        x_var=request.headers["X-Verify"]
       
        response = {"response": f"{request.data['response']}"}
        response1=json.dumps(request.data)
        
        verify=client.verify_response(x_verify=x_var , response=response1)
        if verify:

            decoded_string = base64.b64decode(request.data["response"])
            decoded_data=decoded_string.decode("utf-8")
            print(type(decoded_data))
            data=json.loads(decoded_data)
            print(data)
            if data["success"]==True:

                all_data = {
                    'success': data['success'],
                    'code': data['code'],
                    'message': data['message'],
                    'merchantId': data['data']['merchantId'],
                    'merchantTransactionId': data['data']['merchantTransactionId'],
                    'transactionId': data['data']['transactionId'],
                    'amount': data['data']['amount'],
                    'state': data['data']['state'],
                    'responseCode': data['data']['responseCode'],
                    'paymentInstrumentType': data['data']['paymentInstrument']['type'],
                    'utr': data['data']['paymentInstrument']['utr'],
                    'upiTransactionId': data['data']['paymentInstrument']['upiTransactionId'],
                    'accountHolderName': data['data']['paymentInstrument']['accountHolderName'],
                    'cardNetwork': data['data']['paymentInstrument']['cardNetwork'],
                    'accountType': data['data']['paymentInstrument']['accountType']
                }
                
                print("aaaa" , dict(data).paymentInstrument)
                serializer = DataSerializer(data=all_data)
            else:
                all_data = {
                    'success': data['success'],
                    'code': data['code'],
                    'message': data['message'],
                    'merchantId': data['data']['merchantId'],
                    'merchantTransactionId': data['data']['merchantTransactionId'],
                    'transactionId': data['data']['transactionId'],
                    'amount': data['data']['amount'],
                    'state': data['data']['state'],
                    'responseCode': data['data']['responseCode']}
                print("Falsssee")
                serializer = DataSerializer(data=all_data)
            if serializer.is_valid():
                print("yess")
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({"response has changed"})
    # return Response("dattb")
    # if request.method == 'GET':
        

    #     unique_transaction_id = request.GET['merchentTransactionId']
    
    #     merchant_id = "PGTESTPAYUAT86"  
    #     salt_key = "96434309-7796-489d-8924-ab56988a6076"  
    #     salt_index = 1 
    #     env = Env.UAT
    #     client = PhonePePaymentClient(merchant_id=merchant_id, salt_key=salt_key, salt_index=salt_index, env=env)
    #     response = client.check_status(merchant_transaction_id=unique_transaction_id)
    #     data= response.data
    #     print(data)
    #     client.verify_response()
    #     # print(data.payment_instrument.pg_service_transaction_id , type(data.payment_instrument))
    #     TransactionData.objects.create(
    #     merchant_id=data.merchant_id,
    #     merchant_transaction_id=data.merchant_transaction_id,
    #     transaction_id=data.transaction_id,
    #     amount=data.amount,
    #     response_code=data.response_code,
    #     state=data.state)
        # pg_transaction_id=data.payment_instrument.pg_transaction_id,
        # pg_service_transaction_id=data.payment_instrument.pg_service_transaction_id,
        # bank_transaction_id=data.payment_instrument.bank_transaction_id,
        # bank_id=data.payment_instrument.bank_id)

        # for d in data:
        #     print(d)
    #     return Response({"message":"data has come from server"})
    # else:
    #     return Response('no data')
