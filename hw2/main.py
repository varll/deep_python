def parse_html(html_str: str, open_tag_callback, data_callback, close_tag_callback):
    tags = []
    data = {}
    idx = 0
    while idx != len(html_str):
        # Если не открыт никакой тег, то не записываем
        if tags and (html_str[idx] != '>' and html_str[idx] != '<'):
            data[tags[-1]] += html_str[idx]
        # Если нашли открывающий или закрывающий тег
        if html_str[idx] == '<':
            tag = '<'
            while html_str[idx] != '>':
                idx += 1
                tag += html_str[idx]

            if tag[1] != '/':
                tags.append(tag)
                data[tag] = ''
                open_tag_callback(tag)
            else:
                if data[tags[-1]] != '':
                    data_callback(data[tags[-1]])
                close_tag_callback(tag)
                tags.pop()
        idx += 1
