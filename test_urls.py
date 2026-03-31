import os
import django
from django.test import Client
from django.urls import get_resolver

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

client = Client()
resolver = get_resolver()

def get_urls(patterns, prefix=''):
    urls = []
    for pattern in patterns:
        if hasattr(pattern, 'url_patterns'):
            urls.extend(get_urls(pattern.url_patterns, prefix + pattern.pattern.regex.pattern))
        else:
            urls.append(prefix + pattern.pattern.regex.pattern)
    return urls

urls = get_urls(resolver.url_patterns)
for url in urls:
    # simplify regex patterns
    u = url.replace('^', '/').replace('$', '').replace('\\/', '/')
    print(u)
