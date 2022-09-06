""" Computing GC Content
Usage: just run the script, there are no parameters.

Link to the problem solved in this file: https://rosalind.info/problems/gc/

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. Note that the
reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is
called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling
information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the
next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes
a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows
for a default error of 0.001 in all decimal answers unless otherwise stated.

"""

from pathlib import Path


def gc_content(fasta_file):
    """
    Process a file containing one or more DNA sequences in FASTA format and return a dictionary of sequence ids and
    their GC content.

    :param fasta_file: A valid FASTA file with one or more DNA strings
    :return: A dictionary of sequence ids and their GC content.
    """

    # the input data is a fasta file with fixed width lines containing more than one DNA sequence of at most 1000 nt
    # this means that the sequences will be split on multiple lines

    # this task can deal with very long and numerous sequences
    # it is important not to store the whole DNA string in a variable

    dnas = dict()
    with open(fasta_file, 'r') as ref:
        dna_id = ref.readline().strip()[1:]        # extract the DNA id without the FASTA placeholder (that is '>')
        gc = 0      # GC count for the first DNA string
        dna_len = 0     # DNA string length
        for line in ref:
            # when entering this loop the file handler will point to the second line, that should not start with '>'
            if line.startswith('>'):
                # when encountering a new DNA string store the info about the string that was processed
                dnas[dna_id] = gc * 100 / dna_len

                # extract the DNA id of this new DNA string
                dna_id = line[1:].strip()

                # reinitialize GC count and DNA length for this new DNA string
                gc = 0
                dna_len = 0
            else:
                # Process the DNA string line by line
                dna = line.strip()      # read the DNA substring
                dna_len += len(dna)     # add the substring length to the total length
                for ncl in dna:         # add each GC occurrence in the substring to the total GC count
                    if ncl in ('G', 'C'):
                        gc += 1

        # when reaching EOF store the info about the last string that was processed
        dnas[dna_id] = gc * 100 / dna_len
    return dnas


if __name__ == "__main__":

    # input data is provided as a file
    in_file = Path.cwd() / 'data' / '005_gc_dataset.fasta'

    # process the file to obtain GC content of the DNA sequences
    # consider that the input file is valid
    d = gc_content(in_file)

    # extract the DNA sequence with the max GC content
    max_gc = 0
    max_id = ''
    for k, v in d.items():
        if v > max_gc:
            max_gc = v
            max_id = k

    print(f"The DNA sequence with the max GC content is:\n"
          f"{'ID':<{len(max_id) + 2}}   GC Content (%)\n"
          f"{max_id:<{len(max_id) + 2}}   {max_gc:.4f}")
