from suds.client import Client

url = 'http://10.242.2.188/dn/Subscription/SubscriptionOrder.svc?WSDL'
url2 = 'http://10.242.2.188/dn/Customer/CustomerReservationService.svc?WSDL'
url3 = 'http://10.242.2.188/dn2/InfoWebXMLWebService.asmx?WSDL'
headers = {'content-type': 'text/xml; charset=utf-8'}
country_code = 'NO'
house_no = 33
street = 'NONNEGATA'
zip_code = '0656'
email = 'thomeeeh@dispostable.com'
first_name = 'Jane'
last_name = 'Parker'
telephone = '93256148'
dob = '1975-05-29T00:00:00.000+06:00'
order_flow = 'true'
campaign = 'WEBSALG'
ma_code = 'S_GOOGLE'
num_copies = 1
product_code = 'K6O'
start_date = '2022-02-22T00:00:00.000+06:00'
term_code = '12'
title_code = 'DN'

address_parameters = {'CountryCode': country_code,
                      'HouseNumber': house_no,
                      'Streetname': street,
                      'ZipCode': zip_code}
customer_parameters = {'EmailAddress': email,
                       'Firstname': first_name,
                       'Lastname': last_name,
                       'MobileTelephoneNumber': telephone,
                       'DateOfBirth': dob}
sale_parameters = {'CampaignCode': campaign,
                   'MarketingActivityCode': ma_code}
subscription_parameters = {'NumberOfCopies': num_copies,
                           'ProductCode': product_code,
                           'StartDate': start_date,
                           'TermCode': term_code,
                           'TitleCode': title_code}
customer_number = 1118500
dynamicattribute = 372
da_value = 'RED'
client = Client(url3)
# Lists available services
# print(client)

result = client.service.SetCustomerDynamicAttribute(
    customerNumber=customer_number,
    dynamicAttributeId=dynamicattribute,
    value=da_value
)

# result = client.service.OrderSubscription(
#     AddressParameters=address_parameters,
#     CustomerParameters=customer_parameters,
#     ParticipateInOnlinePaymentFlow=False,
#     SalesParameters=sale_parameters,
#     SubscriptionParameters=subscription_parameters)

result2 = client.service.GetCustomerDynamicAttributes(customerNumber=customer_number)
print(result)
print(result2)
