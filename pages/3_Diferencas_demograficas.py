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
        page_title="Diferenças demográficas", page_icon="📊", layout="wide"
    )

    st.title("3. Diferenças demográficas")

    # carregar dados
    df = load_data()

    st.markdown("#### Homens x Mulheres")

    # quantidade de obitos por sexo e ano
    df_tempo_sexo = df.groupby(["ano_obito", "sexo"]).count()["uf_obito"]
    df_tempo_sexo = df_tempo_sexo.reset_index().rename(
        columns={"uf_obito": "qtd_obitos"}
    )

    # separando os homens
    df_homens = df_tempo_sexo[df_tempo_sexo["sexo"] == "Masculino"]

    # separando as mulheres
    df_mulheres = df_tempo_sexo[df_tempo_sexo["sexo"] == "Feminino"]

    # criando 2 colunas para exibição dos gráficos lado a lado
    col1, col2 = st.columns(2)

    # criando o gráfico de linha dos homens
    fig_homem = px.line(
        df_homens,
        x="ano_obito",
        y="qtd_obitos",
        title="Evolução dos suicídios no Brasil, Homens",
        markers=True,
        template="ggplot2",
        text="qtd_obitos",
    )

    # posição do texto
    fig_homem.update_traces(textposition="top center")

    fig_homem.update_layout(
        xaxis_title="Ano",
        yaxis_title="Quantidade de óbitos",
        font=dict(size=12, color="#000000"),
    )

    # centralizar o titulo
    fig_homem.update_layout(title_x=0.5)

    # eixo x com intervalo de 1 ano
    fig_homem.update_xaxes(dtick=1)

    # mudar cor da linha
    fig_homem.update_traces(line_color="blue")

    # adicionando o grafico na coluna 1
    col1.plotly_chart(fig_homem, use_container_width=True)

    # criando o gráfico de linha das mulheres
    fig_mulher = px.line(
        df_mulheres,
        x="ano_obito",
        y="qtd_obitos",
        title="Evolução dos suicídios no Brasil, Mulheres",
        markers=True,
        template="ggplot2",
        text="qtd_obitos",
    )

    # posição do texto
    fig_mulher.update_traces(textposition="top center")

    fig_mulher.update_layout(
        xaxis_title="Ano",
        yaxis_title="Quantidade de óbitos",
        font=dict(size=12, color="#000000"),
    )

    # centralizar o titulo
    fig_mulher.update_layout(title_x=0.5)

    # eixo x com intervalo de 1 ano
    fig_mulher.update_xaxes(dtick=1)

    # mudar cor da linha
    fig_mulher.update_traces(line_color="blue")

    # mudando a cor da linha
    fig_mulher.update_traces(line_color="pink")

    # adicionando o grafico na coluna 2
    col2.plotly_chart(fig_mulher, use_container_width=True)

    # grafico de ambos para comparação
    fig_ambos = px.line(
        df_tempo_sexo,
        x="ano_obito",
        y="qtd_obitos",
        color="sexo",
        title="Evolução dos suicídios no Brasil por sexo",
        markers=True,
        template="ggplot2",
        text="qtd_obitos",
    )

    # adicionando nomes aos eixos
    fig_ambos.update_layout(
        xaxis_title="Ano",
        yaxis_title="Quantidade de óbitos",
        font=dict(size=12, color="#000000"),
    )

    # centralizar o titulo
    fig_ambos.update_layout(title_x=0.5)

    # alterar cor da linha Masculino e Feminino
    fig_ambos.update_traces(line_color="blue", selector=dict(name="Masculino"))
    fig_ambos.update_traces(line_color="pink", selector=dict(name="Feminino"))

    # posição do texto
    fig_ambos.update_traces(textposition="top center")
    # eixo x com intervalo de 1 ano
    fig_ambos.update_xaxes(dtick=1)

    # adicionando o grafico ao streamlit
    st.plotly_chart(fig_ambos, use_container_width=True)

    # adicionando a conclusão ao streamlit
    st.markdown(
        """
        #### Conclusão 2:

        De acordo com os gráficos, há diferenças significativas nas taxas de suicídio entre homens e mulheres no Brasil de 2014 a 2018. Aqui estão algumas observações baseadas nos dados:

        - **Taxas mais altas entre os homens**: Em todos os anos, o número de suicídios entre os homens é consistentemente maior do que entre as mulheres. Por exemplo, em 2018, houve 5.370 suicídios entre os homens, em comparação com 1.599 entre as mulheres.

        - **Aumento ao longo do tempo**: Ambos os sexos mostram um aumento no número de suicídios ao longo do tempo. No entanto, o aumento é mais acentuado entre os homens. Por exemplo, o número de suicídios entre os homens aumentou de 3.801 em 2014 para 5.370 em 2018. Entre as mulheres, o número aumentou de 1.092 em 2014 para 1.599 em 2018.

        Essas tendências sugerem que, embora as taxas de suicídio estejam aumentando para ambos os sexos, os homens estão em maior risco.
        """
    )

    st.markdown(
        """
        ### Suicídios por idade
        """
    )

    # quantidade de obitos por idade
    df_idade = df.groupby("idade").count()["uf_obito"]
    df_idade = df_idade.reset_index().rename(columns={"uf_obito": "qtd_obitos"})
    df_idade["idade"] = df_idade["idade"].abs()

    # criando faixas de idades
    df_idade["faixa_etaria"] = pd.cut(
        df_idade["idade"],
        bins=[0, 9, 19, 29, 39, 49, 59, 69],
        labels=[
            "0 a 9",
            "10 a 19",
            "20 a 29",
            "30 a 39",
            "40 a 49",
            "50 a 59",
            "60 a 69",
        ],
    )

    df_faixa = df_idade.groupby("faixa_etaria").sum()["qtd_obitos"].reset_index()

    # grafico de barras com as faixas de idades
    fig_idade = px.bar(
        df_faixa,
        x="faixa_etaria",
        y="qtd_obitos",
        title="Quantidade de óbitos por faixa etária",
        template="ggplot2",
        text="qtd_obitos",
    )

    # nomeando os eixos
    fig_idade.update_layout(
        xaxis_title="Faixa etária",
        yaxis_title="Quantidade de óbitos",
        font=dict(size=12, color="#000000"),
    )

    # centralizar o titulo
    fig_idade.update_layout(title_x=0.5)

    # adicionando ao streamlit
    st.plotly_chart(fig_idade, use_container_width=True)

    # adicionando a conclusão ao streamlit
    st.markdown(
        """
        #### Conclusão 3:
        
        Com base no gráfico, podemos observar as seguintes tendências nos casos de suicídio em relação às diferentes faixas etárias:

        - **Faixa etária de 0 a 9 anos**: Esta faixa etária tem a menor quantidade de óbitos, com 80 casos registrados. Isso pode ser devido à menor exposição a fatores de risco para o suicídio nessa idade.

        - **Faixa etária de 10 a 19 anos**: Há um aumento significativo na quantidade de óbitos nesta faixa etária, com 2.862 casos. Isso pode ser atribuído a uma variedade de fatores, incluindo o início da puberdade e o aumento das pressões sociais e acadêmicas.

        - **Faixa etária de 20 a 29 anos**: Esta faixa etária tem a maior quantidade de óbitos, com 7.375 casos. Isso pode ser devido a uma combinação de fatores, incluindo o estresse associado à transição para a vida adulta e o início de carreiras profissionais.

        - **Faixa etária de 30 a 39 anos**: A quantidade de óbitos nesta faixa etária é quase igual à faixa etária de 20 a 29 anos, com 7.205 casos. Isso pode ser devido a fatores como estresse no trabalho, problemas financeiros e questões familiares.

        - **Faixa etária de 40 a 49 anos**: Há uma diminuição na quantidade de óbitos nesta faixa etária, com 5.402 casos. No entanto, o número ainda é significativamente alto.

        - **Faixa etária de 50 a 59 anos**: A quantidade de óbitos continua a diminuir nesta faixa etária, com 4.536 casos.

        - **Faixa etária de 60 a 69 anos**: Esta faixa etária tem uma quantidade significativamente menor de óbitos, com 2.121 casos. Isso pode ser devido a uma variedade de fatores, incluindo aposentadoria e mudanças no estilo de vida.

        Essas tendências sugerem que as taxas de suicídio variam significativamente entre diferentes faixas etárias. Se destacando os números das faixas de 20 a 39, onde os jovens passam a ter mais responsabilidades e pressões sociais.
        """
    )

    st.markdown(
        """
        ### Suicídios x Nível de escolaridade
    """
    )

    # suicidios por nivel de escolaridade
    df_escolaridade = df.groupby("escolaridade").count()["uf_obito"]

    # renomeando as colunas de df_escolaridade
    df_escolaridade = df_escolaridade.reset_index().rename(
        columns={"uf_obito": "qtd_obitos"}
    )

    # criando o grafico de barra
    fig_escolaridade = px.bar(
        df_escolaridade,
        x="escolaridade",
        y="qtd_obitos",
        title="Quantidade de óbitos por nível de escolaridade",
        template="ggplot2",
        text="qtd_obitos",
    )

    # nomeando os eixos
    fig_escolaridade.update_layout(
        xaxis_title="Nível de escolaridade",
        yaxis_title="Quantidade de óbitos",
        font=dict(size=12, color="#000000"),
    )

    # centralizar o titulo
    fig_escolaridade.update_layout(title_x=0.5)

    # adicionando ao streamlit
    st.plotly_chart(fig_escolaridade, use_container_width=True)

    # concluindo
    st.markdown(
        """
        #### Conclusão 4:

        Com base no gráfico obtido, podemos observar as seguintes tendências nas quantidades de suicídio entre diferentes grupos demográficos em relação às diferentes níveis de escolaridade:

        - **Nenhuma escolaridade**: Este grupo tem a menor quantidade de óbitos, com 1.731 casos. Isso pode ser devido a uma variedade de fatores, incluindo a idade (pessoas muito jovens que ainda não começaram a escola) e o acesso limitado a meios letais.

        - **Educação infantil**: Há um aumento significativo na quantidade de óbitos neste grupo, com 5.096 casos. Isso pode ser atribuído a uma variedade de fatores, incluindo o início da puberdade e o aumento das pressões sociais e acadêmicas.

        - **Ensino fundamental**: Este grupo tem uma quantidade ainda maior de óbitos, com 9.529 casos. Isso pode ser devido a uma combinação de fatores, incluindo o estresse associado à transição para a adolescência e o início de problemas de saúde mental.

        - **Ensino médio**: Este grupo tem a maior quantidade de óbitos, com 9.755 casos. Isso pode ser devido a fatores como estresse no trabalho, problemas financeiros e questões familiares.

        - **Graduação**: Há uma diminuição na quantidade de óbitos neste grupo, com 3.472 casos. Isso pode ser devido a uma variedade de fatores, incluindo maior estabilidade financeira, melhor acesso a serviços de saúde mental e maior resiliência ao estresse.

        Essas tendências sugerem que as quantidades de suicídio variam significativamente entre diferentes níveis de escolaridade.
    """
    )

    st.markdown(
        """
        ### Suicídios x Ocupação
        """
    )

    # suicidios por ocupacao
    df_ocupacao = df.groupby("ocupacao").count()["uf_obito"]

    # renomeando as colunas de df_ocupacao
    df_ocupacao = df_ocupacao.reset_index().rename(columns={"uf_obito": "qtd_obitos"})

    # ordenando os valores e mostrando os 10 primeiros
    df_ocupacao_top10 = df_ocupacao.sort_values(ascending=False, by="qtd_obitos").head(
        10
    )

    # grafico treemap com as ocupações com mais suicidios

    fig_ocupacao = px.treemap(
        df_ocupacao_top10,
        path=["ocupacao"],
        values="qtd_obitos",
        color="qtd_obitos",
        hover_data=["ocupacao"],
        color_continuous_scale="RdBu",
        title="Quantidade de óbitos por ocupação",
        template="ggplot2",
    )

    # centralizando o titulo
    fig_ocupacao.update_layout(title_x=0.5)

    # mostrando o grafico
    st.plotly_chart(fig_ocupacao, use_container_width=True)

    # concluindo
    st.markdown(
        """
        ### Conclusão 5:

        Com base no gráfico obtido, podemos observar as seguintes tendências nas quantidades de suicídio entre diferentes grupos demográficos em relação às diferentes ocupações:

        -**Distribuição dos Óbitos**: A ocupação com o maior número de óbitos é “Sem Ocupação”, seguida por “Estudante” e “Aposentado/Pensionista”. Isso pode indicar que essas ocupações têm maior risco de óbito, ou simplesmente que há mais pessoas nessas ocupações.
    """
    )

    st.markdown("""### Suicídios x Raça""")

    # suicidios por raca
    df_raca = df.groupby("raca").count()["uf_obito"]

    # renomeando as colunas de df_raca
    df_raca = df_raca.reset_index().rename(columns={"uf_obito": "qtd_obitos"})

    df_raca = df_raca.sort_values(ascending=False, by="qtd_obitos")

    # criando o grafico de pizza
    fig_raca = px.pie(
        df_raca,
        values="qtd_obitos",
        names="raca",
        title="Quantidade de óbitos por raça/cor",
        template="ggplot2",
    )

    # centralizando o titulo
    fig_raca.update_layout(title_x=0.5)

    # mostrando o grafico
    st.plotly_chart(fig_raca, use_container_width=True)

    # concluindo
    st.markdown(
        """
        ### Conclusão 6:

        **Distribuição de Óbitos por Raça**: O gráfico mostra que a maioria dos óbitos ocorre entre as raças Branca e Parda, que juntas representam mais de 90% dos óbitos. Isso pode indicar que essas raças têm maior risco de óbito, ou simplesmente que há mais pessoas dessas raças na população.
        """
    )

    st.markdown("""### Suicídios x Estado Civil""")

    # suicidios por estado_civil
    df_estado_civil = df.groupby("estado_civil").count()["idade"]

    # renomeando as colunas de df_estado_civil
    df_estado_civil = df_estado_civil.reset_index().rename(
        columns={"idade": "qtd_obitos"}
    )

    df_estado_civil = df_estado_civil.sort_values(ascending=False, by="qtd_obitos")

    # grafico de rosca
    fig_estado_civil = px.pie(
        df_estado_civil,
        values="qtd_obitos",
        names="estado_civil",
        title="Quantidade de óbitos por estado civil",
        template="seaborn",
        hole=0.6,
    )

    # centralizando o titulo
    fig_estado_civil.update_layout(title_x=0.5)

    # mostrando o grafico
    st.plotly_chart(fig_estado_civil, use_container_width=True)

    # concluindo
    st.markdown(
        """
        ### Conclusão 7:

        **Distribuição de Óbitos por Estado Civil**: O gráfico mostra que a maioria dos óbitos ocorre entre as pessoas solteiras, que representam mais de 50% dos óbitos. Mas quando somamos os solteiro e casados temos mais de 70% dos óbitos. Isso pode indicar que esses estados civis têm maior risco de óbito.
    """
    )

    st.markdown("""### Suicídios x Assistência Médica""")

    # suicidios por assistencia_medica
    df_assistencia_medica = df.groupby("assistencia_medica").count()["uf_obito"]

    # renomeando as colunas de df_assistencia_medica
    df_assistencia_medica = df_assistencia_medica.reset_index().rename(
        columns={"uf_obito": "qtd_obitos"}
    )

    # criando uma coluna com os valores em porcentagem
    df_assistencia_medica["percentual"] = (
        df_assistencia_medica["qtd_obitos"] / df_assistencia_medica["qtd_obitos"].sum()
    ) * 100

    df_assistencia_medica = df_assistencia_medica.sort_values(
        ascending=False, by="qtd_obitos"
    ).round(2)

    fig_assistencia_medica = px.bar(
        df_assistencia_medica,
        x="assistencia_medica",
        y="qtd_obitos",
        title="Quantidade de óbitos por assistência médica",
        template="ggplot2",
        text="qtd_obitos",
    )

    # nomeando os eixos
    fig_assistencia_medica.update_layout(
        xaxis_title="Assistência médica",
        yaxis_title="Quantidade de óbitos",
        font=dict(size=12, color="#000000"),
    )

    # centralizando o titulo
    fig_assistencia_medica.update_layout(title_x=0.5)

    # mostrando o grafico
    st.plotly_chart(fig_assistencia_medica, use_container_width=True)

    # concluindo
    st.markdown(
        """
        ### Conclusão 8:

        **Distribuição de Óbitos por Assistência Médica**: O gráfico mostra que a maioria esmagadora dos óbitos ocorre entre as pessoas que não tiveram assistência médica, que representam quase 80% dos óbitos. Isso indica que essas pessoas têm maior risco de óbito.
        """
    )


# executando a funcao main
if __name__ == "__main__":
    main()
