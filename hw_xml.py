import xml.etree.ElementTree as ET

TOP = 10
FILE = 'newsafr.xml'


def words_from_news(filename):
    all_words = []

    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(filename, parser)

    root = tree.getroot()
    xml_items = root.findall('channel/item')

    for item in xml_items:
        all_words += item.find('description').text.lower().split(' ')
    return all_words


def repeats_count(words_list):
    repeats = {}
    for word in words_list:
        if len(word) >= 6:
            if word not in repeats.keys():
                repeats.setdefault(word, 1)
            else:
                repeats[word] += 1
    return repeats


def print_rating(rep_dict, amount):
    for i, pair in enumerate(sorted(rep_dict.items(), key=lambda x: x[1], reverse=True), 1):
        print(f'{i} - слово "{pair[0].upper()}" встречается {pair[1]} раз')
        if i + 1 > amount:
            break
    return


print_rating(repeats_count(words_from_news(FILE)), TOP)
