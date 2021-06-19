from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .serializers import ImageSerializer




class UploadAPIView(APIView):

    # Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]

    # Parses multipart HTML form content, which supports file uploads
    parser_classes = (MultiPartParser, )

    def post(self, request, *args, **kwargs):
        # serializer
        serializer = ImageSerializer(data=request.data)  # handle incoming json requests


        # validate the input data and confirm that all required fields are correct
        if serializer.is_valid():

            result = "hello, your image has been correctly loaded into the DB"





            #serializer.save(user=request.user, result=result)


            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)