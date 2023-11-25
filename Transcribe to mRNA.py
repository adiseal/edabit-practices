def dna_to_rna(dna):
    trans_table = str.maketrans('ATGC', 'UACG')
    return dna.translate(trans_table)