import streamlit as st


# main
def main():
    # Configuração da página principal
    st.set_page_config(page_title="Conclusão", page_icon="📊", layout="wide")

    # título da página
    st.title("6. Sintetizando as respostas")

    st.markdown(
        """
            ### **Prevenção de suicídio**
            Com base nos dados e gráficos apresentados, podemos inferir algumas estratégias que podem ser eficazes na prevenção do suicídio:

            1. **Foco em Homens**: Os homens apresentam taxas de suicídio significativamente mais altas do que as mulheres. Portanto, os esforços de prevenção devem ser direcionados principalmente para os homens, especialmente aqueles na faixa etária de 20 a 39 anos.

            2. **Escolaridade**: Investimentos em educação podem ser úteis na prevenção do suicídio. Isso pode incluir a educação sobre saúde mental, o desenvolvimento de habilidades de enfrentamento, principalmente nos níveis do ensino fundamental e médio, que possuem taxas mais elevadas.

            3. **Localização Geográfica**: Conforme o gráfico "Óbitos por Suicídio no Brasil por UF e Ano" o top 5 dos estados com maiores quantidades de suicídios não se alteram durante o período estudado (2014 a 2018), são eles: "SP", "PR", "MG", "RS" e "SC". Então ações como programas de educação e conscientização sobre suicídio podem ser úteis. Isso pode incluir a educação sobre os sinais de aviso de suicídio e o que fazer se alguém suspeitar que uma pessoa está em risco.

            4. **Intervenções direcionadas**: Intervenções direcionadas a grupos de alto risco, como pessoas com doenças mentais diagnosticadas, pessoas que já tentaram suicídio no passado, e pessoas em situações de crise (como perda de emprego ou luto) ou que possuam algum histórico que possa levar ao CID X700, que representa mais de 50% das causas de óbito por suicídio.

            5. **Apoio a Jovens**: Os jovens, especialmente aqueles entre 10 e 19 anos, também apresentam um número significativo de suicídios. Portanto, o apoio a jovens em risco, como aqueles que sofrem de bullying, pressão dos colegas, ou estresse acadêmico, pode ser uma estratégia eficaz.

            6. **Prevenção nas ocupações**: Cada ocupação terá suas próprias necessidades e desafios únicos, por isso é importante personalizar a estratégia para cada grupo. Por exemplo no caso dos "SEM OCUPAÇÃO", que é o grupo com maior número de suicídios, pode ser útil fornecer apoio a pessoas que perderam o emprego ou estão passando por dificuldades financeiras.

            7. **Necessidade de Intervenções Direcionadas**: Dada a distribuição desigual de óbitos entre as raças, pode ser necessário desenvolver intervenções de saúde pública que sejam direcionadas especificamente para as raças com maior número de óbitos.

            8. **Falta de assistência médica**: Representado por quase 80% dos casos de suicídios estudados em nossa base de dados. Ações como: trabalhar para melhorar o acesso a serviços de saúde mental para aqueles sem assistência médica. Isso pode incluir clínicas de saúde mental comunitárias, linhas diretas de crise de saúde mental, e programas de saúde mental em escolas e locais de trabalho e, principalmente, políticas públicas que aumentem o acesso à saúde mental e aos serviços de prevenção de suicídio para todos, independentemente do status de assistência médica, podem ajudar a diminuir esses dados preocupantes.
    """
    )


# executando o main
if __name__ == "__main__":
    main()
