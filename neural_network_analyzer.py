import openai
import pandas as pd
from config import get_api_key
import streamlit as st

def analyze_data(data, title, x_axis_label, y_axis_label):
    """
    Envia dados e informações do gráfico para análise da I.A..

    Parâmetros:
    data (pd.DataFrame): Dados filtrados.
    title (str): Título do gráfico.
    x_axis_label (str): Rótulo do eixo X.
    y_axis_label (str): Rótulo do eixo Y.

    Retorna:
    str: Análise gerada pela I.A..
    """
    api_key = get_api_key()
    if not api_key:
        raise ValueError("Chave API não configurada. Por favor, configure a chave API na barra lateral.")

    openai.api_key = api_key
    client = openai.OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=api_key,
)

    data_csv = data.to_csv(index=False)

    prompt = f"""
    O gráfico a seguir foi gerado com os seguintes detalhes:
    - Título: {title}
    - Eixo X: {x_axis_label}
    - Eixo Y: {y_axis_label}

    Aqui estão os dados do gráfico:
    {data_csv}

    Por favor, analise esses dados e forneça insights sobre o que eles representam, tendências importantes e quaisquer anomalias notáveis.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um analista de dados."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content.strip()
