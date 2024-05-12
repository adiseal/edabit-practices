def reverse_complement(rna):
    complement = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement[base] for base in reversed(rna))
