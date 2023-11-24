from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .tasks import create_file_task
from rest_framework.decorators import api_view


@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            create_file_task.delay(request.data['name'], request.data['data'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
