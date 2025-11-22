# File: main.py
import sys
from utils import validators
# Import all our new logic modules
from genetics import analyzer, central_dogma, manipulater

def main():
    print("--- Gene-Tool: DNA Sequence Analyzer ---")
    
    while True:
        print("\nMAIN MENU")
        print("1. Calculate GC Content")
        print("2. Transcribe to RNA")
        print("3. Get Reverse Complement")
        print("4. Exit")
        
        choice = input("Select option (1-4): ")
        
        if choice == '4':
            print("Exiting Gene-Tool.")
            sys.exit()

        # Input Phase
        user_seq = input("\nEnter DNA Sequence: ")
        
        # Validation Phase (Error Handling)
        if not validators.is_valid_dna(user_seq):
            print("ERROR: Invalid DNA sequence. Please use only A, T, C, G.")
            continue # Skips the rest and goes back to menu

        # Processing Phase
        if choice == '1':
            result = analyzer.calculate_gc_content(user_seq)
            print(f"RESULT: GC Content is {result}%")
            
        elif choice == '2':
            result = central_dogma.transcribe_dna_to_rna(user_seq)
            print(f"RESULT: RNA Sequence is {result}")
            
        elif choice == '3':
            result = manipulater.reverse_complement(user_seq)
            print(f"RESULT: Reverse Complement is {result}")
            
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()