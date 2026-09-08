import pandas as pd
from src.train_model import predict_attendance

def test_predict_attendance():
    case_1 = pd.Series({'es_lluvioso': 0, 'faltas_mes': 1, 'nota_promedio': 9.0, 'materia_humanidades': 0})
    assert predict_attendance(case_1) == 1

    case_2 = pd.Series({'es_lluvioso': 1, 'faltas_mes': 4, 'nota_promedio': 7.5, 'materia_humanidades': 0})
    assert predict_attendance(case_2) == 0
