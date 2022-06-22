from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from collections import Counter
import os
from django.conf import settings
import string
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
class analysisView(TemplateView):
    template_name = 'analysis/index.html'
    @csrf_exempt
    def get_data(request, format=None):
        folder_path = os.path.join(settings.BASE_DIR, 'analysis')
        #text = open(folder_path+"\\metin.txt", encoding="utf-8").read()
        text=request.POST.get('text')
        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
        tokenized_words = cleaned_text.split()
        final_words = []
        for word in tokenized_words:
            final_words.append(word)
        duygu_list = []
        with open(folder_path+'\\duygu.txt', 'r') as file:
            for line in file: 
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')
                if word in final_words:
                    duygu_list.append(emotion)
        w = Counter(duygu_list)
        return JsonResponse(w,safe=False)