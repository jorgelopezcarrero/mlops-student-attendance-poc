import pandas as pd
import numpy as np
import os

def load_and_transform_data():
    os.makedirs("data", exist_ok=True)
    
    # 1. Generación de dataset sintético (300 estudiantes)
    np.random.seed(42)
    n_samples = 300

    df = pd.DataFrame({
        'alumno': [f'Estudiante_{i}' for i in range(n_samples)],
        'clima': np.random.choice(['Soleado', 'Lluvioso'], size=n_samples, p=[0.7, 0.3]),
        'materia': np.random.choice(['Matemática', 'Biología', 'Física', 'Literatura', 'Castellano'], size=n_samples),
        'nota_promedio': np.round(np.random.uniform(4.0, 10.0, size=n_samples), 1),
        'faltas_mes': np.random.poisson(lam=2, size=n_samples)
    })
    
    # 2. Lógica para definir la etiqueta 'asistio' (Target)
    def define_target(row):
        if row['clima'] == 'Lluvioso' and row['faltas_mes'] > 3:
            return 0
        elif row['nota_promedio'] >= 7.0 and row['faltas_mes'] <= 2:
            return 1
        else:
            return np.random.choice([0, 1], p=[0.4, 0.6])

    df['asistio'] = df.apply(define_target, axis=1)

    # 3. Transformaciones (Encoding)
    df['es_lluvioso'] = df['clima'].apply(lambda x: 1 if x == "Lluvioso" else 0)
    df['materia_humanidades'] = df['materia'].apply(lambda x: 1 if x in ["Literatura", "Castellano"] else 0)
    
    # 4. Guardar dataset procesado
    output_path = "data/processed_data.parquet"
    df.to_parquet(output_path, index=False)
    print(f"Pipeline de datos completado exitosamente -> Generados {len(df)} registros en {output_path}")

if __name__ == "__main__":
    load_and_transform_data()
