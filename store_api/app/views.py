from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app.models import Order
from app.forms import FormOrder
from django.views.decorators.http import require_POST, require_GET

def index(request):
    return render(request, 'index.html')

def orderCreate(request):
    """Create a new Order"""
    form = FormOrder(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/app/orders/')

@require_GET
def NewOrder(request):
    return render(request, 'neworders.html')

@require_GET
def orderDetail(request, id):
    """Detail of each order"""
    try:
        order = Order.objects.get(id=id)
        order = order.serializer()
        return JsonResponse(order, status=200)
    except Exception as err:
        return JsonResponse({'Error' : 'Error: Order Not found'}, status=400)

@require_GET
def statusOrder(request):
    """Order status"""
    pass

@require_GET
def listOrders(request):
    """Display the list orders"""
    return JsonResponse({
        'orders':[order.serializer() for order in Order.objects.all()
    ]}, status=200)