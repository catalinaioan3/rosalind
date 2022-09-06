""" Counting Point Mutations (computing the Hamming distance)
Usage: just run the script, there are no parameters.

Link to the problem solved in this file: https://rosalind.info/problems/gc/

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).

"""

from pathlib import Path
from validations import is_na


def hamming_distance(dna1, dna2):
    """
    Computes the Hamming distance between two DNA sequences. A value of 0 means the sequences are identical.

    :param dna1: A DNA sequence.
    :param dna2: A second DNA sequence of the same length.
    :return: The Hamming distance between the two sequences.
    """
    hd = 0
    if len(dna1) == len(dna2):
        for i in range(0, len(dna1)):
            if dna1[i] != dna2[i]:
                hd += 1
    else:
        raise ValueError("Sequences don't have the same length!")

    return hd


if __name__ == "__main__":

    # input data is provided as a file
    in_file = Path.cwd() / 'data' / '006_hamm_dataset.txt'

    # extract the dna string from data file
    with open(in_file, 'r') as ref:
        s = ref.readline().strip()
        t = ref.readline().strip()

    if is_na(s, 'dna') and is_na(t, 'dna'):
        try:
            print(f"The Hamming distance between the two DNA sequences provided is:\n"
                  f"{hamming_distance(s, t)}")
        except ValueError as err:
            print(err)
    else:
        print("At list one DNA string is not valid.")
