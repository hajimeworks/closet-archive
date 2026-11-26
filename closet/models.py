from django.db import models


class Item(models.Model):
    """図鑑に登録する服1着"""

    CATEGORY_CHOICES = [
        ("outer", "アウター"),
        ("tops", "トップス"),
        ("bottoms", "ボトムス"),
        ("shoes", "シューズ"),
        ("bag", "バッグ"),
        ("accessory", "小物"),
    ]
    STATUS_CHOICES = [("own", "所持"), ("sold", "手放した")]

    name = models.CharField("名前", max_length=100)
    category = models.CharField("カテゴリ", max_length=20, choices=CATEGORY_CHOICES)
    color = models.CharField("色", max_length=30, blank=True)
    brand = models.CharField("ブランド", max_length=100, blank=True)
    era = models.CharField("シーズン・年代", max_length=50, blank=True)
    material = models.CharField("素材", max_length=100, blank=True)
    price = models.PositiveIntegerField("購入価格", null=True, blank=True)
    bought_on = models.DateField("購入日", null=True, blank=True)
    shop = models.CharField("購入場所", max_length=100, blank=True)
    image = models.ImageField("写真", upload_to="items/", blank=True)
    status = models.CharField("状態", max_length=10, choices=STATUS_CHOICES, default="own")
    notes = models.TextField("メモ", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"No.{self.id:03d} {self.name}"
    