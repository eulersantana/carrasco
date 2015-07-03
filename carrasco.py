# -*- coding: utf-8 -*-
# Script de testes - Python - corretor de provas
# João Paulo F. Guimarães -  29/06/2015
# joao.guimaraes@ifrn.edu.br
from __future__ import division
#para o system clear
import os

#Classe prova
class prova:
	objetivas_certas = []
	objetivas_erradas = []
	subjetivas = []
	nota_ob = 0
	nota_sub = 0
	peso_objetiva = 4
	peso_subjetiva = 6
	nota_final = 0
	def nota_objetiva(self):
		self.nota_ob = ((len(self.objetivas_certas) - len(self.objetivas_erradas))*10)/7
		return self.nota_ob
	def nota_subjetiva(self):
		for questao in self.subjetivas:
			self.nota_sub = self.nota_sub + int(questao[1])
		self.nota_sub = self.nota_sub/7
		return self.nota_sub
	def nota(self):
		x = self.nota_objetiva()
		y = self.nota_subjetiva()
		self.nota_final = (x*self.peso_objetiva + y*self.peso_subjetiva)/(self.peso_objetiva+self.peso_subjetiva)
		return self.nota_final
		


#Classe Aluno - guarda as informações básicas de cada aluno que fez a prova
class aluno:
	matricula = 0
	nome = ""
	email = ""
	acertos = -1
	p = prova()
	respostas = []
	def __init__(self,nome,email,matricula,respostas):
		self.matricula = str(matricula)
		self.nome = nome
		self.email = email
		self.respostas = respostas
		path = "correcoes"
		if not os.path.exists(path):
			os.mkdir(path)
		filename = self.nome[0] +  self.nome[1] + self.nome[2] + self.nome[3] + "_" + self.matricula + ".res"		
		self.arquivo = open(os.path.join(path,filename),'a')
	def imprimir(self):
		print "Nome: ", self.nome
		print "Matrícula: ", self.matricula
		print "email: ", self.email
		print "--------------------------"
		
	def salvar(self):
		self.arquivo.write("\n--------------------------\nNome: ")
		self.arquivo.write( self.nome.encode('utf-8') )
		self.arquivo.write( "\nMatricula: ")
		self.arquivo.write( self.matricula)
		self.arquivo.write( "\nEmail: ")
		self.arquivo.write( self.email)
		self.arquivo.write( "\nObjetivas certas: ")	
		self.arquivo.write( str(self.p.objetivas_certas))
		self.arquivo.write( "\nObjetivas erradas: ")	
		self.arquivo.write( str(self.p.objetivas_erradas))		
		self.arquivo.write( "\nNota Objetiva: ")
		self.arquivo.write( str(self.p.nota_objetiva()) )
		self.arquivo.write( "\nSubjetivas: ")
		self.arquivo.write( str(self.p.subjetivas) )
		self.arquivo.write( "\nNota Subjetiva: ")
		self.arquivo.write( str(self.p.nota_subjetiva()) )
		self.arquivo.write( "\nNota Avaliação: ")
		self.arquivo.write( str(self.p.nota()) )
		self.arquivo.close()	
		
	
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
lista_de_questoes_objetivas = [5,6,7,8,9,10,11] #7 objetivas
lista_de_questoes_subjetivas = [4,12,13,14,15,16,17] # 7 subjetivas

#Gabiarra do naosei - Falha no unicode
naosei = perguntas[0]

#Array contendo lista com os objetos alunos
alunos = []
for prova_aluno in respostas:
	
	#Objeto aluno auxiliar com os dados pessoais dos aluno
	aluno_aux = aluno(prova_aluno[1],prova_aluno[2],int(prova_aluno[3]),prova_aluno)
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
	print "Resposta aluno: ", alunos[aluno].respostas[i]			
	print "Gabarito: ", gabarito[i]
	if(alunos[aluno].respostas[i] == gabarito[i]):
		alunos[aluno].p.objetivas_certas.append(i)
	else:
		if(alunos[aluno].respostas[i] != naosei ):
			alunos[aluno].p.objetivas_erradas.append(i)
	print "\n"

#Questões subjetivas	
for i in lista_de_questoes_subjetivas:
	os.system("clear")
	print i, "Questão subjetiva - Aluno: ", alunos[aluno].respostas[1]
	print "Pergunta: ", perguntas[i]
	print "\nResposta aluno: ", alunos[aluno].respostas[i]		
	nota = raw_input( "Qual a nota da questão 0-10?\n")
	tupla_aux = [i,nota]
	alunos[aluno].p.subjetivas.append(tupla_aux)
	os.system("clear")


alunos[aluno].salvar()


