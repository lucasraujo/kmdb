from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Review
from .serializers import ReviewSerializer


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "movie_id"

    def perform_create(self, serializer):
        return serializer.save(
            movie_id=self.kwargs.get("movie_id"), 
            critic=self.kwargs.user
            )