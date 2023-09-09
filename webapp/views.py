import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    # Ваш код для обработки запроса
    return render(request, 'webapp/index.html')


@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        amount = int(request.POST.get('amount'))
        description = request.POST.get('description')

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description=description
            )
            # Обработка успешного платежа
            return JsonResponse({'success': True, 'message': 'Payment successful.'})
        except stripe.error.StripeError as e:
            # Обработка ошибок Stripe
            return JsonResponse({'success': False, 'message': str(e)})

