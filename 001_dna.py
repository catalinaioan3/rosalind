""" Counting DNA Nucleotides
Usage: just run the script, there are no parameters.

Link to the problem solved in this file: https://rosalind.info/problems/dna/

A DNA sequence is an ordered collection of symbols from the alphabet 'A', 'C', 'G', 'T' used to represent nucleotides
adenine, cytosine, guanine, thymine. For RNA strings the letter 'T' is replaced by 'U' for uracil.
In the process of DNA sequencing, the sequencing machine produces files with DNA strings that respect the FASTA format.
Sometimes the sequencer is not able to confidently identify a nucleotide and has specific symbols to represent partial
information.
In this program all unidentified or partially identified nucleotides will be counted as a general nucleotide, N.

Given: A DNA sequence s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols
        ‘A’, ‘C’, ‘G’, and ‘T’ occur in s.

"""

from pathlib import Path
from validations import is_na


def nts_count_dna(dna) -> dict:
    """
    Counts the recurrence of nucleotides in a DNA sequence. All unidentified or partially identified nucleotides will be
    counted as N, a general nucleotide.

    :parameter dna: A DNA sequence of length at most 1000 nt.
    :returns: A dictionary containing all possible dna nucleotides and their recurrence in s
    """

    nts = {'A': 0,
           'C': 0,
           'G': 0,
           'T': 0,
           'N': 0
           }

    # for every nucleotide increase it's specific counter
    # if a nonstandard nucleotide is encountered increase N counter
    for i in dna.upper():
        if i in 'ACGT':
            nts[i] += 1
        else:
            nts['N'] += 1

    return nts


# to generalize this task, I create a function that counts nucleotides in all nucleic acids (both DNA and RNA)
def nts_count(na, na_type='dna'):
    """
    Counts the recurrence of nucleotides in a DNA/RNA sequence. All unidentified or partially identified nucleotides
    will be counted as N, a general nucleotide.

    :parameter na: A DNA/RNA sequence of length at most 1000 nt.
    :parameter na_type: a string with two accepted values, 'dna' and 'rna', specifying the type of nucleic acid provided
    :returns: A dictionary containing all possible nucleotides and their recurrence in s
    """

    nts = {'A': 0,
           'C': 0,
           'G': 0,
           'T': 0,
           'U': 0,
           'N': 0
           }

    for i in na.upper():
        if i in 'ACGTU':
            nts[i] += 1
        else:
            nts['N'] += 1

    # extract the correct nucleotide counts for the specified nucleic acid type
    if na_type == 'dna':
        return {k: v for (k, v) in nts.items() if k != 'U'}
    elif na_type == 'rna':
        return {k: v for (k, v) in nts.items() if k != 'T'}
    else:
        return "Not a valid nucleic acid type."


if __name__ == "__main__":

    # input data is provided as a file
    in_file = Path.cwd() / 'data' / '001_dna_dataset.txt'

    # extract the dna string from data file
    with open(in_file, 'r') as ref:
        s = ref.readline().strip()

    if is_na(s):
        counts = nts_count(s)
        if counts['N'] == 0:
            del counts['N']
        print("The nucleotide counts in the provided sequence are:")
        h = ''
        for k in counts.keys():
            # h += ' ' * 6 + k
            h += k.ljust(6, ' ')
        c = ''
        for v in counts.values():
            # c += "{:>6}".format(v)
            c += f"{v:<6}"
        print(h)
        print(c.strip())
    else:
        print("Not a valid nucleic acid string.")
