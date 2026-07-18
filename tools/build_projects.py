#!/usr/bin/env python3
"""Generate the per-project case-study pages (PT + EN) from project data.

Run from the repo root:  python3 tools/build_projects.py
Outputs: projetos/<slug>/index.html and en/projects/<slug>/index.html
"""
import os
from PIL import Image

SITE = "https://drabelo.github.io/felipebasa"

def dims(name):
    return Image.open(f"assets/img/{name}.jpg").size

def img_tag(name, alt, rel, lazy=True, hero=False):
    w, h = dims(name)
    srcset = []
    for tw in (800, 1600):
        p = f"assets/img/{name}-{tw}.webp"
        if os.path.exists(p):
            srcset.append(f"{rel}assets/img/{name}-{tw}.webp {min(tw, w)}w")
    attrs = f'src="{rel}assets/img/{name}.jpg" alt="{alt}" width="{w}" height="{h}"'
    if srcset:
        attrs += f' srcset="{", ".join(srcset)}" sizes="(max-width: 720px) 100vw, 1200px"'
    if lazy and not hero:
        attrs += ' loading="lazy"'
    if hero:
        attrs += ' fetchpriority="high"'
    return f"<img {attrs}>"

# ---------------------------------------------------------------- project data
# Shared per-project structure; 'pt' and 'en' keys hold localized strings.
PROJECTS = [
 dict(
  slug="mcentral-park", name="MCentral Park", year="2023", hero="mcp-hero",
  pt=dict(
    status="Entregue", tags=["Retrofit", "Habitacional"],
    desc="Reforma total das áreas de lazer e adequação de fachada do condomínio vertical MCentral Park, em Goiânia.",
    meta=[("Ano","2023"),("Tipologia","Habitacional (Retrofit)"),("Área","220 m²"),("Coautoria","Felipe Sousa"),("Local","Goiânia, GO")],
    hero_alt="MCentral Park — fachada renovada com brise de madeira, Goiânia",
    text=["O projeto traz como premissa a reforma total das áreas de lazer e convivência do condomínio vertical MCentral Park, em Goiânia, assim como a adequação de fachada tanto na base do edifício quanto nas fachadas dos pavimentos-tipo. A reconfiguração dos ambientes existentes e das circulações, além da criação de novos ambientes, propõe trazer uso a espaços subutilizados, novos usos e maior qualidade àqueles mantidos.",
          "Participei desde os partidos formais iniciais, passando por projetos mais técnicos como o luminotécnico proposto, até a modelagem e concepção dos interiores."],
    quote="“As formas sinuosas em planta e nos objetos de design vêm para trazer a escala humana e natural na requalificação de uma preexistência reta e pasteurizada.”", cite=None,
    gallery=[("mcp-lobby","Lobby do MCentral Park com revestimento em madeira e mobiliário curvo"),
             ("mcp-sketch","Croqui de estudo da fachada do MCentral Park")],
    process=[("mcp-plan-layout","Planta de layout do mezanino — Revit"),
             ("mcp-plan-demolir","Planta de demolir — intervenção sobre a preexistência"),
             ("mcp-plan-construir","Planta de construir — nova configuração dos ambientes")],
    participation="Coautoria e concepção de reforma de arquitetura e interiores · Modelagem 3D (Revit, Lumion) · Coordenação e correção de projeto executivo e de interiores (Revit)",
    credit="Render — <b>Felipe Sousa</b> · Revit · Lumion · Melhoramento em IA",
  ),
  en=dict(
    status="Delivered", tags=["Retrofit", "Housing"],
    desc="Full renovation of the leisure areas and façade adaptation of the MCentral Park residential tower in Goiânia, Brazil.",
    meta=[("Year","2023"),("Type","Housing (Retrofit)"),("Area","220 m²"),("Co-author","Felipe Sousa"),("Location","Goiânia, Brazil")],
    hero_alt="MCentral Park — renovated façade with timber brise-soleil, Goiânia",
    text=["The project is premised on the full renovation of the leisure and social areas of the MCentral Park residential tower in Goiânia, along with the adaptation of the façade at both the building's base and the typical floors. Reconfiguring existing rooms and circulation, and creating new spaces, brings use to underused areas, adds new programs and raises the quality of those retained.",
          "I took part from the initial formal concepts, through more technical packages such as the proposed lighting design, to the modeling and conception of the interiors."],
    quote="“The sinuous forms in plan and in the design objects bring human and natural scale to the requalification of a straight, pasteurized existing building.”", cite=None,
    gallery=[("mcp-lobby","MCentral Park lobby with timber cladding and curved furniture"),
             ("mcp-sketch","Study sketch of the MCentral Park façade")],
    process=[("mcp-plan-layout","Mezzanine layout plan — Revit"),
             ("mcp-plan-demolir","Demolition plan — intervention on the existing building"),
             ("mcp-plan-construir","Construction plan — new room configuration")],
    participation="Co-authorship and concept for the architecture and interiors renovation · 3D modeling (Revit, Lumion) · Coordination and review of construction and interior packages (Revit)",
    credit="Render — <b>Felipe Sousa</b> · Revit · Lumion · AI enhancement",
  ),
 ),
 dict(
  slug="casa-noor", name="Casa Noor", year="2022", hero="noor-sign",
  pt=dict(
    status="Construído", tags=["Residencial", "Construído"],
    desc="Residência unifamiliar de 500 m² no interior de Goiás — dos croquis em aquarela à obra construída.",
    meta=[("Ano","2022"),("Tipologia","Residência Unifamiliar"),("Área","500 m²"),("Coautoria","Felipe Sousa"),("Fotos","Heitor Rocha")],
    hero_alt="Entrada da Casa Noor, com letreiro em metal sobre parede ripada de madeira",
    text=["Casa Noor é um projeto residencial desenvolvido no Escritório Marcos Lula Arquiteto para um casal e a mãe de um deles, no interior de Goiás. Os primeiros estudos formais partem de croquis manuais finalizados em aquarela, que servem tanto como vislumbre inicial da forma do projeto na primeira entrega quanto como presente de open house na entrega final aos clientes. O projeto foi entregue e finalizado."],
    quote="“A palavra Noor (ou Nur) vem do árabe e significa luz, brilho ou claridade. No entanto, seu significado vai muito além da luz física, carregando um forte simbolismo espiritual.”", cite=None,
    gallery=[("noor-living","Sala de estar integrada ao jardim interno, Casa Noor"),
             ("noor-dining","Sala de jantar com luminárias de fibra natural, Casa Noor"),
             ("noor-exterior","Fachada em ripas de madeira e concreto aparente, Casa Noor"),
             ("noor-terrace","Terraço com cactos e mobiliário externo, Casa Noor"),
             ("noor-watercolor","Pintura em aquarela do estudo inicial da Casa Noor")],
    process=[("noor-det-alvenaria","Detalhamento da abertura orgânica em alvenaria — vistas de raios e malha construtiva (Revit)")],
    participation="Coautoria e concepção de arquitetura e interiores · Modelagem 3D (Revit, Lumion) · Representação de projeto executivo e de interiores · Diretrizes e compatibilização de projetos · Produção para fotos",
    credit="Pintura em aquarela e produção para fotos — <b>Felipe Sousa</b> · Fotos — <b>Heitor Rocha</b>",
  ),
  en=dict(
    status="Built", tags=["Residential", "Built"],
    desc="A 500 m² single-family house in the countryside of Goiás, Brazil — from watercolor sketches to the built work.",
    meta=[("Year","2022"),("Type","Single-family House"),("Area","500 m²"),("Co-author","Felipe Sousa"),("Photos","Heitor Rocha")],
    hero_alt="Casa Noor entrance, metal lettering on a timber-slatted wall",
    text=["Casa Noor is a residential project developed at the Marcos Lula Arquiteto office for a couple and one of their mothers, in the countryside of Goiás. The first formal studies begin as hand sketches finished in watercolor, serving both as an early glimpse of the project's form at the first presentation and as an open-house gift to the clients at final delivery. The project was delivered and completed."],
    quote="“The word Noor (or Nur) comes from Arabic and means light, glow or clarity. Its meaning, however, goes far beyond physical light, carrying strong spiritual symbolism.”", cite=None,
    gallery=[("noor-living","Living room opening onto the internal garden, Casa Noor"),
             ("noor-dining","Dining room with natural-fiber pendant lights, Casa Noor"),
             ("noor-exterior","Façade in timber slats and exposed concrete, Casa Noor"),
             ("noor-terrace","Terrace with cacti and outdoor furniture, Casa Noor"),
             ("noor-watercolor","Watercolor painting of the initial study for Casa Noor")],
    process=[("noor-det-alvenaria","Detailing of the organic masonry opening — radius and construction-grid views (Revit)")],
    participation="Co-authorship and concept for architecture and interiors · 3D modeling (Revit, Lumion) · Construction and interior documentation · Design guidelines and coordination · Photo production",
    credit="Watercolor painting and photo production — <b>Felipe Sousa</b> · Photos — <b>Heitor Rocha</b>",
  ),
 ),
 dict(
  slug="estande-florata", name="Estande Florata", year="2019", hero="florata-hero",
  en_name="Florata Sales Pavilion",
  pt=dict(
    status="Construído", tags=["Comercial", "Construído"],
    desc="Estande de vendas em módulos industrializados com brise em eucalipto tratado, no entorno de Goiânia.",
    meta=[("Ano","2019"),("Tipologia","Comercial"),("Área","220 m²"),("Coautoria","Felipe Sousa"),("Fotos","Heitor Rocha")],
    hero_alt="Estande de vendas Florata, estrutura modular com brise em eucalipto tratado",
    text=["O projeto utiliza módulos construtivos industrializados para garantir rapidez de execução e sustentabilidade, atendendo também à futura ocupação do condomínio. A composição volumétrica e a materialidade buscam se afastar da estética convencional dos “contêineres”, estabelecendo diálogo com o contexto das chácaras de alto padrão no entorno de Goiânia.",
          "Os eucaliptos tratados constituem o principal elemento do partido arquitetônico, conferindo identidade à fachada, “aquecendo” os volumes metálicos e integrando soluções técnicas de forma discreta."],
    quote="Estrutura modular, industrializada e reutilizável — em diálogo com a paisagem rural do entorno.", cite=None,
    gallery=[("florata-2","Estande Florata sob árvores, fachada em vidro e madeira"),
             ("florata-3","Estande Florata, vista lateral com escada helicoidal"),
             ("florata-4","Estande Florata visto do gramado, com mobiliário externo")],
    process=[("florata-croqui","Croqui de estudo do partido — desenho e pintura"),
             ("florata-plan","Planta de layout executiva, com especificações de fornecedores (Revit)")],
    participation="Coautoria e concepção de arquitetura e interiores · Modelagem 3D · Representação de projeto executivo e de interiores (Revit, Lumion)",
    credit="Render — <b>Felipe Sousa</b> · Revit · Lumion · Photoshop · Fotos — <b>Heitor Rocha</b>",
  ),
  en=dict(
    status="Built", tags=["Commercial", "Built"],
    desc="A sales pavilion in industrialized modules with treated-eucalyptus brise-soleil, on the outskirts of Goiânia, Brazil.",
    meta=[("Year","2019"),("Type","Commercial"),("Area","220 m²"),("Co-author","Felipe Sousa"),("Photos","Heitor Rocha")],
    hero_alt="Florata sales pavilion, modular structure with treated-eucalyptus brise-soleil",
    text=["The project uses industrialized construction modules to guarantee speed of execution and sustainability, while also serving the condominium's future occupation. The volumetric composition and materiality seek distance from the conventional “container” aesthetic, establishing a dialogue with the context of high-end country estates around Goiânia.",
          "Treated eucalyptus logs are the main element of the architectural concept, giving the façade its identity, “warming” the metallic volumes and integrating technical solutions discreetly."],
    quote="A modular, industrialized and reusable structure — in dialogue with the surrounding rural landscape.", cite=None,
    gallery=[("florata-2","Florata pavilion under the trees, glass and timber façade"),
             ("florata-3","Florata pavilion, side view with helical stair"),
             ("florata-4","Florata pavilion seen from the lawn, with outdoor furniture")],
    process=[("florata-croqui","Concept study sketch — drawing and painting"),
             ("florata-plan","Executive layout plan with supplier specifications (Revit)")],
    participation="Co-authorship and concept for architecture and interiors · 3D modeling · Construction and interior documentation (Revit, Lumion)",
    credit="Render — <b>Felipe Sousa</b> · Revit · Lumion · Photoshop · Photos — <b>Heitor Rocha</b>",
  ),
 ),
 dict(
  slug="casa-lisa", name="Casa Lisa", year="2024", hero="lisa-watercolor",
  pt=dict(
    status="Entregue", tags=["Reforma", "Paisagismo"],
    desc="Reforma residencial e paisagismo — intervenções pontuais sobre uma pré-existência inacabada.",
    meta=[("Ano","2024"),("Tipologia","Reforma residencial e Paisagismo"),("Área","500 m²"),("Coautoria","Felipe Sousa")],
    hero_alt="Pintura em aquarela do estudo paisagístico da Casa Lisa, formas orgânicas de canteiros",
    text=["Casa Lisa foi um dos projetos mais desafiadores, pois a cliente vinha de uma terceira tentativa com escritórios de arquitetura, orçamento limitado e muitos receios devido a experiências anteriores não resolvidas com outros profissionais. A proposta consistiu em intervenções pontuais sobre uma pré-existência inacabada.",
          "O desenho e o detalhamento dos elementos paisagísticos propostos são o ponto alto de um projeto que conseguiu atender aos desejos de uma cliente com olhar extremamente apurado e demandas rigorosas de funcionalidade e orçamento."],
    quote="“Os jardins não começaram comigo e nem vão terminar depois de mim. Espero que hajam outras pessoas interessadas na perpetuação das plantas.”", cite="Burle Marx",
    gallery=[],
    process=[("lisa-plan-raios","Berço paisagístico — locação e raios de curvas (Revit)")],
    participation="Desenho, detalhamento e compatibilização de projeto paisagístico (Revit)",
    credit="Pintura em aquarela — <b>Felipe Sousa</b>",
  ),
  en=dict(
    status="Delivered", tags=["Renovation", "Landscape"],
    desc="Residential renovation and landscape design — precise interventions on an unfinished existing house.",
    meta=[("Year","2024"),("Type","Residential renovation & Landscape"),("Area","500 m²"),("Co-author","Felipe Sousa")],
    hero_alt="Watercolor painting of the landscape study for Casa Lisa, organic planting-bed shapes",
    text=["Casa Lisa was one of the most challenging projects: the client arrived on her third attempt with architecture offices, with a limited budget and many hesitations left by unresolved past experiences with other professionals. The brief consisted of precise interventions on an unfinished existing house.",
          "The design and detailing of the proposed landscape elements are the high point of a project that managed to meet the wishes of a client with an extremely refined eye and strict demands of functionality and budget."],
    quote="“Gardens did not begin with me, and they will not end after me. I hope there will be other people interested in the perpetuation of plants.”", cite="Burle Marx",
    gallery=[],
    process=[("lisa-plan-raios","Landscape bed — setting-out and curve radii (Revit)")],
    participation="Design, detailing and coordination of the landscape package (Revit)",
    credit="Watercolor painting — <b>Felipe Sousa</b>",
  ),
 ),
 dict(
  slug="casa-fs", name="Casa FS", year="2025", hero="casafs-sketch",
  pt=dict(
    status="Estudo autoral", tags=["Residencial", "Autoral"],
    desc="Ensaio anual autoral — a casa ideal como exercício de autoconhecimento e projeto.",
    meta=[("Ano","2025"),("Tipologia","Residencial"),("Área","200 m²"),("Autoria","Felipe Sousa")],
    hero_alt="Croqui de estudo da Casa FS, marquise em concreto sobre pátio",
    text=["Pensar em uma casa para si, sendo arquiteto ou não, é um exercício contínuo e de maturidade. Observar constantemente como habitamos, e como o ambiente tem a capacidade de reforçar ou dificultar comportamentos, nos entrega um programa detalhado — e, como arquiteto, conseguimos refletir muito além da organização de gavetas.",
          "Daí vieram os ensaios anuais, onde imagino a casa ideal para minha vida atual. A resposta de 2025 é uma casa onde o social e o íntimo se separam por pavimentos, e a área de serviços ocupa o “coração da casa”, com acesso facilitado à entrada, à sala, à cozinha, ao jardim e aos quartos."],
    quote="“Entre o corpo e a casa: um exercício anual de autoconhecimento e projeto.”", cite=None,
    gallery=[],
    process=[("fs-plan-terreo","Plantas do térreo e do pavimento superior — social e íntimo separados por nível (Revit)")],
    participation="Estudo autoral anual — programa, croqui manual e documentação de plantas (Revit)",
    credit="Croqui — <b>Felipe Sousa</b>",
  ),
  en=dict(
    status="Personal study", tags=["Residential", "Independent"],
    desc="An annual personal essay — the ideal house as an exercise in self-knowledge and design.",
    meta=[("Year","2025"),("Type","Residential"),("Area","200 m²"),("Author","Felipe Sousa")],
    hero_alt="Study sketch for Casa FS, concrete canopy over a courtyard",
    text=["Thinking of a house for oneself, architect or not, is a continuous exercise in maturity. Constantly observing how we inhabit — and how the environment can reinforce or hinder behavior — hands us a detailed brief; and as architects we can reflect far beyond the organization of drawers.",
          "From this came the annual essays in which I imagine the ideal house for my current life. The 2025 answer is a house where social and private life are separated by floor, and the utility area occupies the “heart of the house”, with easy access to the entrance, living room, kitchen, garden and bedrooms."],
    quote="“Between the body and the house: an annual exercise in self-knowledge and design.”", cite=None,
    gallery=[],
    process=[("fs-plan-terreo","Ground and upper floor plans — social and private life split by level (Revit)")],
    participation="Annual independent study — brief, hand sketch and plan documentation (Revit)",
    credit="Sketch — <b>Felipe Sousa</b>",
  ),
 ),
 dict(
  slug="casa-vertice", name="Casa Vértice", year="2026", hero="vertice-1",
  pt=dict(
    status="Em desenvolvimento", tags=["Residencial", "Em desenvolvimento"],
    desc="Residência unifamiliar de 550 m² em terreno com declive — formas retas e o apuramento máximo de seus encontros.",
    meta=[("Ano","2026"),("Tipologia","Residência Unifamiliar"),("Área","550 m²"),("Coautoria","Felipe Sousa")],
    hero_alt="Casa Vértice, render em preto e branco da fachada de entrada",
    text=["Casa Vértice é um projeto residencial para uma família funcional e apolínea, que tem como partido as formas retas e o apuramento máximo do encontro entre elas. A casa é implantada em um terreno com declive, em condomínio, e distribui seu programa em três pavimentos, aproveitando a queda do terreno para a implantação de um volume mais horizontalizado.",
          "O projeto se encontra em desenvolvimento no escritório, em fase de definições complementares — elétrica, acabamentos e luminotécnica — com participação ativa minha em produção, concepção, coordenação e correção da produção dos colaboradores envolvidos."],
    quote="“O conceito apolíneo é inspirado na mitologia grega, representando a razão, a ordem, a clareza e a beleza harmoniosa — o domínio da forma e da medida.”", cite="Segundo Nietzsche",
    gallery=[("vertice-2","Casa Vértice, render em preto e branco da fachada posterior com piscina")],
    process=[("vertice-det-secao","Corte de detalhamento — suíte máster, brises em ACM e piscina de borda infinita (Revit)"),
             ("vertice-det-tijolo","Detalhe da parede ventilada — amarração dos tijolos cerâmicos com vergalhão metálico (Revit)")],
    participation="Coautoria e concepção de arquitetura e interiores · Modelagem 3D · Representação de projeto executivo · Detalhamento (Revit)",
    credit="Render — <b>Felipe Sousa</b> · Revit · Lumion · Photoshop",
  ),
  en=dict(
    status="In development", tags=["Residential", "In development"],
    desc="A 550 m² single-family house on a sloping lot — straight lines and the utmost refinement of their meeting points.",
    meta=[("Year","2026"),("Type","Single-family House"),("Area","550 m²"),("Co-author","Felipe Sousa")],
    hero_alt="Casa Vértice, black-and-white render of the entrance façade",
    text=["Casa Vértice is a residential project for a functional, Apollonian family, whose concept is straight lines and the utmost refinement of their meeting points. The house sits on a sloping lot within a gated community and distributes its program across three floors, using the drop of the terrain to set a more horizontal volume into the site.",
          "The project is under development at the office, in the phase of complementary definitions — electrical, finishes and lighting design — with my active participation in production, conception, and the coordination and review of the team's output."],
    quote="“The Apollonian concept is inspired by Greek mythology, representing reason, order, clarity and harmonious beauty — the command of form and measure.”", cite="After Nietzsche",
    gallery=[("vertice-2","Casa Vértice, black-and-white render of the rear façade with pool")],
    process=[("vertice-det-secao","Detail section — master suite, ACM brise-soleil and infinity-edge pool (Revit)"),
             ("vertice-det-tijolo","Ventilated-wall detail — ceramic bricks tied with steel rebar (Revit)")],
    participation="Co-authorship and concept for architecture and interiors · 3D modeling · Construction documentation · Detailing (Revit)",
    credit="Render — <b>Felipe Sousa</b> · Revit · Lumion · Photoshop",
  ),
 ),
]

# ---------------------------------------------------------------- localization
L = dict(
 pt=dict(
   lang="pt-BR", dirname="projetos", rel="../../", home="../../",
   other_lang="EN", other_dirname="en/projects",
   nav=[("#sobre","Sobre"),("__INDEX__","Projetos"),("#concursos","Concursos"),("#arte","Arte"),("#contato","Contato")],
   title_suffix="Felipe Atelier", eyebrow_word="Projeto",
   process_eyebrow="Processo", process_title="Do croqui ao executivo.",
   participation_label="Participação no projeto",
   back="← Todos os projetos", prev="Projeto anterior", next="Próximo projeto",
   contact_line='felipebatistadesousa@gmail.com · <a href="https://wa.me/5562993671667" target="_blank" rel="noopener">WhatsApp</a> · <a href="https://instagram.com/felipebsou" target="_blank" rel="noopener">@felipebsou</a>',
   footer_note="© 2026 Felipe Atelier · Composto em Space Grotesk &amp; Lora — São Paulo",
   og_locale="pt_BR", close="Fechar", prev_img="Imagem anterior", next_img="Próxima imagem", menu="Abrir menu",
 ),
 en=dict(
   lang="en", dirname="en/projects", rel="../../../", home="../../",
   other_lang="PT", other_dirname="projetos",
   nav=[("#about","About"),("__INDEX__","Projects"),("#competitions","Competitions"),("#art","Art"),("#contact","Contact")],
   title_suffix="Felipe Atelier", eyebrow_word="Project",
   process_eyebrow="Process", process_title="From sketch to construction set.",
   participation_label="Role in the project",
   back="← All projects", prev="Previous project", next="Next project",
   contact_line='felipebatistadesousa@gmail.com · <a href="https://wa.me/5562993671667" target="_blank" rel="noopener">WhatsApp</a> · <a href="https://instagram.com/felipebsou" target="_blank" rel="noopener">@felipebsou</a>',
   footer_note="© 2026 Felipe Atelier · Set in Space Grotesk &amp; Lora — São Paulo",
   og_locale="en_US", close="Close", prev_img="Previous image", next_img="Next image", menu="Open menu",
 ),
)

def page(lang, i, p):
    loc = L[lang]
    d = p[lang]
    rel = loc["rel"]
    name = p.get("en_name", p["name"]) if lang == "en" else p["name"]
    n = f"{i+1:02d}"
    url = f"{SITE}/{loc['dirname']}/{p['slug']}/"
    pt_url = f"{SITE}/projetos/{p['slug']}/"
    en_url = f"{SITE}/en/projects/{p['slug']}/"
    hero_w, hero_h = dims(p["hero"])
    prev_p = PROJECTS[(i-1) % len(PROJECTS)]
    next_p = PROJECTS[(i+1) % len(PROJECTS)]
    prev_name = prev_p.get("en_name", prev_p["name"]) if lang == "en" else prev_p["name"]
    next_name = next_p.get("en_name", next_p["name"]) if lang == "en" else next_p["name"]

    nav_links = "\n".join(
        f'      <li><a href="../">{t}</a></li>' if h == "__INDEX__"
        else f'      <li><a href="{loc["home"]}{h}">{t}</a></li>'
        for h, t in loc["nav"])
    other_link = f"{rel}{loc['other_dirname']}/{p['slug']}/"
    meta_html = "\n".join(f'        <div><b>{k}</b><span>{v}</span></div>' for k, v in d["meta"])
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in d["tags"])
    text_html = "\n".join(f"          <p>{t}</p>" for t in d["text"])
    cite_html = f"<cite>{d['cite']}</cite>" if d["cite"] else ""
    gallery_html = ""
    if d["gallery"]:
        imgs = "\n".join(f"        {img_tag(nm, alt, rel)}" for nm, alt in d["gallery"])
        gallery_html = f'\n      <div class="project-gallery two reveal">\n{imgs}\n      </div>\n'
    process_imgs = "\n".join(f"        {img_tag(nm, alt, rel)}" for nm, alt in d["process"])
    n_proc = len(d["process"])
    process_cols = "" if n_proc == 3 else ("two" if n_proc == 2 else "one")

    return f"""<!doctype html>
<html lang="{loc['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — {loc['title_suffix']}</title>
<meta name="description" content="{d['desc']}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="pt-BR" href="{pt_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{pt_url}">

<meta property="og:type" content="article">
<meta property="og:title" content="{name} — {loc['title_suffix']}">
<meta property="og:description" content="{d['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/{p['hero']}.jpg">
<meta property="og:locale" content="{loc['og_locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/assets/img/{p['hero']}.jpg">
<meta name="theme-color" content="#ffffff">

<link rel="icon" type="image/svg+xml" href="{rel}assets/img/favicon.svg">
<link rel="apple-touch-icon" href="{rel}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="{rel}assets/css/style.css">
</head>
<body>

<header class="site-nav scrolled" id="siteNav">
  <a href="{loc['home']}" class="nav-logo"><img src="{rel}assets/img/logo-nav.png" srcset="{rel}assets/img/logo-nav@2x.png 2x" alt="felipe · atelier" width="175" height="44"></a>
  <nav>
    <ul class="nav-links" id="navLinks">
{nav_links}
      <li><a href="{other_link}" class="lang-switch">{loc['other_lang']}</a></li>
    </ul>
  </nav>
  <button class="nav-toggle" id="navToggle" aria-label="{loc['menu']}">
    <span></span><span></span><span></span>
  </button>
</header>

<main class="case-main">
  <article class="project">
    <div class="container project-inner">
      <p class="case-back"><a href="../">{loc['back']}</a></p>
      <div class="project-head reveal is-visible">
        <div class="project-index">{n}</div>
        <h1 class="case-title">{name}</h1>
        <div class="project-tags">{tags_html}</div>
      </div>
      <div class="project-meta reveal is-visible">
{meta_html}
      </div>

      <div class="project-hero reveal is-visible">{img_tag(p['hero'], d['hero_alt'], rel, lazy=False, hero=True)}</div>

      <div class="project-body reveal">
        <div class="project-text">
{text_html}
        </div>
        <blockquote class="project-quote">{d['quote']}{cite_html}</blockquote>
      </div>
{gallery_html}
      <section class="case-process">
        <div class="eyebrow reveal">{loc['process_eyebrow']}</div>
        <h2 class="case-process-title reveal">{loc['process_title']}</h2>
        <div class="project-gallery {process_cols} case-process-gallery reveal">
{process_imgs}
        </div>
      </section>

      <div class="project-footer reveal">
        <div class="project-participation"><b>{loc['participation_label']}</b><br>{d['participation']}</div>
        <div class="credit">{d['credit']}</div>
      </div>

      <nav class="project-nav">
        <a class="prev" href="../{prev_p['slug']}/"><b>{loc['prev']}</b>← {prev_name}</a>
        <a class="next" href="../{next_p['slug']}/"><b>{loc['next']}</b>{next_name} →</a>
      </nav>
    </div>
  </article>
</main>

<footer class="case-footer">
  <div class="container">
    <div class="case-footer-inner">
      <span>{loc['contact_line']}</span>
      <span class="colophon">{loc['footer_note']}</span>
    </div>
  </div>
</footer>

<div class="lightbox" id="lightbox">
  <button class="lightbox-close" id="lightboxClose" aria-label="{loc['close']}">✕</button>
  <button class="lightbox-nav lightbox-prev" id="lightboxPrev" aria-label="{loc['prev_img']}">‹</button>
  <button class="lightbox-nav lightbox-next" id="lightboxNext" aria-label="{loc['next_img']}">›</button>
  <figure class="lightbox-figure">
    <img src="" alt="" id="lightboxImg">
    <figcaption class="lightbox-caption" id="lightboxCaption"></figcaption>
  </figure>
</div>

<script src="{rel}assets/js/main.js"></script>
</body>
</html>
"""



# ---------------------------------------------------------------- index pages
CATS = {  # slug -> (category key, built?)
  "mcentral-park":  ("retrofit", False),
  "casa-noor":      ("residencial", True),
  "estande-florata":("comercial", True),
  "casa-lisa":      ("retrofit", False),
  "casa-fs":        ("residencial", False),
  "casa-vertice":   ("residencial", False),
}

IDX = dict(
 pt=dict(
   path="projetos/index.html", rel="../", home="../",
   title="Projetos — Felipe Atelier",
   desc="Todos os projetos de Felipe Sousa — residenciais, comerciais, retrofit e paisagismo, do croqui ao executivo.",
   canonical="projetos/", other="en/projects/",
   nav=[("#sobre","Sobre"),("","Projetos"),("#concursos","Concursos"),("#arte","Arte"),("#contato","Contato")],
   other_lang="EN",
   eyebrow="Trabalho selecionado · 2019 — 2026", h1="Projetos.",
   lede="Seis projetos, um mesmo olhar sobre materialidade, escala e luz — cada um com estudo completo, do croqui ao executivo.",
   views=("Grade","Lista"), cta="Estudo completo →", count_word="projetos",
   og_locale="pt_BR", menu="Abrir menu",
 ),
 en=dict(
   path="en/projects/index.html", rel="../../", home="../",
   title="Projects — Felipe Atelier",
   desc="All projects by Felipe Sousa — residential, commercial, retrofit and landscape, from sketch to construction set.",
   canonical="en/projects/", other="projetos/",
   nav=[("#about","About"),("","Projects"),("#competitions","Competitions"),("#art","Art"),("#contact","Contact")],
   other_lang="PT",
   eyebrow="Selected work · 2019 — 2026", h1="Projects.",
   lede="Six projects, one gaze on materiality, scale and light — each with a full case study, from sketch to construction set.",
   views=("Grid","List"), cta="Full case study →", count_word="projects",
   og_locale="en_US", menu="Open menu",
 ),
)

def index_page(lang):
    loc = IDX[lang]
    rel = loc["rel"]
    url = f"{SITE}/{loc['canonical']}"
    pt_url = f"{SITE}/projetos/"
    en_url = f"{SITE}/en/projects/"
    nav_links = "\n".join(
        f'      <li><a aria-current="page" href="./">{t}</a></li>' if h == ""
        else f'      <li><a href="{loc["home"]}{h}">{t}</a></li>'
        for h, t in loc["nav"])
    other_link = f"{rel}{loc['other']}"

    cards, rows = [], []
    for i, p in enumerate(PROJECTS):
        d = p[lang]
        name = p.get("en_name", p["name"]) if lang == "en" else p["name"]
        n = f"{i+1:02d}"
        cat, built = CATS[p["slug"]]
        typ = d["meta"][1][1]
        data = f'data-cat="{cat}" data-built="{"1" if built else "0"}"'
        cards.append(f'''      <article class="idxcard" {data}>
        <a href="{p['slug']}/">
          <div class="idxcard-media">{img_tag(p['hero'], d['hero_alt'], rel)}</div>
          <div class="idxcard-info">
            <span class="idxcard-line"><span class="idx-n">{n}</span> · {p['year']} · {d['status']}</span>
            <h2>{name}</h2>
            <p>{d['desc']}</p>
            <span class="project-card-cta">{loc['cta']}</span>
          </div>
        </a>
      </article>''')
        rows.append(f'''      <a href="{p['slug']}/" {data}>
        <span class="idx-n">{n}</span>
        <span class="idx-name">{name}</span>
        <span class="idx-year">{p['year']}</span>
        <span class="idx-type">{typ}</span>
        <span class="idx-status">{d['status']}</span>
      </a>''')
    cards_html = "\n".join(cards)
    rows_html = "\n".join(rows)
    g, l = loc["views"]

    return f'''<!doctype html>
<html lang="{"pt-BR" if lang == "pt" else "en"}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{loc['title']}</title>
<meta name="description" content="{loc['desc']}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="pt-BR" href="{pt_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{pt_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{loc['title']}">
<meta property="og:description" content="{loc['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta property="og:locale" content="{loc['og_locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/svg+xml" href="{rel}assets/img/favicon.svg">
<link rel="apple-touch-icon" href="{rel}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="{rel}assets/css/style.css">
</head>
<body>

<header class="site-nav scrolled" id="siteNav">
  <a href="{loc['home']}" class="nav-logo"><img src="{rel}assets/img/logo-nav.png" srcset="{rel}assets/img/logo-nav@2x.png 2x" alt="felipe · atelier" width="175" height="44"></a>
  <nav>
    <ul class="nav-links" id="navLinks">
{nav_links}
      <li><a href="{other_link}" class="lang-switch">{loc['other_lang']}</a></li>
    </ul>
  </nav>
  <button class="nav-toggle" id="navToggle" aria-label="{loc['menu']}">
    <span></span><span></span><span></span>
  </button>
</header>

<main class="case-main">
  <div class="container">
    <div class="section-head reveal is-visible">
      <div class="eyebrow">{loc['eyebrow']}</div>
      <h1 class="case-title">{loc['h1']}</h1>
      <p class="lede">{loc['lede']}</p>
    </div>

    <div class="idx-toolbar reveal is-visible">
      <span class="idx-count">06 {loc['count_word']}</span>
      <div class="idx-views">
        <button class="chip view-btn active" data-view="grid">{g}</button>
        <button class="chip view-btn" data-view="list">{l}</button>
      </div>
    </div>

    <div class="idx-grid" id="idxGrid">
{cards_html}
    </div>

    <div class="work-index idx-list" id="idxList" hidden>
{rows_html}
    </div>
  </div>
</main>

<footer class="case-footer">
  <div class="container">
    <div class="case-footer-inner">
      <span>{L[lang]['contact_line']}</span>
      <span class="colophon">{L[lang]['footer_note']}</span>
    </div>
  </div>
</footer>

<script src="{rel}assets/js/main.js"></script>
<script>
(function() {{
  var grid = document.getElementById('idxGrid');
  var list = document.getElementById('idxList');
  document.querySelectorAll('.view-btn').forEach(function(b) {{
    b.addEventListener('click', function() {{
      document.querySelectorAll('.view-btn').forEach(function(x) {{ x.classList.remove('active'); }});
      b.classList.add('active');
      var isGrid = b.dataset.view === 'grid';
      grid.hidden = !isGrid;
      list.hidden = isGrid;
    }});
  }});
}})();
</script>
</body>
</html>
'''

def main():
    for lang in ("pt", "en"):
        for i, p in enumerate(PROJECTS):
            out_dir = os.path.join(L[lang]["dirname"], p["slug"])
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "index.html"), "w") as f:
                f.write(page(lang, i, p))
            print("wrote", out_dir)
    for lang in ("pt", "en"):
        path = IDX[lang]["path"]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(index_page(lang))
        print("wrote", path)

if __name__ == "__main__":
    main()
