from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .serializers import UserPlanetArmySerializer


class UserPlanetArmyAPIView(APIView):

    # Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]

    # Parses multipart HTML form content, which supports file uploads
    parser_classes = (MultiPartParser, )

    def post(self, request, *args, **kwargs):
        # serializer
        serializer = UserPlanetArmySerializer(data=request.data)  # handle incoming json requests

        # validate the input data and confirm that all required fields are correct
        if serializer.is_valid():

            # to save the object for the actual user
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
{'crew_id': 1,
 'crew_name': 'slayer',
 'crew_level': 20
 'crew_values': {'ATT': 60,
                'DEF': 20,
                            }
}
--------------------------------------
maybe better like this

{'crew_id': 1,
 'crew_name': 'slayer',
 'crew_level': 20,
 'crew_att': 60,
 'crew_def': 30
}
"""