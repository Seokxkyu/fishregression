import pickle
from sklearn.neighbors import KNeighborsClassifier

def knn_api(length, weight):
    with open(file='/home/kyuseok00/code/fishregression/note/knn_model.pkl', mode='rb') as f:
        fish = pickle.load(f)
    
    pred = fish.predict([[length, weight]])
    
    if pred[0] == 0:
        return "도미"
    return "빙어"
