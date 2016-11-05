from django.db.models import Q
from .models import Blog

def search(request):
    if request.GET:
        query = request.GET['q']
        search_result = Blog.objects.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
            )
        # import pdb; pdb.set_trace()
        return {'search_result': search_result}
    return {}