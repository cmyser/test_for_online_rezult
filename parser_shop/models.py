from django.db import models

class Product(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title



class Product_Info(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    applying = models.TextField()
    composition = models.TextField()
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Информация о продукте'
        verbose_name_plural = 'Информация о продуктах'

    def __str__(self):
        return self.product.title


class Mentions(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mention_mail = models.CharField(max_length=255)
    mention_text = models.TextField()


    class Meta:
        verbose_name = 'мнение'
        verbose_name_plural = 'мнения'

    def __str__(self):
        return self.product.title

    
