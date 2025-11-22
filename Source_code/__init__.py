# File: main.py
import sys
from genetics import analyzer
# You would import the other modules here too:
# from genetics import central_dogma, manipulater
from utils import validators

def main():
    print("--- Gene-Tool: DNA Sequence Analyzer ---")
    
    while True:
        print("\nMAIN MENU")
        print("1. Calculate GC Content")
        print("2. Transcribe to RNA (Coming Soon)")
        print("3. Exit")
        
        choice = input("Select option (1-3): ")
        
        if choice == '1':
            user_seq = input("\nEnter DNA Sequence: ")
            
            # Error Handling Strategy [cite: 41]
            if validators.is_valid_dna(user_seq):
                result = analyzer.calculate_gc_content(user_seq)
                print(f"Success! GC Content: {result}%")
            else:
                print("ERROR: Invalid DNA sequence. Please use only A, T, C, G.")
                
        elif choice == '3':
            print("Exiting Gene-Tool.")
            sys.exit()
            
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
