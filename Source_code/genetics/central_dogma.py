# File: genetics/central_dogma.py

def transcribe_dna_to_rna(dna_sequence):
    """
    Converts a DNA sequence to RNA by replacing Thymine (T) with Uracil (U).
    """
    if not dna_sequence:
        return ""
    
    # Standard Python string replacement
    rna_sequence = dna_sequence.upper().replace('T', 'U')
    
    return rna_sequence
