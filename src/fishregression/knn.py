import pickle
from mmanager import get_model_path

def knn_api(length, weight):
    # 모델 파일 경로 가져오기
    model_path = get_model_path('knn_model.pkl')

    # 모델 로드
    with open(model_path, 'rb') as f:
        knn_model = pickle.load(f)

    # 예측
    pred = knn_model.predict([[length, weight]])

    if pred[0] == 1:
        return "도미"
    return "빙어"
