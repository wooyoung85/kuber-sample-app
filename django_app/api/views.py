from analysis.serializers import AnalysisSerializer
from django.http import JsonResponse
from analysis.tasks import sentence_analysis

def analysis(request):
    data = {}
    sentence = request.GET['sentence']
    task = sentence_analysis.delay(sentence)
    polarity = task.wait(timeout=None, propagate=True)
    data['sentence'] = sentence
    data['polarity'] = polarity
    
    serializer = AnalysisSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(data)