# Analise Saude SP: Redesenhando a Atenção Básica de São Paulo 🏥

[![Python](https://shields.io)](https://python.org)
[![Pandas](https://shields.io)](https://pydata.org)
[![Streamlit](https://shields.io)](https://streamlit.io)

## 📝 O Problema:

A base regulatória nacional para a atenção básica estabelece a configuração das agendas médicas no formato de **4 consultas por hora (15 minutos por vaga)**. Essa métrica puramente quantitativa gera um ciclo de baixa resolutividade: o retorno constante de pacientes com queixas não sanadas e o aumento direto do risco assistencial. 

Pesquisas globais, como a publicada na revista científica **BMJ Open**, comprovam que um menor tempo de consulta ambulatorial se traduz em maiores taxas de internação hospitalar por condições sensíveis à atenção primária (como complicações controláveis de diabetes e hipertensão). 

Em contrapartida, a **Organização Mundial da Saúde (OMS)** e a **Organização para a Cooperação e Desenvolvimento Econômico (OCDE)** apontam de forma consistente que sistemas públicos de saúde de excelência correlacionam maior densidade médica com consultas mais longas e menor taxa de hospitalizações desnecessárias.

### O Contexto Operacional de São Paulo
O problema central que contribui para a precarização da saúde pública na atenção básica da capital paulista é o **baixo indicador de médicos por habitante, concentrado sobretudo nas regiões periféricas**. 

Para evitar penalidades contratuais e descontos nos repasses financeiros feitos pela Secretaria Municipal da Saúde (SMS), as Organizações Sociais de Saúde (OSS) — empresas terceirizadas que gerenciam as unidades — forçam a atenção básica a operar sob uma lógica industrial. O foco passa a ser o atendimento em massa para o cumprimento estrito de metas de produção, atropelando métricas cruciais de qualidade, como a resolutividade e o tempo de escuta qualificada.

**Este projeto demonstra que o redesenho da densidade de médicos por habitante não é apenas um ganho laboral para a categoria, mas a chave regulatória indispensável para alinhar o SUS paulistano aos padrões de excelência recomendados pela OMS.**

---

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
