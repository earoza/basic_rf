[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


# Exemplo Básico de implementação Random Forest
![](https://img.shields.io/badge/python-3.6+-blue.svg)

Exemplo básico de um classificado Random Forest (RF), desenvivida com o intuito de aprofundar o conhecimento com relação ao desenvolvimento de árvores de decisão. 


# Getting started

- [Instalação das dependências](#instalacao-das-dependencias)
- [Dataset](#dataset)
- [Input](#input)	  
- [Execução](#execucao)
	- [Extração das informações](#extracao-das-informacoes)
- [Referencias](#referencias)
- [Contribuidores](#contribuidores)
----------------------------------


# Instalação das dependências

The following command allows to install the required dependencies:

```
 pip3 install -r requirements.txt
 ```

# Datasets 

O datasset selecionado foi o Digits da biblioteca SciKit-Learn (https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html).

# Input

O input para a rede se da por meio da variável digits, a qual contêm as informações de dígitos.

**digits** possui as seguintes informações:
- **DESCR**: Descrição do Dataset;
- **data**: Matriz de dados do dígito (gradiente);
- **images**: Imagem do dígito;
- **target**: Label de classificação do dígito;
- **target_names**: Target Nominal;


Para esse protótipo, será utilizado como 'Y', ou, variável de precição, o label de classificação **target**.

#  Execução

Para a exeução do protótipo, é necessário a utilização do comando no terminal

```
python3 main.py
```

Ou por meio do run do compilador utilizado

## Extração das informações

As informações são extraidos por meio da utilização da biblioteca pandas.


# Referencias

- 📖 [**Ref1**] [Machine Learning Tutorial Python - 11 Random Forest](https://www.youtube.com/watch?v=ok2s1vV9XW0)
# Contribuidores

- 👨‍💻 Enrique Augusto da Roza <a href="mailto:enriqueaugroza@gmail.com">:e-mail:</a>
