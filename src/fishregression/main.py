from typing import Union
from fishregression.api.lr import lr_api
from fishregression.api.knn import knn_api
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Fish Regressor"}

@app.get("/lr")
def read_item(l: float):
    """
    물고기의 무게 예측

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        dict:
          weight (float): 물고기 무게(g)
    """
    length_poly = np.array([l**2, l]).reshape(1, -1)
    weight = lr_api(length_poly)
    return {"weight": weight}

@app.get("/knn")
def read_item(w: float, l: float):
    fish_class = knn_api(l, w)
    result_msg = f"🐟 길이 {l}에 무게 {w}인 물고기는 {fish_class}로 예측됩니다!"
    return {"result": result_msg}


'''
@app.get("/fish")
def fish(length: float):
    """
    물고기의 무게 예측

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        dict:
          weight (float): 물고기 무게(g)
          length (float): 물고기 길이(cm)
    """
    fish_weight = run_prediction(length)

    return {
                "length": length, 
                "weight": fish_weight
            }
'''
