# File: utils/validators.py

def is_valid_dna(sequence):
    """
    Checks if the sequence contains only valid DNA characters (A, T, C, G).
    Returns True if valid, False otherwise.
    """
    valid_bases = {'A', 'T', 'C', 'G'}
    
    # Convert to uppercase to handle 'atcg' input
    upper_seq = sequence.upper()
    
    # Set logic: if we find any character NOT in valid_bases, return False
    for base in upper_seq:
        if base not in valid_bases:
            return False
            
    return True