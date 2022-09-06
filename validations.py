def is_na(seq, na_type='na', alphabet='base') -> bool:
    """
    Verifies if a given sequence is a valid nucleic acid sequence (respects the FASTA alphabet).

    :param seq: a nucleic acid sequence, DNA or RNA
    :param na_type: a string with three accepted values, 'dna', 'rna', 'na', specifying the type of nucleic acid
                    provided, or if the verification should be for all nucleic acid types
    :param alphabet: a string with two accepted values, 'base', 'extended', specifying if the string contains
                    unidentified or partially identified nucleotides
    :return: True if the sequence is valid
    """
    seq = set(seq.upper())

    # list of allowed symbols for nucleic acids in FASTA files
    fasta_na_alphabet = 'ACGTU'
    fasta_na_alphabet_extension = 'RYSWKMBDHVN.'

    # if the type of nucleic acid is provided, eliminate the wrong letter from the alphabet
    if na_type == 'dna':
        fasta_na_alphabet.replace('U', '')
    elif na_type == 'rna':
        fasta_na_alphabet.replace('T', '')

    if alphabet == 'extended':
        fasta_na_alphabet = fasta_na_alphabet + fasta_na_alphabet_extension

    # T appears only in DNA and U appears only in RNA. If a sequence has both nucleotides it is not valid.
    if 'T' in seq and 'U' in seq:
        return False

    for char in fasta_na_alphabet:
        if char in seq:
            seq.remove(char)

    if len(seq) > 0:
        return False
    else:
        return True
