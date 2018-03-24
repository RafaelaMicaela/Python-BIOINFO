with open("rosalind_dna.txt") as f:
	  read_data = f.read()
dna = int()

print(" Rosalind DNA ")
print("Quantidade de Amostras do DNA: %d" % len(dna))
print("Quantidade de Adenina: %d" % dna.cout('A'))
print("Quantidade de Timina: %d" % dna.cout('T'))
print("Quantidade de Guanina: %d" % dna.cout('G'))
print("Quantidade de Citosina: %d" % dna.cout('C'))

f.close()