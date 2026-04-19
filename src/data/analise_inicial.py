import pandas as pd
import os

'''Function in order to define the consult time by its different types'''

def set_time(proc):
    if pd.isna(proc): 
        return 0
    if '0301010072' in proc: 
        return 15  # Vaga atendimento comum
    if any(cod in proc for cod in ['0301010269', '0301010277', '0301010110', '0301010137']):
        return 30  # Puerpério/RN/Pré-natal
    return 0

'''CSV document Path shortnames'''
file_path_doc_nur = '/mnt/harddisk/analise_saudepublica_SP/data/raw/saude_med_enf_mun_ano.csv'

file_path_health_consult_per_type = '/mnt/harddisk/analise_saudepublica_SP/data/raw/atendimento_por_tipo_2023_01_04.csv'


try:
    #Dataframe of Docs and Nurses numbers per city
    df_doc_nur= pd.read_csv(file_path_doc_nur, sep = ';', encoding = 'latin-1')

    #Dataframe of the medical consult numbers grouped by consult type in São Paulo city
    df_consult = pd.read_csv(file_path_health_consult_per_type, sep=';', encoding='latin-1', skiprows=3)

    #Excluding predesigned table format

    df_consult= df_consult[df_consult['Procedimento'].str.contains('Total') == False]


    df_consult['tempo_vaga'] = df_consult['Procedimento'].apply(set_time)

    df_analysis = df_consult[df_consult['tempo_vaga'] > 0].copy()

    print("--- Script executado com sucesso ---")
    print(df_analysis[['Procedimento', 'tempo_vaga']].head())

    print("\n--- Doctor and Nurse per city ---")
    print(df_doc_nur['mun'].value_counts())
    df_doc_nur['pct_sus'] = (df_doc_nur['prof_sus'] / df_doc_nur['prof_tot']) * 100

    
except Exception as e:
    print(f"Erro na execução: {e}") 