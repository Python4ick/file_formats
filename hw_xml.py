import xml.etree.ElementTree as ET

# Преподавателю: декомпозицию кода не делаю осознанно, так как длина кода в данной конкретной короткой задаче увеличится
words = []  # список слов из всех новостей
unique_words = []  # список уникальных слов
top_list = []  # списко кортежей [(слово, повторы)]

# пишем парсер, парсим
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)

# получаем корневой root
root = tree.getroot()

# ищем все новости в channel/item => decription, делим их на слова и добавляем в список, далее как в прошлом задании
xml_items = root.findall('channel/item')
for item in xml_items:
    words += item.find('description').text.lower().split(' ')

# получаем сортированный список кортежей из уникальных слов с подсчетом повторов [('африки', 42), ('туристов', 40)...]
for word in words:
    if len(word) >= 6 and word not in unique_words:
        unique_words.append(word)
        top_list.append((word, words.count(word)))
top_list.sort(key=lambda top: top[1], reverse=True)

# распечатываем первые 10 элементов из сортированнного списка через enumerate, считая с 1
for number, rating in enumerate(top_list[:10], 1):
    print(f'{number} - cлово "{rating[0].upper()}" встречается {rating[1]} раз.')