from django.shortcuts import render
from leads.models import Leads
from leads.serializers import LeadSerializer
from rest_framework import generics

# Create your views here.
class LeadListCreate(generics.ListCreateAPIView):
  queryset = Leads.objects.all()
  serializer_class = LeadSerializer