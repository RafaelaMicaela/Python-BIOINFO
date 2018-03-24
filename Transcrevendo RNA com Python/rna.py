with open("rosalind_rna.txt") as f:
	read_data = f.read()
rna = int()
print(" Rosalind RNA")
print("Quantidade de Amostras de DNA: %d" % len(rna))
print("Quantidade de Adenina: %d" % rna.count('A'))
print("Quantidade de Timina: %d" % rna.count('T'))
print("Quantidade de Guanina: %d" % rna.count('G'))
print("Quantidade de Citosina: %d" % rna.count('C'))

print("-----------------------------------------------")
print("Substituindo amostras de Timina por Uracila...")
print("-----------------------------------------------")

rna = rna.replace('T', 'U')
print("Quantidade de Amostras de RNA: %d" % len(rna))
print("Quantidade de Adenina: %d" % rna.count('A'))
print("Quantidade de Uracila: %d" % rna.count('U'))
print("Quantidade de Guanina: %d" % rna.count('G'))
print("Quantidade de Citosina: %d" % rna.count('C'))

f.close()