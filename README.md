# Gene-Tool-DNA-Sequences-Analyser
A Python-based bioinformatics tool for analyzing DNA sequences. Features include GC content calculation, DNA-to-RNA transcription, and reverse complement generation.

## 1. Project Overview
**Gene-Tool** is a Bioengineering utility designed to automate fundamental tasks related to the "Central Dogma" of biology. Manual analysis of DNA sequences is prone to human error; this tool provides a reliable, automated solution for students and researchers to analyze genetic strings quickly and accurately.

## 2. Features
This project includes three meaningful functional modules:
* **GC Content Calculator:** Calculates the percentage of Guanine and Cytosine bases in a sequence to estimate DNA stability.
* **Transcriber (DNA to RNA):** Simulates the biological process of transcription by converting a DNA coding strand into Messenger RNA (mRNA).
* **Reverse Complement Generator:** Produces the complementary DNA strand in the 5'-to-3' direction, essential for PCR primer design.
* **Input Validation:** Ensures only valid DNA characters (A, T, C, G) are processed.

## 3. Technologies Used
* **Language:** Python 3.x
* **Concepts:** String Manipulation, Modular Programming, Flow Control, Error Handling.

## 4. How to Install and Run
Follow these steps to run the project on your local machine:
Once the program is running, follow the on-screen menu:
Test GC Content:
Select Option 1.
Input: ATCG
Expected Output: 50.0%

Test Transcription:
Select Option 2.
Input: AATTCG
Expected Output: AAUUCG

Test Reverse Complement:
Select Option 3.
Input: ATCG
Expected Output: CGAT

Test Error Handling:
Enter random text like HELLO.
Expected Output: ERROR: Invalid DNA sequence.
### Prerequisites
* Ensure **Python 3** is installed on your system.

### Installation
1.  Clone or download this repository.
2.  Open your terminal/command prompt.
3.  Navigate to the project directory:
    ```bash
    cd GeneTool_Project
    ```

### Running the Application
Run the main script using Python:
```bash
python main.py
