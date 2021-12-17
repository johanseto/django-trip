#Django 
from django.shortcuts import render
"""posts views"""
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
# posts=[
#     {
#         'name': 'My Dog.',
#         'user': 'Yésica Cortes',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/id/237/200/200'
#     },
#     {
#         'name': 'Khe.',
#         'user': 'Pink Woman',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/id/84/200/200'
#     },
#     {
#         'name': 'Nautural web.',
#         'user': 'Pancho Villa',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/id/784/200/200'
#     },
    
# ]

posts= [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]
# def list_posts(request):
#     # list existing posts
#     content=[]
#     for post in posts:
#         content.append("""
#         <p><strong>{name}</strong</p>
#         <p><small>{user} -<i> {timestamp}</small></p>
#         <figure><img src="{picture}"/></figure>
#         """.format(**post))
#     return HttpResponse('<br>'.join(content))

def list_posts(request):
    return render(request,'feed.html',{'posts':posts})