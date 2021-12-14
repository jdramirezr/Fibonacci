from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from app.utils import fibonacci


class FibonacciView(APIView):

    def get(self, request):
        return Response({'k':fibonacci()}, status=HTTP_200_OK)

