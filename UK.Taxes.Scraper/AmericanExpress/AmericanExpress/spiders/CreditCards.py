import re
import scrapy
from scrapy import Spider
from scrapy.http import FormRequest

class CreditcardsSpider(scrapy.Spider):
    name = "CreditCards"

    allowed_domains = ["www.americanexpress.com"]
    start_urls = ["https://www.americanexpress.com/en-gb/credit-cards/all-cards/"]

    def start_requests(self):
        set_credit_cards_url = 'https://www.americanexpress.com/en-gb/credit-cards/all-cards/'

        set_url = 'https://www.americanexpress.com/uk/credit-cards/all-cards/?inav=gb_menu_cards_pc_view_cm'
        set_url1 = 'https://www.americanexpress.com/en-gb/credit-cards/all-cards/?inav=gb_menu_cards_pc_view_cm'

        set = 'https://www.americanexpress.com/en-gb/credit-cards/platinum-cashback-everyday-credit-card/?linknav=en-gb-amex-cardshop-allcards-text-PlatCashBackEverydayCC-fc'
        yield scrapy.Request(set, callback=self.parse_personal_cards)

    def start_scraping(self, response):
        # Use XPath selector to find the link with the text "View Personal Cards" in the navbar
        link = response.xpath('//a[contains(., "Earn cashback on all your purchases, with no annual fee.")]/@href').get()

        if link:
            # Follow the link to the "View Personal Cards" page
            yield response.follow(link, self.parse_personal_cards)

    def parse_personal_cards(self, response):
        link = response.xpath('//span[contains(., "Earn cashback on all your purchases, with no annual fee.")]').get()

        print('Beniamin Test')
        print(link)
        print()
        # Using the above link will need further to click on the All Cards Tab from the navigation bar so we can see all the cards from that website
        # Find and click the desired navbar menu item
        #menu_item = self.driver.find_element(By.XPATH, '//your-menu-item-xpath')
        #menu_item.click()

        # click on the view personal cards then click on the All cards and then get all teh cards data...

        htmlData = response.css('div.body div:nth-child(2) div div div.sc_at_grid_container:first-child').extract()

        print();
        # print('Beniamin Jitca V150 Test');
        # t = response.css('.sc_at_grid_container')
        # for i in t:
        #     print(i.css('::text').get());
        # print('Beniamin Jitca V150 Test');

        #yield  { 'Data': response.css('body').extract() }

        # print(response.css('div.sc_horizontallyFluid div').extract())
        # print(response.css('p.sc_fontType_benton_light.sc_color_white.sc_textHeading_5.sc_textAlign_left').extract())

        # test = response.css('div p.sc_fontType_benton_regular').extract()
        # print(test)

        # for t in test:
        #     print(t.css('::text').get())

        #print(htmlData);
        #print();

        # tabs = re.findall(r'\b(Yearly|Monthly|Weekly)\b',''.join(htmlData))

        # for tab in tabs:
        #     parentDiv = response.css('div.govuk-tabs__panel#' + tab.upper())
        #     details = parentDiv.css('dl.govuk-summary-list')

        #     yield {
        #         tab: {
        #             'TabTitle': parentDiv.css('div.govuk-panel__body::text').get().replace('\n        ', '') + parentDiv.css('div.govuk-panel__body strong::text').get(),
        #             parentDiv.css('h2.govuk-heading-l:nth-child(2)::text').get(): {
        #                 details[0].css('div.govuk-summary-list__row:nth-child(1) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
        #                     details[0].css('div.govuk-summary-list__row:nth-child(1) dd.govuk-summary-list__value::text').get().replace('\n        ', '').replace('\n      ', ''),
        #                 details[0].css('div.govuk-summary-list__row:nth-child(2) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
        #                     details[0].css('div.govuk-summary-list__row:nth-child(2) dd.govuk-summary-list__value::text').get().replace('\n        ', '').replace('\n      ', ''),
        #                 details[0].css('div.govuk-summary-list__row:nth-child(3) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
        #                     details[0].css('div.govuk-summary-list__row:nth-child(3) dd.govuk-summary-list__value strong::text').get().replace('\n        ', '').replace('\n      ', ''),
        #             },
        #             parentDiv.css('h2.govuk-heading-l:nth-child(4)::text').get(): {
        #                 details[1].css('div.govuk-summary-list__row:nth-child(1) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
        #                     details[1].css('div.govuk-summary-list__row:nth-child(1) dd.govuk-summary-list__value::text').get().replace('\n        ', '').replace('\n      ', ''),
        #                 details[1].css('div.govuk-summary-list__row:nth-child(2) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
        #                     details[1].css('div.govuk-summary-list__row:nth-child(2) dd.govuk-summary-list__value::text').get().replace('\n        ', '').replace('\n      ', ''),
        #                 details[1].css('div.govuk-summary-list__row:nth-child(3) dt.govuk-summary-list__key::text').get().replace('\n        ', '').replace('\n      ', ''):
        #                     details[1].css('div.govuk-summary-list__row:nth-child(3) dd.govuk-summary-list__value strong::text').get().replace('\n        ', '').replace('\n      ', ''),
        #             }
        #         }
        #     }

    def parse(self, response):
        pass
