from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name') # show specific field
    
    class Meta:
        model = WatchList
        fields = '__all__'


# class StreamPlatformSerializer(serializers.ModelSerializer):
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # enable all field to be link 


    # serializer relationship
    # watchlist related_name
    watchlist = WatchListSerializer(many=True,read_only=True)

    # watchlist = serializers.StringRelatedField(many=True,read_only=True)
    # show the return (self.title)

    # watchlist = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # show the id

    # watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie-detail')
    # show the links
    # when we use it, we must provide (request)

    class Meta:
        model = StreamPlatform
        fields = '__all__'