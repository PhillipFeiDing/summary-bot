from bs4 import BeautifulSoup


class DataExtractor:

    def __init__(self, type):
        assert type in ("html", "xml"), "This data extractor only parses HTML and XML documents."
        self.type = type
        self.soup = None

    def read(self, markup):
        if self.type == "html":
            self.soup = BeautifulSoup(markup, "lxml")
        else:
            self.soup = BeautifulSoup(markup, "lxml-xml")

    def findAllTags(self, tag):
        assert self.soup is not None, "This data extractor has no mark-up document to work on yet."
        return self.soup.find_all(tag)

    def findAllTagsInTagList(self, tag, tag_list):
        res = []
        for super_tag in tag_list:
            res = res + super_tag.find_all(tag)
        return res

    def extractTextFromTagList(self, tag_list):
        res = []
        for tag in tag_list:
            text = tag.text
            if text is not None:
                res.append(text.strip().replace("\n", " ").replace("\xa0", ""))
        return res

    def extractText(self):
        return self.soup.text

    def save(self, content, path):
        fh = open(path, "w")
        fh.write(content)
        fh.close()