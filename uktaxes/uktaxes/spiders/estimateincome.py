import re
import scrapy
from scrapy import Spider
from scrapy.http import FormRequest

class EstimateincomeSpider(scrapy.Spider):
    name = "estimateincome"

    allowed_domains = ["www.tax.service.gov.uk"]
    start_urls = ["https://www.tax.service.gov.uk/estimate-paye-take-home-pay"]

    def start_requests(self):
        set_income_details_url = 'https://www.tax.service.gov.uk/estimate-paye-take-home-pay/your-pay'
        yield scrapy.Request(set_income_details_url, callback=self.set_income_details)

    def set_income_details(self, response):
        salary = '40000'
        paidPeriod = 'a year'

        token = response.css("form input[name=csrfToken]::attr(value)").extract_first()
        yield FormRequest.from_response(response,
                                        formdata={
                                            'csrf_token': token,
                                            'amount': salary,
                                            'period': paidPeriod
                                        },
                                        callback=self.set_state_pension_details)

    def set_state_pension_details(self, response):
        state_pension_url = 'https://www.tax.service.gov.uk/estimate-paye-take-home-pay/state-pension'
        overStatePensionAge = 'false'

        token = response.css("form input[name=csrfToken]::attr(value)").extract_first()
        yield FormRequest.from_response(response,
                                        formdata={
                                            'csrf_token': token,
                                            'overStatePensionAge': overStatePensionAge,
                                        },
                                        callback=self.set_tax_code_details)

    def set_tax_code_details(self, response):
        tax_code_url = 'https://www.tax.service.gov.uk/estimate-paye-take-home-pay/tax-code'

        token = response.css("form input[name=csrfToken]::attr(value)").extract_first()
        yield FormRequest.from_response(response,
                                        formdata={
                                            'csrf_token': token,
                                            'taxCode': '1257L',
                                        },
                                        callback=self.set_scottish_tax_details)

    def set_scottish_tax_details(self, response):
        scottish_tax_url = 'https://www.tax.service.gov.uk/estimate-paye-take-home-pay/scottish-tax'
        payScottishRate = 'false'

        token = response.css("form input[name=csrfToken]::attr(value)").extract_first()
        yield FormRequest.from_response(response,
                                        formdata={
                                            'csrf_token': token,
                                            'payScottishRate': payScottishRate,
                                        },
                                        callback=self.start_scraping)

    def check_your_answers(self, response):
        tax_answer_url = 'https://www.tax.service.gov.uk/estimate-paye-take-home-pay/your-answers'

        token = response.css("form input[name=csrfToken]::attr(value)").extract_first()
        yield FormRequest.from_response(response,
                                        formdata={
                                            'csrf_token': token,
                                        },
                                        callback=self.start_scraping)

    def start_scraping(self, response):
        tax_income_details_url = 'https://www.tax.service.gov.uk/estimate-paye-take-home-pay/your-results?csrfToken=b1dee9f85acdd7f9e1d1618a475b1e4578d3b1a4-1683988609201-6214d5d260e81da646b0d80d&csrf_token=b1dee9f85acdd7f9e1d1618a475b1e4578d3b1a4-1683988609201-6214d5d260e81da646b0d80d&payScottishRate=false'

        tabsHtml = response.css('ul.govuk-tabs__list li a.govuk-tabs__tab::text').extract()
        tabs = re.findall(r'\b(Yearly|Monthly|Weekly)\b',''.join(tabsHtml))

        for tab in tabs:
            parentDiv = response.css('div.govuk-tabs__panel#' + tab.upper())
            details = parentDiv.css('dl.govuk-summary-list')

            yield {
                tab: {
                    'TabTitle': parentDiv.css('div.govuk-panel__body::text').get().replace('\n        ', '') + parentDiv.css('div.govuk-panel__body strong::text').get(),
                    parentDiv.css('h2.govuk-heading-l:nth-child(2)::text').get(): {
                        details[0].css('div.govuk-summary-list__row:nth-child(1) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
                            details[0].css('div.govuk-summary-list__row:nth-child(1) dd.govuk-summary-list__value::text').get().replace('\n        ', '').replace('\n      ', ''),
                        details[0].css('div.govuk-summary-list__row:nth-child(2) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
                            details[0].css('div.govuk-summary-list__row:nth-child(2) dd.govuk-summary-list__value::text').get().replace('\n        ', '').replace('\n      ', ''),
                        details[0].css('div.govuk-summary-list__row:nth-child(3) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
                            details[0].css('div.govuk-summary-list__row:nth-child(3) dd.govuk-summary-list__value strong::text').get().replace('\n        ', '').replace('\n      ', ''),
                    },
                    parentDiv.css('h2.govuk-heading-l:nth-child(4)::text').get(): {
                        details[1].css('div.govuk-summary-list__row:nth-child(1) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
                            details[1].css('div.govuk-summary-list__row:nth-child(1) dd.govuk-summary-list__value::text').get().replace('\n        ', '').replace('\n      ', ''),
                        details[1].css('div.govuk-summary-list__row:nth-child(2) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
                            details[1].css('div.govuk-summary-list__row:nth-child(2) dd.govuk-summary-list__value::text').get().replace('\n        ', '').replace('\n      ', ''),
                        details[1].css('div.govuk-summary-list__row:nth-child(3) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
                            details[1].css('div.govuk-summary-list__row:nth-child(3) dd.govuk-summary-list__value strong::text').get().replace('\n        ', '').replace('\n      ', ''),
                    }
                }
            }
