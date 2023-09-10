from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from .forms import PaymentForm  # Импортируйте форму PaymentForm из вашего приложения


stripe.api_key = settings.STRIPE_SECRET_KEY  # Замените 'your_stripe_api_key' на ваш ключ Stripe

def index(request):
    # Ваш код для обработки запроса
    return render(request, 'webapp/index.html')

@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Получите данные из формы
            order = form.cleaned_data['order']
            payment_amount = form.cleaned_data['payment_amount']
            payment_method = form.cleaned_data['payment_method']
            expiration_date_month = form.cleaned_data['expiration_date_month']
            expiration_date_year = form.cleaned_data['expiration_date_year']

            # Создайте Stripe токен (необходимо подключить Stripe.js для этого)
            try:
                token = stripe.Token.create(
                    card={
                        "number": form.cleaned_data['card_number'],
                        "exp_month": expiration_date_month,
                        "exp_year": expiration_date_year,
                        "cvc": form.cleaned_data['cvv'],
                    },
                )

                # Создайте платеж в Stripe
                charge = stripe.Charge.create(
                    amount=int(payment_amount * 100),  # Сумма в центах
                    currency='usd',
                    source=token.id,
                    description=f'Payment for Order #{order}',
                )

                # Обработка успешного платежа
                return JsonResponse({'success': True, 'message': 'Payment successful.'})
            except stripe.error.StripeError as e:
                # Обработка ошибок Stripe
                return JsonResponse({'success': False, 'message': str(e)})

    else:
        form = PaymentForm()

    return render(request, 'webapp/index.html', {'form': form})
