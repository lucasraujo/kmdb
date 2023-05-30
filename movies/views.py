from rest_framework import generics
from .models import Movie
from .serializers import MoviesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.kwargs.user, genres=self.kwargs.genres)
