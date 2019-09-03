from data_extractor import DataExtractor
import json
from tqdm import tqdm


def get_FRIENDS_transcript():

    read_path = "html/FRIENDS/transcript/transcript.json"
    save_dir = "data/FRIENDS/transcript/"
    save_name = "transcript.json"

    fh = open(read_path, "r")
    json_str = fh.read()
    fh.close()

    json_obj = json.loads(json_str)

    for key in tqdm(list(json_obj.keys())):

        html = json_obj[key]

        extractor = DataExtractor("html")
        extractor.read(html)

        texts = extractor.extractText()

        try:
            begin_idx = texts.index("[Scene")
            texts = texts[begin_idx:]
            end_idx = len(texts) - texts[::-1].lower().index("dne")
            texts = texts[: end_idx]
            json_obj[key] = texts
        except Exception as e:
            print("Ignore transcripts for {}".format(key))


    print("Serializing...")
    json_str = json.dumps(json_obj)
    print("Done.")

    print("Saving...")
    extractor.save(json_str, save_dir + save_name)
    print("Done.")


def get_FRIENDS_summary():
    read_path = "html/FRIENDS/summary/summary.json"
    save_dir = "data/FRIENDS/summary/"
    save_name = "summary.json"

    fh = open(read_path, "r")
    json_str = fh.read()
    fh.close()

    json_obj = json.loads(json_str)

    html = json_obj["summary"]

    extractor = DataExtractor("html")
    extractor.read(html)
    h3_tags = extractor.findAllTags("h3")
    h3_contents = extractor.extractTextFromTagList(h3_tags)
    h3_contents.append("END")

    dl_tags = extractor.findAllTags("dl")
    dl_contents = " ".join(extractor.extractTextFromTagList(dl_tags))
    dl_contents = dl_contents + " END"

    res = {}
    for i in range(len(h3_contents) - 1):
        begin_txt = h3_contents[i]
        end_txt = h3_contents[i + 1]
        begin_idx = dl_contents.index(begin_txt)
        end_idx = dl_contents.index(end_txt)
        summary = dl_contents[begin_idx + len(begin_txt) + 1: end_idx]
        try:
            strip_idx = summary.index("   ")
            summary = summary[:strip_idx]
        except Exception:
            pass
        seq_num = begin_txt[:begin_txt.index(" ")]
        dot_idx = seq_num.index(".")
        s_num = seq_num[:dot_idx]
        e_num = seq_num[dot_idx + 1:]
        seq_num = s_num.zfill(2) + e_num.zfill(2)
        res[seq_num] = summary

    print("Serializing...")
    json_str = json.dumps(res)
    print("Done.")

    print("Saving...")
    extractor.save(json_str, save_dir + save_name)
    print("Done.")




if __name__ == "__main__":
    get_FRIENDS_summary()
