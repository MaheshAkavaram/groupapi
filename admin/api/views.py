from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import RoomSerializer, MessageSerializer
from .models import Room, Message



"""
def Rooms(request):
    if request.method == "POST":
        name = JSONParser().parse(request)
        v1 = RoomSerializer(data=name)

        if v1.is_valid():
            v1.save()
            return JsonResponse(v1.data, safe=False)
        else:
            return JsonResponse(v1.errors, safe=False)
    elif request.method == "GET":
        data = Room.objects.all()
        output = RoomSerializer(data, many=True)
        return JsonResponse(output.data, safe=False)
"""

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return JsonResponse(request, {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return JsonResponse('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return JsonResponse('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return JsonResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})