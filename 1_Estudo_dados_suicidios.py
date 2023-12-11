import streamlit as st


# main
def main():
    # Configuração da página principal
    st.set_page_config(page_title="Suicídios no Brasil", page_icon="📊", layout="wide")

    st.sidebar.title("Navegação")

    # título da página
    st.title("1. Estudo sobre os dados de suicídios no Brasil nos anos de 2014 a 2018")

    # exibição do texto em markdown
    st.markdown(
        """
        ### Este estudo visa responder as seguintes perguntas:

        1. **Tendências ao longo do tempo**: Como as quantidades de suicídios mudaram ao longo do tempo? Elas estão aumentando, diminuindo ou permanecendo estáveis?

        2. **Diferenças demográficas**: Existem diferenças nas taxas de suicídio entre diferentes grupos demográficos? Por exemplo, as taxas de suicídio são diferentes para homens e mulheres? E quanto a diferentes faixas etárias ou níveis de educação?

        3. **Localização geográfica**: Existem diferenças nas taxas de suicídio entre diferentes localidades? Algumas áreas têm taxas de suicídio consistentemente mais altas do que outras?

        4. **Métodos de suicídio**: Quais são os métodos de suicídio mais comuns? Existem diferenças nos métodos usados por diferentes grupos demográficos ou em diferentes localidades?

        5. **Prevenção de suicídio**: Com base nos dados, quais estratégias podem ser mais eficazes na prevenção do suicídio? Existem certos grupos demográficos ou localidades que devem ser alvo de esforços de prevenção?
        """
    )


# inicializa a página
if __name__ == "__main__":
    main()
