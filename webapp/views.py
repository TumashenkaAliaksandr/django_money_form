from django.shortcuts import render, redirect
from .forms import PaymentForm  # Импортируйте вашу форму
from .models import Payment  # Импортируйте модель Payment


def index(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_data = form.cleaned_data
            payment = Payment(
                order_number=payment_data['order_number'],  # Пример: получите данные из формы
                total_amount=payment_data['total_amount'],  # Пример: получите данные из формы
                # Другие поля модели Payment
            )
            payment.save()
            # Здесь вы можете обработать оплату через платежный шлюз
            # Например, payment.charge(payment_data['total_amount'])
            return redirect('payment_success')  # Замените 'payment_success' на правильный URL
    else:
        form = PaymentForm()

    return render(request, 'webapp/index.html', {'form': form})
