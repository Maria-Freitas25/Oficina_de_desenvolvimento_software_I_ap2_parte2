import streamlit as st

st.markdown('---')
st.markdown('# Sobre a Base de Dados')
st.markdown('''O naufrágio do titanic aconteceu em 15 de abril de 1992 no atlântico norte colidindo com um iceberg.
Quatro dias depois de sua viagem inaugural, o considerado ‘inafundável’ navio deixou 1502 mortos dos 2224 passageiros e tripulantes.
Mesmo com um fator sorte envolvido no desastre parece que alguns grupos tiveram mais chances que outros de sobrevivência.
Vamos trabalhar com A base de dados : 
conjunto de treinamento (train.csv)
__*Dicionário dos dados*__
- PassengerId (Número de identificação dos passageiros)
- survival (Sobrevivencia, 0 = não e 1 = sim)
- pclass (Classe de ingresso, 1 = 1° 2 = 2° 3 = 3° )
- Name (Nome do passageiro)
- sex (Sexo do passageiro)
- Age (Idade)
- sibsp ( irmãos / cônjuges a bordo do Titanic)
- parch (de pais / filhos a bordo do Titanic)
- ticket (Número do bilhete)
- fare (Tarifa de passageiro)
- cabin (Número da cabine)
- embarked (Porto de embarcação , C = Cherbourg, Q = Queenstown, S = Southampton)''')
st.markdown('---')
