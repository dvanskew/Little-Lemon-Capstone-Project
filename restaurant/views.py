from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import booking, menu, booking
#from .serializer import MenuSerializer, BookingSerialize
#from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
import json
from datetime import datetime



# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def menu(request):
    menu_items = menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_items})

class BookingView(APIView):
    def get(self, request):
        bookings = booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class MenuView(APIView):
    def get(self, request):
        menu_items = menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
#from .serializer import menuSerializer, BookingSerializer

#class BookingView(generics.ListCreateAPIView):
   # permission_classes = [AllowAny]
   # queryset = booking.objects.all()
    #serializer_class = BookingSerializer
    
    #def get_queryset(self):
        #date = self.request.query_params.get('date', None)
        #if date is not None:
           # return self.queryset.filter(booking_date=date)
        #return self.queryset
    
#from .serializer import menuSerializer, BookingSerializer

#class MenuView(generics.ListCreateAPIView):
    #permission_classes = [AllowAny]
    #queryset = menu.objects.all()
    #serializer_class = menuSerializer
    
    #def get_queryset(self):
       # category = self.request.query_params.get('category', None)
       # if category is not None:
        #    return self.queryset.filter(category=category)
        #return self.queryset
    
    #My code above.
#class MenuItemsView(generics.ListCreateAPIView):
   # permission_classes = [AllowAny]
    #queryset = menu.objects.all()
    #serializer_class = menuSerializer

#class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
   
    #queryset = menu.objects.all()
    #serializer_class = menuSerializer

  
#class BookingViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    #queryset = Booking.objects.all()
    #serializer_class = BookingSerializer

def book(request):
    form = BookingForm
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

def about(request):
    return render(request, "about.html")

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(booking_date=data['booking_date']).filter(
            no_of_guests=data['no_of_guests']).exists()
        if exist==False:
            booking = Booking(
                name=data['name'],
                booking_date=data['booking_date'],
                no_of_guests=data['no_of_guests'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')


def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    print("date: ", date)
    bookings = Booking.objects.all().filter(booking_date = date)
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})

