from fishregression.mmanager import get_model_path
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

def lr_api(length):
    # path = get_model_path()

    # with open(file=path, mode='rb') as f:
    #    lr = pickle.load(f)

    # lr 모델 경로 수정
    with open(file='/home/kyuseok00/code/fishregression/note/lr_model.pkl', mode='rb') as f:
        lr_model = pickle.load(f)

    # 2차 항이 포함된 데이터 생성 (길이의 제곱, 길이)
    length_poly = np.array([length**2, length]).reshape(1, -1)

    # 선형 회귀 모델로 무게 예측
    predicted_weight = lr_model.predict(length_poly)
    return predicted_weight[0]
