from suds.client import Client


def run_sub_step():
    url = 'http://10.242.2.188/dn/Subscription/SubscriptionChange.svc?wsdl'
    client = Client(url)
    print(url)
    result = client.service.GetPermanentChangesForSubscription(
        SubscriptionIdentifier={
            'CustomerNumber': 1118500,
            'TitleCode': 'DN'},
        StartDate='1978-08-06T00:00:00.000+06:00'
    )
    print(result)


def run_customer_step():
    url = 'http://10.242.2.188/dn/Customer/CustomerReservationService.svc?WSDL'
    client = Client(url)
    print(url)
    result = client.service.CreateCustomerReservation(
        CustomerReservation={'TitleCode': 'DN',
                             'ReservationCode': 'XSMSR'},
        CustomerNumber=1118500
    )
    print(result)


def get_subscription_elements():
    url = 'http://10.242.2.188/dn/InfoWebXMLWebService.asmx?WSDL'
    client = Client(url)
    result = client.service.GetSubscriptionElements(
        customerNumber=1118500,
        startDate='2022-07-07T00:00:00',
        endDate='2022-07-07T00:00:00'
    )
    print(result)


if __name__ == '__main__':
    get_subscription_elements()
