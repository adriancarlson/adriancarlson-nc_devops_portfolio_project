from django.shortcuts import render, redirect
from .models import Parishes, Intentions, Meetings
from .forms import ParishesForm, IntentionsForm, MeetingsForm
from .serializers import IntentionsSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view



def home(request):
    intentions = Intentions.objects.all()
    context = {'intentions': intentions}
    return render(request, 'base/home.html', context)



def intention(request, pk):
    intention = Intentions.objects.get(id=pk)
    context = {'intention': intention}
    return render(request, 'base/intention.html', context)

def createIntention(request):
    form = IntentionsForm()

    if request.method == 'POST':
        form = IntentionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/intention_form.html', context)

def updateIntention(request, pk):
    intention = Intentions.objects.get(id=pk)
    form = IntentionsForm(instance=intention)

    if request.method == 'POST':
        form = IntentionsForm(request.POST, instance=intention)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/intention_form.html', context)

def deleteIntention(request, pk):
    intention = Intentions.objects.get(id=pk)
    if request.method == 'POST':
        intention.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': intention})











def parish(request, pk):
    parish = Parishes.objects.get(id=pk)
    context = {'parish': parish}
    return render(request, 'base/parish.html', context)

def meeting(request, pk):
    meeting = Meetings.objects.get(id=pk)
    context = {'meeting': meeting}
    return render(request, 'base/meetings.html', context)






@api_view(['GET', 'POST', 'DELETE'])
def intention_list(request):
    if request.method == 'GET':
        intentions = Intentions.objects.all()

        intention = request.GET.get('intention', None)
        if intention is not None:
            intentions = intentions.filter(intention__icontains=intention)

        intentions_serializer = IntentionsSerializer(intentions, many=True)
        return JsonResponse(intentions_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        intention_data = JSONParser().parse(request)
        intention_serializer = IntentionsSerializer(data=intention_data)
        if intention_serializer.is_valid():
            intention_serializer.save()
            return JsonResponse(intention_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(intention_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Intentions.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Intentions were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def intention_detail(request, pk):
    try:
        intention = Intentions.objects.get(id=pk)
    except intention.DoesNotExist:
        return JsonResponse({'message': 'The intention does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        intention_serializer = IntentionsSerializer(intention)
        return JsonResponse(intention_serializer.data)

    elif request.method == 'PUT':
        intention_data = JSONParser().parse(request)
        intention_serializer = IntentionsSerializer(intention, data=intention_data)
        if intention_serializer.is_valid():
            intention_serializer.save()
            return JsonResponse(intention_serializer.data)
        return JsonResponse(intention_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        intention = Intentions.objects.get(id=pk)
        intention.delete()

        return JsonResponse({'message': 'intention was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
