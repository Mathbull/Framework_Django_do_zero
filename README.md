<h1 align="center">[INTRODUÇÃO A TEMPLETES]</h1>

<H2>Conteúdo abordado:</H2>

- É usado o _ para caso em que o template não será o renderizado, mas será um complemento

- Estrutura de templates para reutilização _base.html

- templete de layout genérico _leyout1.html (Servirá de base para todo o desing do sitemea)
 
- Usa o Jinja (gerenciador de templete, junta partes estáticas com partes dinâmicas de acordo com o banco de dados ou depender da sua lógica):
  
{{ }} => imprime valores de variáveis<br>
    {% %} => execultar comandos:<br>
        {% if var %}<br>
            <a></a><br>
        {% else %}<br>
        {% endif %}<br>
    {# #} => comentários<br>
    
- Aplicar o layout genérico em um templete final
  
- Arquivos estáticos ( imagens, CSS, JS e qualquer outro arquivo que não muda)
  
- implementação do collectstatic para gerenciamento de arquivo em para um futuro cenario de produção.
  
- Usar aquivo estático: favicon
