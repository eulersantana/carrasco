# -*- coding: utf-8 -*-
# Script de testes - Python - corretor de provas
# João Paulo F. Guimarães -  29/06/2015
# joao.guimaraes@ifrn.edu.br

#Classe Aluno - guarda as informações básicas de cada aluno que fez a prova
class aluno:
	matricula = 0
	nome = ""
	email = ""
	acertos = -1
	
	def __init__(self,nome,email,matricula):
		self.matricula = str(matricula)
		self.nome = nome
		self.email = email
	def imprimir(self):
		print "--------------------------\n"
		print "Nome: ", self.nome
		print "Matrícula: ", self.matricula
		print "email: ", self.email
		print "acertos: " , self.acertos
	def salvar(self):
		string = "--------------------------\n" + "Nome: "
		string = string + self.nome
		string = string + "\nMatricula: "
		string = string + self.matricula
		string = string + "\nEmail: "
		string = string + self.email
		string = string + "\Nota Objetiva: "
		string = string + self.acertos

		return string
		
	
#Importe da ferramente de trabalhar com excel
import xlrd

#Interface com a planilha
def xlread(arq_xls):
    # Abre o arquivo
    xls = xlrd.open_workbook(arq_xls)
    # Pega a primeira planilha do arquivo
    plan = xls.sheets()[0]

    # Para i de zero ao numero de linhas da planilha
    for i in xrange(plan.nrows):
        # Le os valores nas linhas da planilha
        yield plan.row_values(i)


#Copiando respostas da planilha para o array linhas
linhas = []
for linha in xlread("t.xlsx"):
	linhas.append(linha)


#Copiando perguntas - primeira linha da planilha
perguntas = linhas[0]

#Copiando respostas do alunos
respostas = []
for i in range(1,len(linhas)-1):
	respostas.append(linhas[i])

#Copiando respostas - gabarito na última linha da planilha
gabarito = linhas[len(linhas)-1]

#Metadados prova
lista_de_questoes_objetivas = [5,6,7,8,9,10,11] 
lista_de_questoes_subjetivas = [4,12,13,14,15,16,17] 

#Variável auxiliar para dar as notas aos alunos
nota_objetiva = 0

#Gabiarra do naosei - Falha no unicode
naosei = perguntas[0]

#Array contendo lista com os objetos alunos
alunos = []
for prova_aluno in respostas:
	
	#Objeto aluno auxiliar com os dados pessoais dos aluno
	aluno_aux = aluno(prova_aluno[1],prova_aluno[2],int(prova_aluno[3]))

	#Questão objetiva	
	for i in lista_de_questoes_objetivas:
		print "\n"
		print "Pergunta: ", perguntas[i]
		print "Resposta aluno: ", prova_aluno[i]			
		print "Gabarito: ", gabarito[i]
		if(prova_aluno[i] == gabarito[i]):
			nota_objetiva = nota_objetiva+1
		else:
			if(prova_aluno[i] != naosei ):
				nota_objetiva = nota_objetiva-1
				print prova_aluno[i]			
		print "\n"
	#Questões subjetivas	
	for i in lista_de_questoes_subjetivas:
		print "\n"	
		print i, "Questão subjetiva"
		print "Pergunta: ", perguntas[i]
		print "Resposta aluno: ", prova_aluno[i]			
		nota_aux = raw_input( "Qual a nota da questão 0-10?")
	
	#incluindo na lista de alunos	
	aluno_aux.acertos = nota_objetiva
	alunos.append(aluno_aux)	
	nota_objetiva = 0;

	arquivo = open('Relatório.repo', 'w')
	arquivo.write(aluno_aux.salvar())
	arquivo.close()
	

	
	

for aluno in alunos:
	aluno.imprimir()
	



