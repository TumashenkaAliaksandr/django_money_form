from django import forms
from .models import Payment  # Замените .models на путь к вашим моделям

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order_number', 'total_amount', 'owner', 'cvv', 'card_number', 'expiration_date_month', 'expiration_date_year']
        # Добавьте остальные поля, если необходимо
