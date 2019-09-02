from requests_html import HTMLSession
import re


class HtmlScraper:

    def __init__(self):
        self.session = HTMLSession()
        self.success_code = 200

    def request_html(self, url):
        page = self.session.get(url)
        if page.status_code != self.success_code:
            raise Exception("HTML request failed: status code {}".format(page.status_code))
        return page.html.html

    def extract_links(self, url):
        page = self.session.get(url)
        if page.status_code != self.success_code:
            raise Exception("HTML request failed: status code {}".format(page.status_code))
        return list(page.html.links)

    def filter_links(self, links, pattern=None):
        if pattern is None:
            return links
        return [link for link in links if re.match(re.compile(pattern), link) is not None]

    def save(self, content, path):
        fh = open(path, "w")
        fh.write(content)
        fh.close()
