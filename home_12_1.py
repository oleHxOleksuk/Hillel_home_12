import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = re.sub(r'<[^>]+>', '', html)

    clean_text = re.sub(r'&[a-zA-Z0-9#]+;', '', clean_text)

    cleaned_lines = []
    for line in clean_text.splitlines():
        stripped = line.strip()
        if stripped:
            cleaned_lines.append(stripped)

    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write('\n'.join(cleaned_lines))

delete_html_tags('draft.html')