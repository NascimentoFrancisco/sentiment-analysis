from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from models_ai.classifier.get_models import ModelsSentimentAnalysis

class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class SearchSentimentAnalysis(View):


    def post(self, request, **kwargs):
        
        response = dict()

        if request.method == 'POST':
            if request.POST['text']:
                
                response['text'] = request.POST['text']
                models = ModelsSentimentAnalysis()

                if request.POST['algorithm'] == 'Naive bayes':
                    
                    model = models.classifier_model_Naive_Bayes()
                    response['algorithm'] = 'Naive bayes'
                
                elif request.POST['algorithm'] == 'Regressão logística':

                    model = models.classifier_model_logistic_regression()
                    response['algorithm'] = 'Regressão logística'

                else:

                    messages.warning(request, f'Escolha um dos algoritmos!')

                    return render(request, 'home.html',response)

                text = models.vectorizer_transform([request.POST['text']])
                result = model.predict(text)

                if result[0] == 0:
                
                    response['sentiment'] = 'Negativo'
                    response['option'] = False

                else:
                
                    response['sentiment'] = 'Positivo'
                    response['option'] = True
            else:
                messages.warning(request, 
                    f'Digite alguma frase no formulário!'
                )
            return render(request, 'home.html',response)

        return render(request, 'home.html',response)
