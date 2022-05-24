def run_step():
    url = 'http://10.242.2.188/dn/InfoWebXMLWebService.asmx?WSDL'
    dynamicattribute_id = 372
    esp = EngagementScorePrepper()
    esp.update_engagement_score(url=url, dynamicattribute_id=dynamicattribute_id)


if __name__ == '__main__':
    run_step()



    # Update Infosoft via webservices
    def set_engagement_score_ws(self, engagement_score, url, dynamicattribute_id):
        self.logger.info(f'Updating Infosoft. {len(engagement_score)} customers to update.')
        for i, row in engagement_score.iterrows():
            client = Client(url)
            result = client.service.SetCustomerDynamicAttribute(
                customerNumber=engagement_score.iloc[i]['customer_number'],
                dynamicAttributeId=dynamicattribute_id,
                value=engagement_score.iloc[i]['level_eng_score']
            )
            if result is None:
                self.logger.error(f'Update failed for customer {engagement_score.iloc[i]["customer_number"]}. '
                                  f'Response from web service is empty.')
            elif result.StatusCode == '00':
                self.logger.debug(f'Customer {engagement_score.iloc[i]["customer_number"]} updated')
            else:
                self.logger.error(f'Update failed for customer {engagement_score.iloc[i]["customer_number"]}. '
                                  f'Status code: {result.StatusCode}')