from django.shortcuts import render
from django.conf import settings
from foodApiApp.models import Administator, Menu, Food, SpecialItem,MostPopular, Customer, Order, OrderItem, Payment
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views
from rest_framework import permissions
from rest_framework.response import Response
from foodApiApp.serializers import UserSerializer, GroupSerializer, CustomerSerializer, CatagorySerializer, SpecialOfferSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CatagoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = CatagorySerializer

class SpecialOfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SpecialItem.objects.all()
    serializer_class = SpecialOfferSerializer

# class CustomViewset(viewsets.ModelViewSet):
#     queryset = Administator.objects.all()
#     serializer_class = CustomSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class Saydur(views.APIView):
    permission_classes = [

    ]

    def get(self, request):
        request.user
        customer = Customer.objects.get(user=request.user)
        category = customer.order_set.all().first().orderitem.food.catagory
        # catagory = Food.objects.catagory
        mostPopular = MostPopular.objects.all()
        mp_arr = []
        for item in mostPopular:
            mp_arr.append({"name": item.name, "price": item.price, "description": item.description})
        specialItem = SpecialItem.objects.all()
        si_arr = []
        for item in specialItem:
            si_arr.append({
                "menu" : item.menuName
            })
        return Response({"Name": customer.name, "Catagory":category,"Most Popular":mp_arr, "Special Offer":si_arr,})


def index(request):
    administator = Administator.objects.all().first()
    menu = Menu.objects.all().first()
    food = Food.objects.all().first()
    specialItem = SpecialItem.objects.all().first()
    mostPopular = MostPopular.objects.all().first()
    customer = Customer.objects.all().first()
    order = Order.objects.all().first()
    orderItem = OrderItem.objects.all().first()
    payment = Payment.objects.all().first()

    con = {
        'administator': administator,
        'menu': menu,
        'food': food,
        'specialItem': specialItem,
        'mostPopular': mostPopular,
        'customer': customer,
        'order': order,
        'orderItem': orderItem,
        'payment': payment,
    }

    return render(request,con)