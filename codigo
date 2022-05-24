from pywebio import *
from pywebio.output import *
from pywebio.input import *
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#!/usr/bin/env python3
# -- coding: utf-8 --
global idFilme
def main2():
    tpl = '''
    <details {{#open}}open{{/open}}>
    <summary>{{title}}</summary>
    {{#contents}}
    {{& pywebio_output_parse}}
    {{/contents}}
    </details>
'''
    dfTAGS = pd.read_csv(("tags.csv"), usecols=["movieId", "tag"], sep=",")
    dfMOVIES = pd.read_csv(("movies.csv"), usecols=["movieId", "title","genres","images"], sep=",")
    informacoes = input_group('Sistema de Recomendação de filmes',[
        input('Digite seu nome:',name=('username')),
    ])
    credentials = input_group("Escolha um filme de sua preferência:", [
        radio(options=["A lembrança de Anne Frank","Akira","Aladdin (1992)", 
        "Apollo 13", "As Patricinhas de Beverly Hills","Batman","Blade Runner","Coraline","Crepúsculo","Dumbo","Esqueceram de Mim",
        "Forrest Gump","Guerra nas Estrelas: Episódio 4 - Uma Nova Esperança","Harry Potter e a Pedra Filosofal","Interstellar",
        "John Wick","Jumanji","Karate Kid","La La Land","O Poderoso Chefão","Os Vingadores","Aristogatas","Se Beber, Não Case!",
        "The War Room","Titanic","Toy Story"]
				,inline=None, validate=None, value=None,name="radio", onchange=None)
        ])
    if credentials['radio']=='Toy Story':
        idFilme=1
    if credentials['radio']=='Jumanji':
        idFilme=2
    if credentials['radio'] == 'Guerra nas Estrelas: Episódio 4 - Uma Nova Esperança':
        idFilme=260
    if credentials['radio'] == 'Blade Runner':
        idFilme=541
    if credentials['radio'] == 'Akira':
        idFilme=1274
    if credentials['radio'] == 'Anaconda':
        idFilme=1499
    if credentials['radio'] == 'John Wick':
        idFilme=115149  
    if credentials['radio'] == 'Forrest Gump':
        idFilme=356 
    if credentials['radio'] == 'Aladdin (1992)':
        idFilme=588 
    if credentials['radio'] == 'Batman':
        idFilme=592
    if credentials['radio'] == 'A lembrança de Anne Frank':
        idFilme=116
    if credentials['radio'] == 'Apollo 13':
        idFilme=150
    if credentials['radio']=='O Poderoso Chefão':
        idFilme=858
    if credentials['radio']=='Titanic':
        idFilme=1721
    if credentials['radio']=='Karate Kid':
        idFilme=2420
    if credentials['radio']=='The War Room':
        idFilme=556
    if credentials['radio']=='Aristogatas':
        idFilme=616
    if credentials['radio']=='La La Land':
        idFilme=164909
    if credentials['radio']=='Dumbo':
        idFilme=1029
    if credentials['radio']=='Coraline':
        idFilme=66097
    if credentials['radio']=='Interstellar':
        idFilme=109487
    if credentials['radio']=='As Patricinhas de Beverly Hills':
        idFilme=39
    if credentials['radio']=='Harry Potter e a Pedra Filosofal':
        idFilme=4896
    if credentials['radio']=='Os Vingadores':
        idFilme=89745
    if credentials['radio']=='Crepúsculo':
        idFilme=63992
    if credentials['radio']=='Esqueceram de Mim':
        idFilme=586
    if credentials['radio']=='Se Beber, Não Case!':
        idFilme=69122
    tags = []
    filmes = []
    images = []
    filmesRecomendados = []
    filmesImages = []
    filmesCol = dfTAGS["movieId"].values
    tagsCol = dfTAGS["tag"].values
    for i in range(len(filmesCol)):
        if idFilme == filmesCol[i]:        
            if tagsCol[i] not in tags:
                tags.append(tagsCol[i].lower())
    for j in range(len(tagsCol)):
        if tagsCol[j].lower() in tags:
            if filmesCol[j] not in filmes:
                filmes.append(filmesCol[j])
                images.append(filmesCol[j])
    filmesId = dfMOVIES["movieId"].values
    filmesNome = dfMOVIES["title"].values
    filmeImage = dfMOVIES["images"].values
    filmeEscolhido = ""
    for k in range(len(filmesId)):
        if filmesId[k] == idFilme:
            filmeEscolhido = filmesNome[k]
    for l in range(len(filmes)):
        for m in range(len(filmesNome)):
            if filmes[l] == filmesId[m]:
                filmesRecomendados.append(filmesNome[m])
                filmesImages.append(filmeImage[m])
    put_table([
        ['Usuário:',(informacoes['username'])],
        ['Filme:',filmeEscolhido]
    ])
    style(put_text('TAGS:'), 'color:green')
    for n in range(1):
        put_text("\t",n+1,"-", tags[n])
    style(put_text('FILMES RECOMENDADOS:'), 'color:green')
    for o in range(7):
            put_widget(tpl, {
            "open": False,
            "title": filmesRecomendados[o],
            "contents": [
                filmesRecomendados[o],
                put_row([put_image(filmesImages[o])])
            ]
        })
@config(theme='dark')    
def main():
    main2()
pass
