from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

# A model is the single, definitive source of information about your data. 
# It contains the essential fields and behaviors of the data you’re storing. 
# Django follows the DRY Principle. The goal is to define your data model in one
# place and automatically derive things from it.



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# Aqui, cada modelo é representado por uma classe derivada da classe 
# django.db.models.Model. Cada modelo possui alguns atributos de classe, as 
# quais por sua vez representa um campo do banco de dados no modelo.

# Cada campo é representado por uma instância de uma classe Field – por exemplo, 
# CharField para campos do tipo caractere e DateTimeField para data/hora. 
# Isto diz ao Django qual tipo de dado cada campo contém.

# O nome de cada instância Field (por exemplo question_text ou pub_date) é o 
# nome do campo, em formato amigável para a máquina. Você irá usar este valor 
# no seu código Python, e seu banco de dados irá usá-lo como nome de coluna.

# Você pode usar um argumento opcional na primeira posição de um Field para 
# designar um nome legível para seres humanos o qual será usado em uma série de 
# partes introspectivas do Django, e também servirá como documentação. Se esse 
# argumento não for fornecido, o Django utilizará o nome legível para máquina. 
# Neste exemplo nós definimos um nome legível para humanos apenas para 
# Question.pub_date. Para todos os outros campos neste modelo, o nome legível 
# para máquina será utilizado como nome legível para humanos.

# Algumas classes de Field possuem elementos obrigatórios. O CharField, por 
# exemplo, requer que você informe a ele um max_length que é usado não apenas no 
# esquema do banco de dados, mas na validação, como nós veremos em breve.

# Um Field pode ter vários argumentos opcionais; neste caso, definimos o valor 
# default de votes para 0.

# Finalmente, note que uma relação foi criada, usando ForeignKey. Isso diz ao 
# Django que cada Choice está relacionada a uma única Question. O Django oferece 
# suporte para todos os relacionamentos comuns de um banco de dados: 
# muitos-para-um, muitos-para-muitos e um-para-um.

# Aquela pequena parte do modelo fornece ao Django muita informação. Com ela o 
# Django é capaz de:

# Criar um esquema de banco de dados (instruções CREATE TABLE) para a aplicação.
# Criar uma API de acesso a banco de dados para acessar objetos Question e 
# Choice.
# Mas primeiro nós precisamos dizer ao nosso projeto que a aplicação polls está 
# instalada.

# Para incluir a aplicação no nosso projeto, precisamos adicionar a referência à 
# classe de configuração da aplicação na configuração INSTALLED_APPS . A classe 
# PollsConfig está no arquivo polls/apps.py, então seu caminho pontuado é 
# 'polls.apps.PollsConfig'. Edite o arquivo mysite/settings.py e adicione aquele 
# caminho com notação de ponto a configuração INSTALLED_APPS. 

