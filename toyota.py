import scrapy
 
class ToyotaPythonSpider(scrapy.Spider):

    name = 'toyota.py'

    def start_requests(self):
        urls = ['https://lista.mercadolivre.com.br/toytoa-bandeirante#D[A:toytoa%20bandeirante]'] 
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):   
        for item in response.xpath('//div[@class="ui-search-result__content"]'):
            yield{
                'Carro':item.xpath('.//div//div/a/h2[@class="ui-search-item__title"]/text()').get(),
                'Preço':item.xpath('.//div//div/div/div/span/span[@class="andes-visually-hidden"]/text()').get(),
                'Ano': item.xpath('.//div//div//ul/li[@class="ui-search-card-attributes__attribute"][1]/text()').get(),
                'Kms': item.xpath('.//div//div//ul/li[@class="ui-search-card-attributes__attribute"][2]/text()').get()
            }
        
        # try:
        #     link_proxima_pagina = response.xpath('//a[@data-testid="pagination-page-next"]/@href').get()
        #     if link_proxima_pagina is not None:
        #         link_proxima_pagina_completo = response.urljoin(link_proxima_pagina)
        #         yield scrapy.Request(url=link_proxima_pagina_completo,callback=self.parse)
        # except:
        #     print('Chegamos na ultima página')
