from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from shop.shop_items import shop_items
from .serializers import UserTroopSerializer


class ShopAPIView(APIView):
    # Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]

    # Parses multipart HTML form content, which supports file uploads
    parser_classes = (MultiPartParser,)

    # to return the list of items available
    def get(self, request, *args, **kwargs):
        shop_troops = shop_items.shop_troops
        return Response(shop_troops, status=status.HTTP_200_OK)


class UserTroopsAPIViews(APIView):
    # Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]

    # Parses multipart HTML form content, which supports file uploads
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        # serializer
        serializer = UserTroopSerializer(data=request.data)  # handle incoming json requests

        troop_id = request.data['troop_id']
        troop_info = shop_items.shop_troops[int(troop_id)]


        # validate the input data and confirm that all required fields are correct
        if serializer.is_valid():

            # to save the object for the actual user
            serializer.save(user=request.user,
                            troop_name=troop_info['troop_name'], troop_level=troop_info['troop_level'],
                            troop_att=troop_info['troop_att'], troop_def=troop_info['troop_def'])

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
