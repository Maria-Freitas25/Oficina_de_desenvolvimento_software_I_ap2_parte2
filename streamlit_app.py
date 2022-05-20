import streamlit as st
PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)
def main ():
  st.title("Teste StreamLit")
  st.subheader("How to run streamlit from colab")
  menu = ["Home","About"]
  choise = st.side.selectbox('Menu',menu)
  if choice == 'Home':
    st.subheader("Streamlit from Colab")
  if name == 'main':
    main()
