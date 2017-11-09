from Bio import SeqIO
import sys
import random

#label matrix of k-mers with taxonmic rank, from class to genus
#parameters: argv[1] = matrix of k-mers, as generated by fasta2matrix script; arg[2] = taxonomy file (e.g. taxonomy.txt")
nome=sys.argv[1].split(".")[0]

outputFileClass = open(nome+"_C.txt", "w")
outputFileOrder = open(nome+"_O.txt", "w")
outputFileFamily = open(nome+"_F.txt", "w")
outputFileGenus = open(nome+"_G.txt", "w")
matrix = list(open(sys.argv[1], "r"))
records= open(sys.argv[2], "r") 
outputFileGenus.write(matrix[0])
outputFileFamily.write(matrix[0])	
outputFileOrder.write(matrix[0])
outputFileClass.write(matrix[0])
matrix=matrix[1:]
for seq in records:
	elements=seq.split(" ")
	sequ=elements[0][1:]
	classe=elements[1]
	ordine=elements[2]
	famiglia=elements[3]
	genere=elements[4]
	matrix = open(sys.argv[1], "r")
	for line in matrix:
		sequ2num=line.split(",")[0];
		#print (sequ2num)
		sequ2=sequ2num.split("-")[0];
		if (sequ == sequ2):
			outputFileGenus.write(line.split("\n")[0]+","+genere)
			outputFileFamily.write(line.split("\n")[0]+","+famiglia+"\n")
			outputFileOrder.write(line.split("\n")[0]+","+ordine+"\n")
			outputFileClass.write(line.split("\n")[0]+","+classe+"\n")
