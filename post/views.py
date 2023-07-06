from django.shortcuts import render

from .models import Course, Student


# Create your views here.
def posts_list(request):
    queryset = Course.objects.all()
    print(queryset)
    return render(request, 'listing.html', {'posts': queryset})


# ----------------------------------------------------------

# REST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def course_list_api_view(request):
    queryset = Course.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

# @api_view(['DELETE'])
# def delete(request, id):
#     post = get_object_or_404(Course, pb=204)