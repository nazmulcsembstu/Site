from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
     
     dest1 = Destination()
     dest1.name = 'Dhaka'
     dest1.desc = 'The City is beatuful'
     dest1.img = 'destination_7.jpg'
     dest1.price = 5000
     dest1.offer = False
     
     dest2 = Destination()
     dest2.name = 'Pabna'
     dest2.desc = 'The City is awesome'
     dest2.img = 'destination_8.jpg'
     dest2.price = 6000
     dest2.offer = True
     
     dest3 = Destination()
     dest3.name = 'Rajshahi'
     dest3.desc = 'The City is nice'
     dest3.img = 'destination_9.jpg'
     dest3.price = 7000
     dest3.offer = False
     
     dest4 = Destination()
     dest4.name = 'Barishal'
     dest4.desc = 'The City is beatuful'
     dest4.img = 'destination_4.jpg'
     dest4.price = 5000
     dest4.offer = False
     
     dest5 = Destination()
     dest5.name = 'Sylhet'
     dest5.desc = 'The City is awesome'
     dest5.img = 'destination_3.jpg'
     dest5.price = 6000
     dest5.offer = False
     
     dest6 = Destination()
     dest6.name = 'Dinajpur'
     dest6.desc = 'The City is nice'
     dest6.img = 'destination_6.jpg'
     dest6.price = 7000
     dest6.offer = False
     
     dests=[dest1, dest2, dest3, dest4, dest5, dest6]
     
     return render(request, "index.html", {'dests':dests})
    