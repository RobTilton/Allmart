import requests
import random
import time

import os
import sys
import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Allmart.settings")
django.setup()

from eshop_app.models import Product


def get_largest_product_id():
    largest_product = Product.objects.order_by('-id').first()
    if largest_product:
        return largest_product.id
    else:
        return None


def create_product(count):
    largest_product_id = get_largest_product_id() or 0

    url = 'http://127.0.0.1:8000/api/products/'
    
    for i in range(largest_product_id + 1 , largest_product_id + count + 1):
        data = {
            'name': f'Product Number {i}',
            'description': f'Number {i}',
            'cents': random.randint(25, 5000), 
            'stock': random.randint(1, 100),  
            'category': random.randint(1, 5)  
        }

        response = requests.post(url, data=data)

        if response.status_code == 201:
            print(f"Product {i} created successfully!")
        else:
            print("Failed to create product. Status code:", response.status_code)
            print("Response content:", response.text)
        
        time.sleep(0.5)

amount = int(input('How many new items do you want to make: '))
create_product(amount)