# File: genetics/manipulater.py

def reverse_complement(dna_sequence):
    """
    Generates the reverse complement of a DNA strand.
    Example: 5'-ATCG-3' becomes 5'-CGAT-3'
    """
    upper_seq = dna_sequence.upper()
    
    # Dictionary mapping each base to its complement
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Step 1: Find complement for each base
    complement_bases = []
    for base in upper_seq:
        if base in complement_map:
            complement_bases.append(complement_map[base])
        else:
            # Should be caught by validator, but safe fallback
            complement_bases.append(base)
            
    # Step 2: Reverse the list and join back into a string
    # [::-1] is a python trick to reverse a list
    rev_comp_seq = "".join(complement_bases[::-1])
    
    return rev_comp_seq
