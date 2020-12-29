from PIL import Image
from rest_framework import permissions
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.image_recognizer.models.prediction import Prediction
from apps.image_recognizer.serializers import ImageSerializer
from apps.image_recognizer.serializers import PredictionSerializer


class PredictImageView(APIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        try:
            request_image = request.data['image']
            pil_image: Image.Image = Image.open(request_image)
            prediction = Prediction(pil_image.fp)
            serializer = PredictionSerializer(prediction)
            return Response(serializer.data)
        except KeyError:
            raise ParseError('Request has no resource file attached')
