import pickle
import numpy as np
from mmanager import get_model_path

def lr_api(length):
    # 모델 파일 경로 가져오기
    model_path = get_model_path('lr_model.pkl')

    # 모델 로드
    with open(model_path, 'rb') as f:
        lr_model = pickle.load(f)

    # 다항 회귀를 위한 2차 항 추가
    length_poly = np.array([length**2, length]).reshape(1, -1)

    # 예측
    predicted_weight = lr_model.predict(length_poly)
    return predicted_weight[0]
