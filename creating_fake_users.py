import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_django.settings')

import django
django.setup()

from fake.models import UserCredentials
from faker import Faker

fake = Faker()


def populate(n=10):
    for counter in range(n):
        fake_first = fake.first_name()
        fake_last = fake.last_name()
        fake_email = fake_first.lower().split()[0] + fake_last.lower().split()[0] + '@' + fake.email().split('@')[1]

        UserCredentials.objects.get_or_create(first_name=fake_first, last_name=fake_last, email=fake_email)


if __name__ == '__main__':
    print('working on it')
    populate(20)
