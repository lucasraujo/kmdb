from rest_framework.serializers import ModelSerializer
from .models import Movie


class MoviesSerializer(ModelSerializer):
    class Meta: 
        model = Movie
        fields = "__all__"
        read_only_fields = ["id"]
        

