sequencia = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
dataset = 'CGAAACGCTCTTCTTAAACGTCCTATACTATTGGCTCTAATTATGGTGGTGTAACCGCGCACGCCGCTTAAATTCAGCTAGCGTTCTCTGGGAAAGCTATTACCTTAAAGGCACCTGGTACATAGCGACGCGCAACGCCACTTGTATTAGACACTGAGTCGACCAGTTGTAGACACGACACACCACCCTATGAACACAGGCACTTGTGCACCGTCAACAGAGATCATACTCTCATACGATCAGGCACTTCACAGCTCCTGGGCAGGGGGCCCATCCGCACGTAATACAGGCTACTCAAAATTCACATGACATGCTCCTACGTCGTCTTGAGCGCTCGCCCTTGCTGGTGTTAAGTCTGCCACGTTAGCGGTCACCCCCCTTGTTCGGCCTATTCCTGCAGCTACTACATTGTAATAGAGACACCTACGCTTGGGAAGCATCTTGGAGGTGGCTCATGCGCCTGCATTGGGAAACACGTGCTACCGTGATCTTGAATTTGGTGAACACCCCCGCCTTATGTGGGCTAATCACTGATAGCTGACTTAATTGTCGCGCTCAAAGGAGTAGTGACGAGCAGGTGATAGGACTGTGAGGATCCTAGGAGACCTAAACCTACACTCTAGGGCAAGAGACTCCTCCATCTCTAGAATCAATCGTCCTTGCCCACATCTTCAAGGCGGCATGTCAAAATATGTATCCGGCAACAGTATATATAGAAAGCCCAGTGTTTATCATGCGGACGGTTGAAAGCAGGGTGCTGGTTAAACGCGTAATACTCAGAATATGATACTGGATCACGTGTAAAGAGTTTGGATAATTTGACACTTGGACTGGGCACAACTGTAGATTAATAGACCTCGTGAGCACACCCCTAACAAACTGGCCAAAGTCGACAAGATGCGCTTGGTTACTCAACTGGAACATCAGTAGAACGAAGTCTAGCTGAAT'
adenine = 0
cytosine = 0
guanine = 0
thymine = 0
for i in dataset:
    if i[0] == 'A':
        adenine = adenine + 1
    elif i[0] == 'C':
        cytosine = cytosine + 1
    elif i[0] == 'G':
        guanine = guanine + 1
    elif i[0] == 'T':
        thymine = thymine + 1
print(adenine,cytosine,guanine,thymine)
