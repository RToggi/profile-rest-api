from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """Test API VIEW """

    name = serializers.CharField(max_length=10)
