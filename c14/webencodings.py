import codecs

HTML = '''
<!DOCTYPE html>
<html>
<head>
%(declared)s
<style type="text/css">
</style>
<title>%(title)s</title>
</head>
<body>

<p>%(text)s</p>

</body>
</html>
'''

utf8_text = 'Hello–“World” £1-€6 is ‘great’ for UK!'
latin1_text = 'Amélie, Jörgen, Theuß, Thérèse, and Søren'



def charset(coding=None):
    if coding is None:
        return ''
    return f'<meta charset="{coding}"/>'


cases = {
    'utf8-encoded-no-declaration.html': {
        'actual': 'UTF-8',
        'declared': charset(None),
        'title': 'UTF-8 encoding, no declaration'
    },
    'utf8-encoded-correctly-declared.html': {
        'actual': 'UTF-8',
        'declared': charset('UTF-8'),
        'title': 'UTF-8 encoding, correctly declared',
    },
    'utf8-encoded-declared-latin1.html': {
        'actual': 'UTF-8',
        'declared': charset('iso-8859-1'),
        'title': 'UTF-8encoding, declared as latin-1',
    },
    'latin1-encoded-no-declaration.html': {
        'actual': 'iso-8859-1',
        'declared': charset(None),
        'title': 'Latin1--encoding, no declaration',
    },
    'latin1-encoded-correctly-declared.html': {
        'actual': 'iso-8859-1',
        'declared': charset('iso-8859-1'),
        'title': 'Latin1 encoding, correctly declared',
    },
    'latin1-encoded-declared-utf-8.html': {
        'actual': 'iso-8859-1',
        'declared': charset('UTF-8'),
        'title': 'Latin-1 encoding, declared as UTF-8',
    },
}


for filename, params in cases.items():
    actual = params['actual']
    with codecs.open(filename, 'w', encoding=actual) as f:
        params['text'] = utf8_text if actual == 'UTF-8' else latin1_text
        f.write(HTML % params)
        print(f'Written {filename}.')

