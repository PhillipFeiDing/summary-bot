from tqdm import tqdm
import json
import re
from html_scraper import HtmlScraper


def get_FRIENDS_transcript():

    root_url = "https://fangj.github.io/friends/"
    link_pattern = "season/\d\d\d\d\.html"
    label_pattern = "\d\d\d\d"
    save_dir = "html/FRIENDS/transcript/"
    save_name = "transript.json"

    scraper = HtmlScraper()

    print("Extracting links from resource url...")
    links = scraper.filter_links(scraper.extract_links(root_url), link_pattern)
    print("Done.")

    labels_htmls = {}
    print("Pulling HTML from {} page(s)...".format(len(links)))
    for link in tqdm(links):
        label = re.search(re.compile(label_pattern), link).group(0)
        url = root_url + link
        try:
            html_str = scraper.request_html(url)
            labels_htmls[label] = html_str
        except Exception as e:
            print("Requesting url {} failed. msg: {}".format(url, e.args[0]))
            print("Action: ignore")
    print("\nDone.")

    print("Serializing...")
    json_str = json.dumps(labels_htmls)
    print("Done.")

    print("Saving...")
    scraper.save(json_str, save_dir + save_name)
    print("Done.")


def get_FRIENDS_summary():

    root_url = "http://www.friends-tv.org/epshort.html"
    save_dir = "html/FRIENDS/summary/"
    save_name = "sumamry.json"

    scraper = HtmlScraper()

    print("Pulling HTML from root url...")
    html_str = scraper.request_html(root_url)
    print("Done.")

    print("Serializing...")
    json_str = json.dumps({"summary": html_str})
    print("Done.")

    print("Saving...")
    scraper.save(json_str, save_dir + save_name)
    print("Done.")

if __name__ == "__main__":
    # get_FRIENDS_transcript()
    get_FRIENDS_summary()
