import pandas as pd
import os

file_path = '/mnt/harddisk/analise_saudepublica_SP/data/raw/saude_med_enf_mun_ano.csv'

try:
    df = pd.read_csv(file_path, sep = ';', encoding = 'latin-1')

    print ("--- Primeiras 5 linhas do arquivo---")
    print(df.head())

    print("\n--- Médicos e Enfermeiros por Município ---")
    print(df['mun'].value_counts())
    df['pct_sus'] = (df['prof_sus'] / df['prof_tot']) * 100

except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")