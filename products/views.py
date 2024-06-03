from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from .models import ProductsModel, CategoryModel
from .serializers import ProductsSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


# class ProductsViewSet(ModelViewSet):
#     permission_classes = [AllowAny]
#     queryset = ProductsModel.objects.all()
#     serializer_class = ProductsSerializer

#     # If need filter list
#     # def get_queryset(self):
#     #     pk = self.kwargs.get("pk")

#     #     if not pk:
#     #         return ProductsModel.objects.all()[0:3]
        
#     #     return ProductsModel.objects.filter(pk=pk)

#     # If need take one category
#     # @action(methods=["get"], detail=True)
#     # def category(self, request, pk=None):
#     #     cats = CategoryModel.objects.get(pk=pk)
#     #     return Response({"cats": cats.name})
    
#     # If need take all categories
#     @action(methods=["get"], detail=False)
#     def category(self, request):
#         cats = CategoryModel.objects.all()
#         return Response({"cats": [c.name for c in cats]})
    




class ProductsAPIViewList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer


class ProductsAPIViewUpdate(RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer


class ProductsAPIViewDestroy(RetrieveDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer


# class ProductsAPIViewCRUD(RetrieveUpdateDestroyAPIView):
# #     permission_classes = [AllowAny]
# #     queryset = ProductsModel.objects.all()
# #     serializer_class = ProductsSerializer