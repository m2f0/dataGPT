import streamlit as st

# Função para obter a chave API da configuração do usuário
def get_api_key():
    return st.session_state.get('api_key')

# Função para selecionar a rede neural e configurar a chave API
def select_neural_network():
    st.sidebar.header("Configuração da Rede Neural")
    neural_network = st.sidebar.selectbox("Escolha a rede neural", ["OpenAI", "NNovUp", "Meta", "Google"])
    api_key = st.sidebar.text_input("Insira a chave API", type="password")

    if neural_network and api_key:
        st.session_state['neural_network'] = neural_network
        st.session_state['api_key'] = api_key
        st.sidebar.success(f"{neural_network} configurada com sucesso!")

def get_selected_network():
    return st.session_state.get('neural_network')
