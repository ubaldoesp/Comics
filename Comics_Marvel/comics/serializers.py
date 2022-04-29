from rest_framework.serializers import ModelSerializer
from .models import Comic
class ComicsSerializers(ModelSerializer):
    class Meta:
        model= Comic
        fields= '__all__'