# -*- coding: utf-8 -*-
# Script de testes - Python - corretor de provas
# João Paulo F. Guimarães -  29/06/2015
# joao.guimaraes@ifrn.edu.br

#para o system clear
import os

#Classe prova
class prova:
	objetivas_certas = []
	objetivas_erradas = []
	subjetivas = []
	def nota_objetiva(self):
		return len(self.objetivas_certas) - len(self.objetivas_erradas)


#Classe Aluno - guarda as informações básicas de cada aluno que fez a prova
class aluno:
	matricula = 0
	nome = ""
	email = ""
	acertos = -1
	p = prova()
	
	def __init__(self,nome,email,matricula):
		self.matricula = str(matricula)
		self.nome = nome
		self.email = email
	def imprimir(self):
		print "Nome: ", self.nome
		print "Matrícula: ", self.matricula
		print "email: ", self.email
		print "--------------------------"
		
	def salvar(self):
		string = "--------------------------\n" + "Nome: "
		string = string + self.nome
		string = string + "\nMatricula: "
		string = string + str(self.matricula)
		string = string + "\nEmail: "
		string = string + str(self.email)
		string = string + "\nNota Objetiva: "
		string = string + str(self.p.nota_objetiva())
		string = string + "\nSubjetivas: "
		string = string + str(self.p.subjetivas)

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

#Gabiarra do naosei - Falha no unicode
naosei = perguntas[0]

#Array contendo lista com os objetos alunos
alunos = []
for prova_aluno in respostas:
	
	#Objeto aluno auxiliar com os dados pessoais dos aluno
	aluno_aux = aluno(prova_aluno[1],prova_aluno[2],int(prova_aluno[3]))
	alunos.append(aluno_aux)

escolha = 0
for aluno in alunos:
	print "[", escolha, "]" 
	aluno.imprimir()
	escolha = escolha+1
	print "\n"
aluno = int(raw_input( "Selecione o aluno que você deseja avaliar\n"))	

#Questões objetiva
for i in lista_de_questoes_objetivas:	
	print "\n"
	print "Pergunta: ", perguntas[i]
	print "Resposta aluno: ", prova_aluno[i]			
	print "Gabarito: ", gabarito[i]
	if(prova_aluno[i] == gabarito[i]):
		alunos[aluno].p.objetivas_certas.append(i)
	else:
		if(prova_aluno[i] != naosei ):
			alunos[aluno].p.objetivas_erradas.append(i)
	print "\n"

#Questões subjetivas	
for i in lista_de_questoes_subjetivas:
	os.system("clear")
	print i, "Questão subjetiva"
	print "Pergunta: ", perguntas[i]
	print "\nResposta aluno: ", prova_aluno[i]			
	nota = raw_input( "Qual a nota da questão 0-10?\n")
	tupla_aux = [i,nota]
	alunos[aluno].p.subjetivas.append(tupla_aux)
	os.system("clear")

arquivo = open('relatorio.repo', 'a')
arquivo.write(str(alunos[aluno].salvar()))
arquivo.write("\n")
arquivo.close()




