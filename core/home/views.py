from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT'])   #this func can have these methods.
def index(request):
    courses = {
    "course_name": "Python",
    "learn": ["Django", "Flask", "Tornado", "FastAPI"],
    "course_provider": "Scaler"
    }
    if request.method == 'GET':
        coursesapp = {
        "course_name": "App Development",
        "learn": ["Flutter", "Android", "FlutterFlow"],
        "course_provider": "Coursera"
        }
        return Response(coursesapp)
    elif request.method == 'POST':
        return Response(courses)