"""platzigram views"""
#Django
from django.http import HttpResponse

#utilities
from datetime import datetime
import json
def hello_world(request):
    now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f"Hello world bitches xD the time is {str(now)}")


def sort_integers(request):
    print(request)
    #mport pdb; pdb.set_trace()
    numbers=request.GET['numbers']
    numbers=list(map(int,numbers.split(',')))
    numbers.sort()
    data={
        'status':'ok',
        'numbers': numbers,
        'message':'Integer sort succesfully'
    }
    #return HttpResponse('hi numbers =[' +str(numbers)+']')
    return HttpResponse(json.dumps(data,indent=4),content_type='application/json')


def say_hi(request,name,age):
    #"return a greeting"
    if age<12:
        message= 'Sorry {},you are not alloewd'.format(name)
    else:
        message= ' yeah {}, you are avaliable to this site'.format(name)
        
    return HttpResponse(message)