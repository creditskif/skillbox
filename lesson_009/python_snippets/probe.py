from pprint import pprint

file_name = 'pushkin.txt'
# file = open(file_name, mode='r')  # mode (режим): чтение символьное
file = open(file_name, mode='r', encoding='utf8')
file_content = file.read()
file.close()
pprint(file_content)