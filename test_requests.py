import os
import django
from django.test import Client

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

client = Client()

urls_to_test = [
    "/",
    "/tournament/login/",
    "/tournament/register/",
    "/tournament/gallery/",
    "/tournament/gallery2/",
    "/tournament/player/",
    "/tournament/player/manage/",
    "/tournament/player/add/",
    "/tournament/contact/",
    "/tournament/aboutus/",
    "/tournament/coach/",
    "/tournament/coachview/",
    "/tournament/coach/add/",
    "/tournament/upcoming/",
    "/store/",
    "/store/product",
    "/store/product/add/",
    "/store/cart/",
    "/store/checkout/",
]

for url in urls_to_test:
    try:
        response = client.get(url)
        print(f"{url} -> {response.status_code}")
    except Exception as e:
        print(f"{url} -> ERROR: {e}")
