import streamlit as st

def main ():
  st.title("Teste StreamLit")
  st.subheader("How to run streamlit from colab")
  menu = ["Home","About"]
  choise = st.side.selectbox('Menu',menu)
  if choice == 'Home':
    st.subheader("Streamlit from Colab")
if name == 'main':
    main()
