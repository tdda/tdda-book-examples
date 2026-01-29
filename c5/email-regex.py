import re

EMAIL_RE = re.compile(r'^(.+)@(.+)\.(.+)$')
EMAILS = (
    'quality@tdda.info',
    'More.Quality@longer.tdda.info',
    '@tdda@tdda.info',
    '@tddd@tddc@tddb.tdda.info',
    '@tdda.info'
)

for email in EMAILS:
    m = re.match(EMAIL_RE, email)
    print(email)
    print(m)
    if m is not None:
        print(m.groups())
    print()

m = re.match(EMAIL_RE, 'njr@tdda.info')
for i in range(4):
    print(f'm.group({i}):', repr(m.group(i)))
