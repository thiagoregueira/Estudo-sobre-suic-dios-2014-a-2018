# importando as bibliotecas necessárias
import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st


# função para conectar ao banco de dados SQLite
def load_data():
    conn = sqlite3.connect("suicidios_tratado.db")
    df = pd.read_sql_query("SELECT * FROM suicidios_tratado", conn)
    conn.close()
    return df


# main
def main():
    # configurações da página
    st.set_page_config(
        page_title="Tendência ao longo do tempo", page_icon="📊", layout="wide"
    )

    st.title("2. Tendência ao longo do tempo")

    # carregar dados
    df = load_data()

    # df da tendencia ao longo do tempo
    df_tempo = df.groupby("ano_obito").count()["uf_obito"].reset_index()
    df_tempo = df_tempo.reset_index().rename(columns={"uf_obito": "qtd_obitos"})

    # criando o gráfico de linha para visualizar as mudanças ao longo do tempo
    fig1 = px.line(
        df_tempo,
        x="ano_obito",
        y="qtd_obitos",
        title="Evolução dos suicídios no Brasil",
        markers=True,
        template="ggplot2",
        text="qtd_obitos",
    )
    # centralizar o titulo
    fig1.update_layout(title_x=0.5)

    # adicionando rótulos aos marcadores
    fig1.update_traces(textposition="top center")

    fig1.update_layout(
        xaxis_title="Ano",
        yaxis_title="Quantidade de óbitos",
        font=dict(size=12, color="#000000"),
    )
    # eixo x com intervalo de 1 ano
    fig1.update_xaxes(dtick=1)

    # exibindo o gráfico no streamlit
    st.plotly_chart(fig1, use_container_width=True)

    # escrevendo a conclusão em markdown
    st.markdown(
        """
        #### Conclusão 1:

        De acordo com o gráfico, o número de suicídios no Brasil tem aumentado ao longo do tempo.

        Em 2014, houve aproximadamente 4.893 suicídios.
        Em 2015, o número aumentou para 5.328.
        Em 2016, houve 5.749 suicídios.
        Em 2017, o número aumentou novamente para 6.544.
        Finalmente, em 2018, houve 6.969 suicídios.

        Portanto, a tendência geral é de um aumento no número de suicídios no Brasil de 2014 a 2018."""
    )


# iniciação da aplicação
if __name__ == "__main__":
    main()
