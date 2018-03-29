f = open("/home/rafaela/Downloads/rosalind_dna (6).txt")
read_data = f.read()
a = []
for x in range(0, len(read_data)):
	a.insert(read_data[x],1)

print(a)



print(read_data.count('T'))


f.close()