from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi", unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="categories/photos/", null=True, blank=True, verbose_name="Rasmi")
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Kategoriya",
                               related_name="subcategories")

    def __str__(self):
        if self.parent:
            return f"Sub: {self.name}"
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ('pk',)

    def send_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return "https://avatars.mds.yandex.net/i?id=7944b3d2cb8a76e3d06265db5b82b258_l-5661780-images-thumbs&n=13"


QUALITY = [
    ('or', 'organic'),
    ('gmo', 'GMO'),
]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Mahsulot nomi")
    slug = models.SlugField(max_length=160, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="Mahsulot haqida...")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Narxi")
    discount = models.IntegerField(null=True, blank=True, verbose_name="Chegirma (%)")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Ombordagi soni")
    weight = models.PositiveIntegerField(verbose_name="Vazni")
    made_in = models.CharField(max_length=100, verbose_name="Yetishtirilgan")
    quality = models.CharField(max_length=3, choices=QUALITY, verbose_name="Sifati")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Kategoriya",
                                 related_name="products")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ('-pk',)

    def get_image(self):
        # images = Images.objects.filter(product=self)
        # images = self.images_set.all()
        images = self.images.all()
        if images:
            return images[0].image.url
        return "https://www.nugaedu.gr/style/images/no-image.jpg"


class Images(models.Model):
    '''Product Images'''
    image = models.ImageField(upload_to="products/images/", verbose_name="Rasmi")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Mahsulot", related_name="images")

    def __str__(self):
        return f"{self.product.name} | {self.image.name}"

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"

