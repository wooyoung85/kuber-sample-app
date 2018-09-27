from rest_framework import serializers 
from .models import Analysis 

class AnalysisSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Analysis # 모델 설정 
        fields = ('sentence','polarity') # 필드 설정
