import os
import sys
from django.core.management.utils import get_random_secret_key

# Настройка окружения Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MySite.settings")

def run():
    print(f"SECRET_KEY={get_random_secret_key()}")

if __name__ == "__main__":
    run()