import pickle


class ModelsSentimentAnalysis:


    def __init__(self):

        self.classifier_model_logistic_regression()
        self.classifier_model_Naive_Bayes()
        self.get_vectorizer()


    def classifier_model_logistic_regression(self):

        model = pickle.load(open('models_ai/binary_files/model_rg.pkl','rb'))
        return model
    

    def classifier_model_Naive_Bayes(self):

        model = pickle.load(open('models_ai/binary_files/model_by.pkl','rb'))
        return model
    

    def get_vectorizer(self):

        vectorizer = pickle.load(open('models_ai/binary_files/vectorizer.pkl','rb'))
        return vectorizer
    

