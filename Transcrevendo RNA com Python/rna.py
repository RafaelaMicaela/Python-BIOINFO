with open("rosalind_rna.txt") as f:
	read_data = f.read()
rna = int()
print(" Rosalind RNA")
print("Quantidade de Amostras de DNA: "'{:d}'.format(len(rna)))
print("Quantidade de Adenina: " '{:d}'.format(rna.count('A')))
print("Quantidade de Timina: " '{:d}'.format(rna.count('T')))
print("Quantidade de Guanina: "'{:d}'.format(rna.count('G')))
print("Quantidade de Citosina: "'{:d}'.format(rna.count('C')))

print("-----------------------------------------------")
print("Substituindo amostras de Timina por Uracila...")
print("-----------------------------------------------")

rna = rna.replace('T', 'U')
print("Quantidade de Amostras de RNA: "'{:d}'.format(len(rna)))
print("Quantidade de Adenina: "'{:d}'.format(rna.count('A')))
print("Quantidade de Uracila: "'{:d}'.format(rna.count('U')))
print("Quantidade de Guanina: " '{:d}'.format(rna.count('G')))
print("Quantidade de Citosina: "'{:d}'.format(rna.count('C')))

f.close()