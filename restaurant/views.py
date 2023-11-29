from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import booking, menu


# Create your views here.

class bookingView(APIView):
    def get(self, request):
        bookings = booking.objects.all()
        serializer = bookingSerializer(bookings, many=True)
        return Response(serializer.data)
# not sure if I need this post.
    def post(self, request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class menuView(APIView):
    def get(self, request):
        menu = menu.objects.all()
        serializer = menuSerializer(menu, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})
        