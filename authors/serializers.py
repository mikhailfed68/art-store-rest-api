from rest_framework import serializers

from authors.models import Painter


class PainterDetailSerializer(serializers.ModelSerializer):
    artworks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='product-detail')

    class Meta:
        model = Painter
        fields = [
            'id', 'first_name', 'last_name', 'avatar',
            'birthday', 'about_yourself', 'education',
            'exhibitions', 'tags', 'artworks',
        ]
        depth = 1


class PainterListSerializer(serializers.HyperlinkedModelSerializer):
    artworks_counter = serializers.IntegerField(source='count_artworks')

    class Meta:
        model = Painter
        fields = ['url', 'id', 'first_name', 'last_name', 'avatar', 'artworks_counter']
