# File: genetics/analyzer.py

def calculate_gc_content(sequence):
    """
    Calculates the percentage of G and C bases in a DNA sequence.
    """
    seq = sequence.upper()
    total_bases = len(seq)
    
    if total_bases == 0:
        return 0.0
    
    g_count = seq.count('G')
    c_count = seq.count('C')
    
    gc_percent = ((g_count + c_count) / total_bases) * 100
    return round(gc_percent, 2)
