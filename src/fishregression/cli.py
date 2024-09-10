from fishregression.lr import lr_api
from fishregression.knn import knn_api
import requests

def predict():
    # 사용자 입력을 바로 받음
    length = float(input("🐟 물고기의 길이를 입력하세요: "))

    # weight 예측 선형회귀 API 호출
    weight = lr_api(length)

    # 물고기 분류 API 호출
    fish_class = knn_api(length, weight)

    print(f"🐟 length가 {length}인 물고기의 weight는 {weight}으로 예측되며, 종류는 '{fish_class}' 입니다.")


