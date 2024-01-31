from django.shortcuts import render
from books.models import Book
from rest_framework.decorators import api_view
from books.serializers import bookserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# @api_view(['GET','POST'])
# def booklist(request):
#     if(request.method=="GET"):
#         books=Book.objects.all()
#         s=bookserializer(books,many=True)
#         return Response(s.data)
#     elif(request.method=="POST"):
#         s=bookserializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#     return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def book_detail(request,pk):
#     try:
#         book=Book.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if(request.method=="GET"):
#         s = bookserializer(book)
#         return Response(s.data)
#     elif(request.method=="PUT"):
#         s = bookserializer(book,data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=="DELETE"):
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import mixins,generics,viewsets

#          MIXINS

# class booklist(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class book_detail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#
#     def get(self, request, pk):
#         return self.retrieve(request)
#
#     def put(self, request, pk):
#         return self.update(request)
#
#     def delete(self, request, pk):
#         return self.delete(request)


#         GENERICS

# class booklist( generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#
# class book_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
# #


#    USING VIEWSETS

class bookviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class = bookserializer

# from books.models import User
from django.contrib.auth.models import User
from books.serializers import userserializer



# registration
class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer

