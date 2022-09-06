""" Complementing a Strand of DNA
Usage: just run the script, there are no parameters.

Link to the problem solved in this file: https://rosalind.info/problems/revc/

DNA complementarity is a property shared between two DNA sequences, such that when they are aligned antiparallel
(oriented in opposite directions) to each other, the nucleotide bases at each position in the sequences will form bonds
between them and create the double helix structure of DNA.
Since there is only one complement for any nucleotide (A - T, C - G), a reverse complement string can be reconstructed
for any DNA string. The complementary string has to be reversed because DNA strings are always read from a specific end
(from a chemical point of view).

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.

"""

from pathlib import Path
from validations import is_na


def complementary_dna(dna):
    # DNA complementarity dictionary
    dna2cdna = {
            "A": "T",
            "C": "G",
            "G": "C",
            "T": "A"
            }

    cdna = ""
    for i in dna:
        # the new nucleotide is always added before de string obtained at the previous step
        # this way the complementary string is constructed from de end nucleotide to the first
        cdna = dna2cdna[i] + cdna

    return cdna


# a second solution for the same task
def complementary_dna_v2(dna):
    dna2cdna = {'A': 'T',
                'C': 'G',
                'G': 'C',
                'T': 'A'
                }
    cdna = ''
    for i in dna:
        cdna += dna2cdna[i]
    # the new nucleotide is added at the end of the string and the string is reversed in a different step
    return cdna[::-1]


if __name__ == "__main__":

    # input data is provided as a file
    in_file = Path.cwd() / 'data' / '003_revc_dataset.txt'

    # extract the dna string from data file
    with open(in_file, 'r') as ref:
        s = ref.readline().strip()

    if is_na(s, 'dna'):
        sc = complementary_dna(s)
        print(f"The complementary DNA sequence for the provided DNA is: \n"
              f"{sc}")
    else:
        print("Not a valid DNA string.")
