from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Post, Comment, Category

class commentSerialzer(serializers.ModelSerializer):
    comment_by = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ('id','comment_by','post','body')

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.ReadOnlyField(source='post.title')
    class Meta:
        model = Category
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ('id','owner','title','body','comments','created','categories')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    posts = serializers.HyperlinkedIdentityField(view_name='post-detail',many=True,read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = User
        fields = ('id','username','posts','comments','categories')  

   