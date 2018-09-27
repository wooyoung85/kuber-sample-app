from rest_framework import viewsets 
from .serializers import AnalysisSerializer 
from .models import Analysis 

class AnalysisViewSet(viewsets.ModelViewSet): 
    queryset = Analysis.objects.all() 
    serializer_class = AnalysisSerializer
