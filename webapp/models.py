from django.db import models
from django.contrib.auth.models import User  # Импортируем модель пользователя, если нужно

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Ссылка на пользователя, если есть
    order_number = models.CharField(max_length=20, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    # Добавьте другие поля заказа, если необходимо

    def __str__(self):
        return f"Order #{self.order_number}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20, default='pending')
    payment_date = models.DateTimeField(auto_now=True)

    MONTH_CHOICES = [
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]

    expiration_date_month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    expiration_date_year = models.PositiveIntegerField()

    cvv = models.CharField(max_length=4)
    card_number = models.CharField(max_length=16)
    owner = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Добавьте другие поля для платежей, если необходимо

    def __str__(self):
        return f"Payment #{self.pk} for Order #{self.order.order_number}"


class Transaction(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    transaction_status = models.CharField(max_length=20)
    transaction_date = models.DateTimeField(auto_now=True)
    # Добавьте другие поля для транзакций, если необходимо

    def __str__(self):
        return f"Transaction #{self.pk} for Payment #{self.payment.pk}"

