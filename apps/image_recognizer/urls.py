from django.urls import path

from apps.image_recognizer.views import PredictImageView

urlpatterns = [
    path('api/predict', PredictImageView.as_view()),
]
