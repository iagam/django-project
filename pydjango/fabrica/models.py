from django.db import models

# Create your models here.


class Product:
    id: int
    name: str
    desc: str
    rating: float
    img: str
    price: int
    offer: bool
