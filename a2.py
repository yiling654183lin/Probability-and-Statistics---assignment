def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    data1=len(dna1)
    data2=len(dna2)
    if data1-data2>0:
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    result = dna.count(nucleotide)
            
    return result

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False 

def is_valid_sequence(dna):
    """(str)->bool
    
    Return True if and olny if the DNA sequence has only ATCG.
    
    >>>is_valid_sequence('ATCG')
    True
    >>>is_valid_sequence('SAA')
    False
    
    """
    data1=count_nucleotides(dna, 'A')
    data2=count_nucleotides(dna, 'T')
    data3=count_nucleotides(dna, 'C')
    data4=count_nucleotides(dna, 'G')
    if (len(dna)-data1-data2-data3-data4==0):
        return True
    else:
        return False

def insert_sequence(dna1,dna2,pos):
    """(str,str,int)->str
    
    Return the combination of the DNA on the assign position.
    
    >>>insert_sequence('CCGG','AT',2)
    CCATGG
    >>>insert_sequence('ATT','GG',1)
    AGGTT
    
    """
    result=''
    if (is_valid_sequence(dna1) and is_valid_sequence(dna2)):
        for i in range (0,len(dna1),+1):
            if i==pos:
                for j in range (0,len(dna2),+1):
                    result=result + dna2[j]
                result=result+dna1[i]
            else:
                result=result+dna1[i]
        return result
    else:
        return 'Invalid DNA sequence'
        
def get_complement(dna):
    """(str)->str
    
    Return the complement of the input DNA
    
    >>>get_complement('A')
    T
    >>>get_complement('C')
    G
    
    """
    if dna == 'A':
        return 'T'
    elif dna == 'T':
        return 'A'
    elif dna == 'C':
        return 'G'
    elif dna == 'G':
        return 'C'
    else:
        return 'Invalid input'

def get_complementary_sequence(dna):
    """(str)->str
    
    Return the complementary DNA sequence of the input DNA sequence
    
    >>>get_complementary_sequence('AATTC')
    'TTAAG'
    >>>get_complementary_sequence('ATCG')
    'TAGC'    

    """
    result=''
    for dna in dna:
        result = result + get_complement(dna)
    return result 
