import folium
import webbrowser

# Cria o mapa centralizado no Brasil
mapa = folium.Map(location=[-14.2350, -51.9253], zoom_start=4, tiles="CartoDB positron")

# Lista de pontos turísticos
pontos_turisticos = [
    # Sudeste
    {
        "nome": "Cristo Redentor",
        "local": "Rio de Janeiro - RJ",
        "coordenadas": [-22.9519, -43.2105],
        "curiosidade": "Uma das 7 maravilhas do mundo moderno, símbolo do Brasil.",
        "cor": "red",
        "icone": "glyphicon-star"
    },
    {
        "nome": "Pão de Açúcar",
        "local": "Rio de Janeiro - RJ",
        "coordenadas": [-22.9486, -43.1566],
        "curiosidade": "Morro icônico com teleférico e vista panorâmica da cidade.",
        "cor": "orange",
        "icone": "glyphicon-screenshot"
    },
    {
        "nome": "Ouro Preto",
        "local": "Ouro Preto - MG",
        "coordenadas": [-20.3856, -43.5036],
        "curiosidade": "Cidade histórica com arquitetura colonial e igrejas barrocas.",
        "cor": "purple",
        "icone": "glyphicon-home"
    },
    {
        "nome": "Ilha Grande",
        "local": "Angra dos Reis - RJ",
        "coordenadas": [-23.1496, -44.2839],
        "curiosidade": "Paraíso de praias e trilhas na Mata Atlântica.",
        "cor": "lightblue",
        "icone": "glyphicon-tree-deciduous"
    },

    # Sul
    {
        "nome": "Cataratas do Iguaçu",
        "local": "Foz do Iguaçu - PR",
        "coordenadas": [-25.6953, -54.4367],
        "curiosidade": "Conjunto de 275 quedas d’água na fronteira com a Argentina.",
        "cor": "blue",
        "icone": "glyphicon-tint"
    },
    {
        "nome": "Gramado",
        "local": "Gramado - RS",
        "coordenadas": [-29.3733, -50.8761],
        "curiosidade": "Cidade turística famosa pelo Natal Luz e arquitetura europeia.",
        "cor": "green",
        "icone": "glyphicon-tree-deciduous"
    },
    {
        "nome": "Serra do Rio do Rastro",
        "local": "Bom Jardim da Serra - SC",
        "coordenadas": [-28.4145, -49.6024],
        "curiosidade": "Estrada com curvas incríveis e vista de tirar o fôlego.",
        "cor": "darkgreen",
        "icone": "glyphicon-road"
    },

    # Nordeste
    {
        "nome": "Pelourinho",
        "local": "Salvador - BA",
        "coordenadas": [-12.9714, -38.5108],
        "curiosidade": "Centro histórico com arquitetura colonial e forte cultura afro-brasileira.",
        "cor": "pink",
        "icone": "glyphicon-king"
    },
    {
        "nome": "Lençóis Maranhenses",
        "local": "Barreirinhas - MA",
        "coordenadas": [-2.5319, -43.1216],
        "curiosidade": "Dunas com lagoas cristalinas que se formam na época das chuvas.",
        "cor": "lightblue",
        "icone": "glyphicon-picture"
    },
    {
        "nome": "Praia de Jericoacoara",
        "local": "Jijoca de Jericoacoara - CE",
        "coordenadas": [-2.7956, -40.5122],
        "curiosidade": "Praia paradisíaca com dunas, lagoas e pores do sol famosos.",
        "cor": "beige",
        "icone": "glyphicon-sunglasses"
    },
    {
        "nome": "Praia dos Carneiros",
        "local": "Tamandaré - PE",
        "coordenadas": [-8.7030, -35.0506],
        "curiosidade": "Praia com coqueiros, águas claras e a charmosa Capela de São Benedito.",
        "cor": "cadetblue",
        "icone": "glyphicon-heart"
    },
    {
        "nome": "Fernando de Noronha",
        "local": "Fernando de Noronha - PE",
        "coordenadas": [-3.8553, -32.4233],
        "curiosidade": "Arquipélago com algumas das praias mais bonitas do mundo.",
        "cor": "darkblue",
        "icone": "glyphicon-plane"
    },

    # Centro-Oeste
    {
        "nome": "Chapada dos Veadeiros",
        "local": "Alto Paraíso - GO",
        "coordenadas": [-14.1300, -47.5200],
        "curiosidade": "Parque Nacional com cachoeiras, trilhas e biodiversidade única.",
        "cor": "darkgreen",
        "icone": "glyphicon-leaf"
    },
    {
        "nome": "Pantanal",
        "local": "Mato Grosso do Sul",
        "coordenadas": [-17.5980, -57.7970],
        "curiosidade": "Maior planície alagável do mundo, rica em fauna e flora.",
        "cor": "cadetblue",
        "icone": "glyphicon-flag"
    },
    {
        "nome": "Chapada dos Guimarães",
        "local": "Chapada dos Guimarães - MT",
        "coordenadas": [-15.4606, -55.7500],
        "curiosidade": "Formações rochosas e cachoeiras impressionantes.",
        "cor": "lightgreen",
        "icone": "glyphicon-tree-deciduous"
    },

    # Norte
    {
        "nome": "Teatro Amazonas",
        "local": "Manaus - AM",
        "coordenadas": [-3.1303, -60.0233],
        "curiosidade": "Teatro histórico símbolo do ciclo da borracha.",
        "cor": "darkpurple",
        "icone": "glyphicon-music"
    },
    {
        "nome": "Encontro das Águas",
        "local": "Manaus - AM",
        "coordenadas": [-3.1347, -59.8988],
        "curiosidade": "Rio Negro e Rio Solimões correm lado a lado sem se misturar.",
        "cor": "black",
        "icone": "glyphicon-tint"
    },
    {
        "nome": "Monte Roraima",
        "local": "Pacaraima - RR",
        "coordenadas": [5.2270, -60.7650],
        "curiosidade": "Montanha icônica na tríplice fronteira Brasil-Venezuela-Guiana.",
        "cor": "orange",
        "icone": "glyphicon-screenshot"
    }
]

# Adiciona os marcadores no mapa
for ponto in pontos_turisticos:
    popup_html = f"""
    <h4>{ponto['nome']}</h4>
    <b>Localização:</b> {ponto['local']}<br>
    <b>Curiosidade:</b> {ponto['curiosidade']}
    """
    folium.Marker(
        location=ponto["coordenadas"],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=ponto["nome"],
        icon=folium.Icon(color=ponto["cor"], icon=ponto["icone"])
    ).add_to(mapa)

# Salva e abre o mapa
mapa.save("mapa_turistico_brasil.html")
webbrowser.open("mapa_turistico_brasil.html")
