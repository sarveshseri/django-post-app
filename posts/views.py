import time

from django.db import IntegrityError
from django.views.decorators.cache import cache_page

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status as drf_http_status

from .exceptions import ValidationException

from .models import Post, PostAnalysis
from .serializers import PostSerializer, PostCreateSerializer, PostAnalysisSerializer
from .util import create_analysis

import traceback


@api_view(['POST'])
def create_post(request):
    json_data = JSONParser().parse(request)
    print(json_data)
    request_serializer = PostCreateSerializer(data=json_data)
    if request_serializer.is_valid():
        try:
            post = Post.objects.create(
                id=request_serializer.data.get('id'),
                content=request_serializer.data.get('content'))
            post.save()
            response_serializer = PostSerializer(post)
            return Response(response_serializer.data, status=drf_http_status.HTTP_200_OK)
        except IntegrityError as ex:
            if 'unique constraint' in str(ex.args).lower():
                return Response(data={"error": "duplicate post id"}, status=drf_http_status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            traceback.print_exc()
            return Response(data={"error": str(ex.args)}, status=drf_http_status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        raise ValidationException("Invalid Request")


@api_view(['GET'])
@cache_page(60)
def get_post_analysis(request, id):
    try:
        post_analysis = PostAnalysis.objects.get(post_id=id)
    except PostAnalysis.DoesNotExist:
        try:
            post_analysis = create_analysis(post_id=id)
            post_analysis.save()
        except Post.DoesNotExist:
            return Response(data={"error": "post does not exist"}, status=drf_http_status.HTTP_400_BAD_REQUEST)
    response_serializer = PostAnalysisSerializer(post_analysis)
    return Response(response_serializer.data, status=drf_http_status.HTTP_200_OK)
