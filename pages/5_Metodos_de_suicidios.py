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
    st.set_page_config(page_title="Metodos de Suicídios", page_icon="☠️", layout="wide")

    st.title("5. Metodos de Suicidios")

    # carregar dados
    df = load_data()

    # suicidios por causas_basicas_obito
    df_causa = df.groupby("causas_basicas_obito").count()["uf_obito"]

    # renomeando as colunas de df_causa
    df_causa = (
        df_causa.reset_index()
        .rename(columns={"uf_obito": "qtd_obitos"})
        .sort_values(ascending=False, by="qtd_obitos")
    )

    # representando os valores da coluna causas_basicas_obito em porcentagem
    df_causa["porcentagem"] = (
        df_causa["qtd_obitos"] / df_causa["qtd_obitos"].sum()
    ) * 100

    # arredondando os valores da coluna porcentagem
    df_causa["porcentagem"] = df_causa["porcentagem"].round(2)

    # grafico de barras com as maiores causas de obitos
    fig_causa = px.bar(
        df_causa.head(10),
        x="causas_basicas_obito",
        y="qtd_obitos",
        title="Maiores causas de óbitos por suicídio",
        template="ggplot2",
        text="porcentagem",
    )

    # nomeando os eixos
    fig_causa.update_layout(
        xaxis_title="Causas básicas de óbito",
        yaxis_title="Quantidade de óbitos (%)",
        font=dict(size=12, color="#000000"),
    )

    # centralizando o titulo
    fig_causa.update_layout(title_x=0.5)

    # exibindo o grafico
    st.plotly_chart(fig_causa, use_container_width=True)

    # concluindo
    st.markdown(
        """
            ### Conclusão 10:

            Com base no gráfico obtido, podemos observar as seguintes tendências nos métodos de suicídio ao longo do tempo:

            - **Diferenças significativas entre métodos**: Existem diferenças notáveis nos métodos de suicídio ao longo do tempo. Por exemplo, o X700 tem sido consistentemente o método mais comum de suicídio em todos os anos observados.

            - **X700**: Este método tem sido consistentemente o mais comum em todos os anos, correspondendo a mais de 50% dos casos de suicídio de 2014 a 2018. Isso pode ser devido a vários fatores, como o acesso a meios letais, a facilidade de uso e a eficácia.

            Breve descrição do método X700: O código X700 na Classificação Internacional de Doenças (CID 10) refere-se a uma lesão autoinfligida intencionalmente causada por enforcamento, estrangulamento e sufocação em casa.
        """
    )


# chamando a função main
if __name__ == "__main__":
    main()
