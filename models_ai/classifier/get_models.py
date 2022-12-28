import pickle


class ModelsSentimentAnalysis:


    def __init__(self):

        self.vectorizer = pickle.load(open('models_ai/binary_files/vectorizer.pkl','rb'))
        self.model_bayesian = pickle.load(open('models_ai/binary_files/model_by.pkl','rb'))
        self.model_logistic_regression = pickle.load(open('models_ai/binary_files/model_rg.pkl','rb'))

    def classifier_model_logistic_regression(self):

        return self.model_logistic_regression
    

    def classifier_model_Naive_Bayes(self):

        return self.model_bayesian
    

    def get_vectorizer(self):

        return self.vectorizer
    
    
    def vectorizer_transform(self,text:list):

        return self.vectorizer.transform(text)

