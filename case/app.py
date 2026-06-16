"""
Fluência Real — Página de Vendas (case demonstrativo)
Como rodar:
    pip install streamlit
    streamlit run app.py

Mantenha o arquivo 'sales_page.html' na mesma pasta deste app.py.
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Fluência Real — Destrave seu inglês",
    page_icon="🗣️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Esconde o "chrome" padrão do Streamlit e remove margens para a página ocupar tudo
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .stApp {background: #FBF7F0;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
      iframe {border: none !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Carrega o HTML da página de vendas
html_path = Path(__file__).parent / "sales_page.html"
html = html_path.read_text(encoding="utf-8")

# Renderiza. A altura cresce sozinha via postMessage (setFrameHeight);
# height inicial + scrolling=True garantem que nada fica cortado caso o auto-resize falhe.
components.html(html, height=900, scrolling=True)
