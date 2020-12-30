from PIL import Image
from rest_framework import permissions
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.image_recognizer.non_database_models import Prediction
from apps.image_recognizer.serializers import PredictionSerializer
from apps.image_recognizer.services import ImageRecognitionService


class PredictImageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        try:
            request_image = request.data['image']
            pil_image: Image.Image = Image.open(request_image)
            recognition_service = ImageRecognitionService()
            predicted_character = recognition_service.predict(pil_image)
            prediction = Prediction(predicted_character)
            serializer = PredictionSerializer(prediction)
            return Response(serializer.data)
        except KeyError:
            raise ParseError('Request has no resource file attached')
