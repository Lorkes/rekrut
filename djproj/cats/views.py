from rest_framework.response import Response
from .models import User, Cat, Hunting
from rest_framework.decorators import api_view


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


