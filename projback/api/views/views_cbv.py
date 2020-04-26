from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Category,Image
from api.serializers import CategorySerializer2,ImageSerializer
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated


class CategoryListAPIView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        categories=Category.objects.all()
        serializer=CategorySerializer2(categories,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CategorySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoryDetailAPIView(APIView):
    def get_object(self,id):
        try:
             return Category.objects.get(id=id)
        except Category.DoesNotExist as e:
            return Response({'error': str(e)})
    def get(self,request,category_id):
        category=self.get_object(category_id)
        serializer = CategorySerializer2(category)
        return Response(serializer.data)
    def put(self,request,category_id):
        category=self.get_object(category_id)
        serializer = CategorySerializer2(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    def delete(self,request,category_id):
        category=self.get_object(category_id)
        category.delete()
        return Response({'deleted': True})
class CategoryVacanciesListAPIView(APIView):
    def get(self, request, category_id):
        try:
            vacancies = Image.objects.filter(category_id=category_id)
        except Image.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = ImageSerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)
class CategoryWithVacanciesListAPUView(APIView):
    def get(self, request, category_id):
        vacancies = Image.objects.filter(category_id=category_id)
        serializer = ImageSerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ImageListAPIView(APIView):
    def get(self, request):
        try:
            vacancies = Image.objects.all()
        except Category.DoesNotExist as e:
            return Response({'error': str(e)})
        serializer = ImageSerializer(vacancies, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ImageDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Image.objects.get(id=id)
        except Image.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, image_id):
        image = self.get_object(image_id)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def put(self, request, image_id):
        image = self.get_object(image_id)
        serializer = ImageSerializer(instance=image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, image_id):
        image = self.get_object(image_id)
        image.delete()

        return Response({'deleted': True})


class TopVacanciesListAPIView(APIView):
    def get(self, request):
        try:
            top_vacancies = Image.objects.order_by('-salary')[:10]
        except Image.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = ImageSerializer(top_vacancies, many=True)
        return Response(serializer.data)