def clean(text, header):
    text = text.replace(header, str()).replace('\n\n', '\n').replace('\n    \n', '\n')
    for line in text.replace('\xa0-', '').split('\n'):
        index = line.rfind('-')
        print(line[:index] + '-' + line[index + 1: index + 2] + line[index + 2].lower() + line[index + 3:])


