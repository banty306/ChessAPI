from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chess.serializers.play_serializer import PlaySerializer
from chess.controllers.play_controller import PlayController
from chess.config import SlugName


class PlayView(APIView):
    def post(self, request, *args, **kwargs):
        req_data = PlaySerializer(self, request.data)
        req_data.is_valid(raise_exception=True)
        data = req_data.validated_data
        slug = kwargs.get('slug')

        valid_slug = [SlugName.BISHOP.value, SlugName.QUEEN.value, SlugName.KNIGHT.value, SlugName.ROOK.value]
        if slug not in valid_slug:
            return Response({'error': 'Invalid slug'}, status=status.HTTP_400_BAD_REQUEST)

        response = PlayController().find_next_move(data, slug)
        return Response(response, status=status.HTTP_200_OK)
