# importando as bibliotecas necessárias
import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st


# função para conectar ao banco de dados SQLite
@st.cache_data
def load_data():
    conn = sqlite3.connect("suicidios_tratado.db")
    df = pd.read_sql_query("SELECT * FROM suicidios_tratado", conn)
    conn.close()
    return df


# main
def main():
    # configurações da página
    st.set_page_config(
        page_title="Localização geográfica", page_icon="🗺️", layout="wide"
    )

    st.title("4. Localização geográfica")

    # carregar dados
    df = load_data()

    # suicidios por uf_obito
    df_uf = df.groupby("uf_obito").count()["idade"]

    # renomeando as colunas de df_uf
    df_uf = (
        df_uf.reset_index()
        .rename(columns={"idade": "qtd_obitos"})
        .sort_values(ascending=True, by="qtd_obitos")
    )

    # criando um grafico de barras horizontais
    fig_loc = px.bar(
        df_uf,
        x="qtd_obitos",
        y="uf_obito",
        orientation="h",
        title="Quantidade de obitos por UF (Todo o período)",
        template="ggplot2",
        text="qtd_obitos",
        height=800,
    )

    # nomeando os eixos
    fig_loc.update_layout(
        xaxis_title="Quantidade de óbitos",
        yaxis_title="UF",
        font=dict(size=12, color="#000000"),
    )

    # centralizando o titulo
    fig_loc.update_layout(title_x=0.5)

    # exibindo o gráfico
    st.plotly_chart(fig_loc, use_container_width=True)

    # suicidios por uf e ano
    df_uf_ano = df.groupby(["uf_obito", "ano_obito"]).count()["idade"]

    # renomeando as colunas de df_uf_ano
    df_uf_ano = (
        df_uf_ano.reset_index()
        .rename(columns={"idade": "qtd_obitos"})
        .sort_values(ascending=True, by="qtd_obitos")
    )

    # Cria o gráfico de linha
    fig_loc2 = px.bar(
        df_uf_ano,
        x="ano_obito",
        y="qtd_obitos",
        color="uf_obito",
        title="Óbitos por Suicídio no Brasil por UF e Ano",
        template="ggplot2",
    )

    # nomeando os eixos
    fig_loc2.update_layout(
        xaxis_title="Ano",
        yaxis_title="Quantidade de óbitos",
        font=dict(size=12, color="#000000"),
    )

    # centralizando o titulo
    fig_loc2.update_layout(title_x=0.5)

    # exibindo o gráfico
    st.plotly_chart(fig_loc2, use_container_width=True)

    # escrevendo a conclusão em markdown
    st.markdown(
        """
        ### Conclusão 9:

        Com base no gráfico obtido, podemos observar as seguintes tendências nas quantidades de suicídio entre diferentes localidades ao longo do tempo:

        - **Diferenças significativas entre localidades**: Existem diferenças notáveis nas quantidades de suicídio entre diferentes localidades ao longo do tempo. Por exemplo, São Paulo (SP) tem um número significativamente maior de óbitos por suicídio do que Roraima (RR) em todos os anos observados.

        - **São Paulo (SP)**: Esta unidade federativa tem a maior quantidade de óbitos em todos os anos, com um pico de 1.069 casos em 2018. Isso pode ser devido a vários fatores, como o tamanho da população, o status socioeconômico, o acesso a serviços de saúde mental, entre outros.

        - **Roraima (RR)**: Esta unidade federativa tem a menor quantidade de óbitos em todos os anos, com um pico de 7 casos em 2018. Isso pode ser devido a uma população menor, diferentes fatores socioeconômicos, ou uma variedade de outras possíveis razões.

        - **Outras unidades federativas**: As outras unidades federativas apresentam números variados de óbitos por suicídio ao longo do tempo, indicando que a taxa de suicídio pode variar significativamente de uma localidade para outra e ao longo do tempo.

        Essas tendências sugerem que as taxas de suicídio podem variar significativamente entre diferentes localidades e ao longo do tempo.
    """
    )


# executando a função main
if __name__ == "__main__":
    main()
