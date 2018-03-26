with open("rosalind_dna.txt") as f:
	  read_data = f.read()
dna = int()

print(" Rosalind DNA ")
print("Quantidade de Amostras do DNA: " '{:d}'.format(len(dna)))
print("Quantidade de Adenina: "'{:d}'.format(dna.cout('A')))
print("Quantidade de Timina: "'{:d}'.format(dna.cout('T')))
print("Quantidade de Guanina: " '{:d}'.format(dna.cout('G')))
print("Quantidade de Citosina: "'{:d}'.format(dna.cout('C')))

f.close()