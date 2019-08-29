from django.shortcuts import render

# Create your views here.
def push(request):
    return render(request, 'w14/push.html')


def pull(request):
    print(request.GET)
    number = request.GET.get('number')
    context = {
        'number': number,
    }
    
    return render(request, 'w14/pull.html', context)