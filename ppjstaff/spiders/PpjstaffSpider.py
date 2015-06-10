import scrapy

from ppjstaff.items import PpjstaffItem

class PpjstaffSpider(scrapy.Spider):
    name = "Ppjspider"
    allowed_domains = ["www.ppj.gov.my"]
    start_urls = [
        "http://www.ppj.gov.my/iisApp/carta_organisasi_ppj_dtl.asp?dept_code=%"
    ]

    def parse(self, response):
        for sel in response.xpath('//table/tr'):
            item = PpjstaffItem()
            item['bil'] = sel.xpath('td [@valign="top"][@class="windowbg2"][@width="20"]/text()').extract()
            item['nama'] = sel.xpath('td [@valign="top"][@class="windowbg2"][@width="200"]/text()').extract()
            item['jawatan'] = sel.xpath('td [@valign="top"][@class="windowbg2"][@width="270"]/text()').extract()
            item['gelaran'] = sel.xpath('td [@valign="top"][@class="windowbg2"][@width="80"]/text()').extract()
            item['ext'] = sel.xpath('td [@valign="top"][@class="windowbg2"][@width="50"]/text()').extract()
            item['fax'] = sel.xpath('td [@valign="top"][@class="windowbg2"][@width="100"]/text()').extract()
            item['email'] = sel.xpath('td [@valign="top"][@class="windowbg2"][@width="100"]/a/text()').extract()
            yield item
