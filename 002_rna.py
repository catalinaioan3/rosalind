""" Transcribing DNA into RNA
Usage: just run the script, there are no parameters.

Link to the problem solved in this file: https://rosalind.info/problems/rna/

A DNA sequence is an ordered collection of symbols from the alphabet 'A', 'C', 'G', 'T' used to represent nucleotides
adenine, cytosine, guanine, thymine. For RNA strings the letter 'T' is replaced by 'U' for nucleotide uracil.
In the process of DNA sequencing, the sequencing machine produces files with DNA strings that respect the FASTA format.
Sometimes the sequencer is not able to confidently identify a nucleotide and has specific symbols to represent partial
information.
In this program all unidentified or partially identified nucleotides will be counted as a general nucleotide, N.

Transcription is the process by which the information in a strand of DNA is copied into a new molecule of
messenger RNA (mRNA). It consists of copying the 'A', 'C', 'G' nucleotides and converting the 'T' nucleotides in 'U'.

Given: A DNA sequence s of length at most 1000 nt.
Return: The transcribed RNA sequence of t.

"""

from pathlib import Path
from validations import is_na


def dna_to_rna(dna):
    """
    Transcribes a DNA sequence into the corresponding RNA sequence.

    :param dna: A DNA sequence
    :return: The transcribed RNA sequence
    """

    # this is the shortest version to solve this task, below will be another 2 versions
    rna = dna.replace('T', 'U')

    return rna


# a second solution for the same task
def dna_to_rna_v2(dna):
    rna = ''
    for i in dna:
        if i == "T":
            rna += "U"
        else:
            rna += i

    return rna


# a third solution for the same task
def dna_to_rna_v3(dna):
    rna = ''
    for i in range(0, len(dna)):
        if dna[i] == 'T':
            rna += 'U'
        else:
            rna += dna[i]

    return rna


if __name__ == "__main__":

    # input data is provided as a file
    in_file = Path.cwd() / 'data' / '002_rna_dataset.txt'

    # extract the dna string from data file
    with open(in_file, 'r') as ref:
        s = ref.readline().strip()

    if is_na(s, 'dna'):
        t = dna_to_rna(s)
        print(f"The transcribed RNA sequence for the provided DNA is: \n"
              f"{t}")
    else:
        print("Not a valid DNA string.")
