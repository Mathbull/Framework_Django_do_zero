<h1 align="center">[INTRODUÇÃO AOS MODELS]</h1>

Nessa aula abrdamos sobre modelos de dados, ORM e migrações, demonstrando como criar e manipular modelos, além de exibir dados em templates

<h2>Atividades realixadas</h2>

- Introdução ao ORM e models
- Migração de dados 
- Reversão de modelos
- criar um model
- criando uma question no terminal:
```
(InteractiveConsole)
>>> from polls.models import Question
>>> Question.object.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Question' has no attribute 'object'
>>> Question.objects.all()
<QuerySet []>
>>> from datetime importe datetime
  File "<console>", line 1
    from datetime importe datetime
                    ^^^^^^^
SyntaxError: invalid syntax
>>> from datetime import datetime
>>> agora = datetime.now()
>>> question1 = Question(question_text="Qual é sua duvida?", pub_date=agora)
>>> question1.question_text
'Qual é sua duvida?'
>>> question1.id
>>> question1.save()
>>> question1.id
1
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
>>> quit
Use quit() or Ctrl-Z plus Return to exit
>>> quit
```

- exibir dados em um template
