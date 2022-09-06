""" Translating RNA into Protein
Usage: just run the script, there are no parameters.

Link to the problem solved in this file: https://rosalind.info/problems/prot/

Proteins are chains of smaller molecules called amino acids; 20 amino acids commonly appear in every species. Proteins
power every practical function carried out by the cell. Proteins are encoded in RNA sequences, groups of 3 nucleotides,
called codons, correspond to one aminoacid.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

"""

from pathlib import Path
from validations import is_na


def rna_to_protein(rna):
    """
    Translates an RNA string into it's corresponding protein.

    :param rna: An RNA sequence of length at most 10000 nt.
    :return: The corresponding protein string.
    """

    genetic_code = {
            'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
            'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
            'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
            'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
            'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
            'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R',
            'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 'CGA': 'R', 'AGA': 'R',
            'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G',
            'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
            }

    # search for the start codon in the RNA string and delete the nucleotides before it
    start_is_present = False
    for i in range(0, len(rna)-1):
        if rna[i:i+3] == 'AUG':
            rna = rna[i:]
            start_is_present = True
            break
    if not start_is_present:
        raise ValueError("Start codon not present in RNA string!")

    # search for the stop codon and delete it together with the nucleotides after it
    stop_codons = [k for k, v in genetic_code.items() if v == 'STOP']

    stop_is_present = False
    for i in range(0, len(rna)-1, 3):
        codon = rna[i:i+3]
        if codon in stop_codons:
            stop_is_present = True
            rna = rna[:i]
            break
    if not stop_is_present:
        raise ValueError("STOP codon not present in RNA string!")

    # convert rna to protein
    protein = ""
    for i in range(0, len(rna) - 1, 3):
        codon = rna[i:i+3]
        protein += genetic_code[codon]

    return protein


if __name__ == "__main__":

    # input data is provided as a file
    in_file = Path.cwd() / 'data' / '008_prot_dataset.txt'

    # extract the dna string from data file
    with open(in_file, 'r') as ref:
        s = ref.readline().strip()

    if is_na(s, 'rna'):
        try:
            print(f"The protein translated from the provided RNA sequence is:\n"
                  f"{rna_to_protein(s)}")
        except ValueError as err:
            print(err)
    else:
        print("Not a valid nucleic acid string.")
