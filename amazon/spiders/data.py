import scrapy

class Data(scrapy.Spider):
    name = 'amazon'
    p = 2
    start_urls = ['https://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&qid=1630559628&rnid=2684818031&ref=lp_976390031_nr_p_n_publication_date_1']

    def parse(self, response, **kwargs):
        title = response.css(".a-color-base.a-text-normal::text").extract()
        image = response.css('.s-image::attr(src)').extract()

        yield {
            'title':title,
            'image':image
        }
        next_p = 'https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&page=' + str(Data.p) +'&qid=1630561593&rnid=2684818031&ref=sr_pg_3'

        if Data.p <= 75:
            Data.p += 1
            yield response.follow(next_p, callback=self.parse)
