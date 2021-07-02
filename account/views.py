from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status         # for send status
from rest_framework.views import APIView  # class view


class SignupAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)  # handle incoming json requests, get data from request

        # validate the input data and confirm that all required fields are correct
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):

    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



class UploadAPIView(APIView):
    # Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]

    # Parses multipart HTML form content, which supports file uploads
    parser_classes = (MultiPartParser, )

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)  # handle incoming json requests, get data from request

        if serializer.is_valid():
            return Response("Your Token is ok!", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)