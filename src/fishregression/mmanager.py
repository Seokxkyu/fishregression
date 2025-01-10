import os

def get_model_path(model_name):
    my_path = __file__
    dir_name = os.path.dirname(my_path)
    # 모델 파일 경로를 생성
    model_path = os.path.join(dir_name, model_name)
    return model_path
