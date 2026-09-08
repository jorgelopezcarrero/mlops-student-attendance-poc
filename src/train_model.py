import pandas as pd

def predict_attendance(row):
    if row['es_lluvioso'] == 1:
        if row['faltas_mes'] > 3:
            return 0
        else:
            return 1 if row['nota_promedio'] > 8.5 else 0
    else:
        if row['nota_promedio'] >= 8.0 and row['faltas_mes'] <= 2:
            return 1
        else:
            return 0 if row['materia_humanidades'] == 1 else 1

def run_predictions():
    df = pd.read_parquet("data/processed_data.parquet")
    df['prediccion'] = df.apply(predict_attendance, axis=1)
    
    accuracy = (df['asistio'] == df['prediccion']).mean() * 100
    print(f"Modelo evaluado. Precisión obtenida: {accuracy:.2f}%")
    return accuracy

if __name__ == "__main__":
    run_predictions()
