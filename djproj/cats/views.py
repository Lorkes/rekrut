from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Cat, Hunting
from .serializers import HuntingSerializer


@api_view()
def list_users(request):
    return Response({f'User {user.id}': user.user_total_cats for user in User.objects.all()})


@api_view(['GET'])
def user_cats(request, user_id):
    cats = [[c.cat_name, c.cat_coloration, c.cat_male, Hunting.objects.filter(cat_went=c.id).count()]
            for c in Cat.objects.filter(cat_owner_id=user_id)]
    cat_fields = ['Name', 'Coloration', 'Male', 'Huntings']
    return Response({
        'User_id': user_id,
        'User': User.objects.filter(id=user_id)[0].user_name,
        'Cats': [dict(zip(cat_fields, cat)) for cat in cats],
    })


@api_view(['GET', 'POST'])
def add_hunting(request):
    if request.method == 'GET':
        return Response({"method_error": 'This is the POST endpoint. Please provide new hunting data.'})
    hunt = HuntingSerializer(data=request.data)
    if hunt.is_valid():
        hunt.save()
        return Response({"message": "Hunting successfully saved."})
    else:
        return Response(status=400)
