<h1>Django do zero - Como criar um aplicativo Web</h1>

<h2>motivação</h2>

Reforçar o conhecimento que já possuo sobre Django

fundamentos Django

Rápido e produtivo

<h2>Objetivos</h2>

Criar uma aplicação de enquete

Aprender os fundamentos do Django 

Capacitar você implementar aplicativos Web

Tirar você do zero no Django


<h2>Requisitos</h2>
Computador + internet(windows ou linux)

Python 3.10

<h3>Desejável:</h3>

Experiência com computador: criar arquivos/pasta... se localizar dentro do SO

Noções de lógica de programação(tipos de dados, variáveis, laõs de repetições, variáveis vetores e matriz, estrutura de decisão).

Noções de linguagem Python (orientação a objetos, indentação dos blocos código)

Noções de HTML + CSS

<h2>Tópicos gerais de estudos</h2>

<ol>
    <li>Introdução a Web Framework e ao Django
        <details>
            <summary>Framework na progrmação?</summary>
            É um conjunto dde bilbliotecas especiamente organizadas que servem de arcabouço(estrutura, esquelento) para
            projetos de software.<br>
            Um framwork de programação permite encapsular implentações complexas em um formato mais fácil e adaptável para uso. Por exemplo: Bootstrap(para css)
        </details>
        <details>
            <summary>Vantagens dos Framewoks</summary>
            A principal vantagem é agregar rotinas, funções, modelos e recursos já implemntados. Este fato acelera muito o desenvolvimento de solução simples ou complexas
        </details>
        <details>
            <summary>Desvantagens dos Frameworks</summary>
            Direcionam o estilo, exigem seguir um <strong>padrão rigoroso</strong><br>
            Convenções e configurações se sobrepôem á criatividade do programador na solução de determinados problemas.<br>
            O desenvolvedor deve conhecer como ele funciona, ele pode limitar determindas necessidades que o framework não suporta nativamente
        </details>
        <details>
            <summary>MVC - Model, view e Controller</summary>
            MVC (Model, view e Controller) é a arquitetura adorada pela maior parte dos frameworks de desenvolvimento Web. <br>
            Divide o sistema em <strong>camadas</strong>, de forma que possam <strong>trabalhar em conjunto</strong> mas sendo independentes ao mesmo tempo. <br>
            Permite algo grau de <strong>reaproveitamento</strong> e a integrações das equipes(programadores) especializados em cada camada
        </details>
        <details>
            <summary>Django - um Framewok Web</summary>
            O django é um framework web full stack open source (código aberto) escrito em Python, gratuito e de alto nível.<br>
            O Django habilita o programador a construir de forma rápida sistemas que usam pouco código.<br>
            Um projeto Django se divide em pequenas aplicações baseadas no modelo MVT (model, view e Templates)
        </details>
        <details>
            <summary>principais Caraterísticas - Django</summary>
            Desenvolvimento rápido de aplicações WEB;<br>
            Incluí toda a base para o sistema: autenticação, área administrativa, formulários, rotas, sistemas de templates, etc; <br>
            Poderoso ORM (Object Relational Mapper);<br>
            Robustez comprovada pelo tempo;<br>
            Focado em Seguranã e manutenibilidade;<br>
            Portável pois usa a linguagem Python; <br>
        </details>
        <details>
            <summary>Principios - Django</summary>
            <strong>KISS*</strong> (Keep it simples and stupid);<br>
            <strong>DRY</strong> (dont't repeat yourself);<br>
            Models "encorpado", e views "enxutas";<br>
            Colocar o mínimo possível da <strong>Lógica de negócio</strong> no templates;<br>
            Criar apps "pequenos" e reutilizaveis;<br>
        </details>
         <details>
            <summary>arquivos importantes do Projeto</summary>
            <strong>settings.py</strong><br>
            É o aquivo de configuração do sistema/projeto Django: conexão com bancos de dados, apps instalados e ativos, métodos e formatos de cache, logs, etc.<br>
            <strong>urls.py</strong><br>
            O arquivo urls.py do projeto mapeaia as rotas do sistemas<br>
            <strong>manage.py</strong><br>
            É o script administrativo do sistema/projeto Django. Através deke se executa manutenção dos dados e diversas outras importantes como criação de usuário administrador.<br>
        </details>
         <details>
            <summary>Estrutura de um App Django</summary>
            `django-admin startapp produtos`<br>
            Tipicamente dentro da pasta do App existirá uma pasta <strong>templates</strong> com os arquivos HTML (com as marcações específicas do Django).<br>
            Em geral, cada <strong>módulo ou funcionamento</strong> terá um App próprio, exemplo: produtos, pedidos, clientes, etc. <br>
            <strong>Arquivos importantes do App</strong><br>
            <strong>models.py</strong><br>
            É o arquivo onde será descrita no formato de classes os modelos de dados do App, incluindo as regras de negócio.<br>
            <strong>views.py</strong><br>
            Contém as funções que transformam uma requisição HTTP em uma resposta (HTML, JSON, xls, txt, pdf, etc).<br>
            <strong>migrations</strong><br>
            É a parte onde o Django manterá o versionamento dos modelos dos dados do App. É gerenciado automaticamente com pouca ou nem uma intervenção do desenvolvedor.<br>
        </details>
    </li>
    <li>Preparação do ambiente de trabalho</li>
    <li>1º aplicação "Olá Django"</li>
    <li>Indrodução aos Templates</li>
    <li>Introdução aos modelos de dados e micração de dados</li>
    <li>Área administrativa</li>
    <li>Introdução ás views e rotas</li>
    <li>Responstas em formato JSON(exemplo API)</li>
    <li>Hospedagem do sistema na internet</li>
    <li>Implementação de um CRUD básico: CREATE</li>
    <li>Implementação de um CRUD básico: READ</li>
    <li>Introdução aos Forms</li>
    <li>Atualização do sistema hospedado na internet</li>
    <li>Implementação de um CRUD básico: UPDATE</li>
    <li>Implementação de um CRUD básico: Delete</li>
    <li>Upload de arquivos</li>
    <li>LOgin e controle de acesso </li>
    <li>Relacionamento 1 para N entre modelos</li>
    <li>Envio de E-mails pelo sistema</li>
    <li>Relacionamento N para N entre Models</li>
</ol>
    