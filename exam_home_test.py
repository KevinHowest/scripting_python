
def check_sequence(sequence):
    GC = {'G', 'C'}
    GC_content = 0
    seq_len = 0
    message = "warning"
    for nuc in sequence:
        if nuc in GC:
            GC_content += 1
        seq_len += 1
    
    GC_content = (GC_content/seq_len)*100
    if 40 <= GC_content <= 60:
        message = "ok"
    
    return "{} {}".format(message, str(GC_content)) 


def nucleotide_repeats(sequence):
    history = ''
    count = 0
    for nuc in sequence:
        if nuc == history:
            count += 1
        else:
            history = nuc
            count = 0
        
        if count == 3:
            return "warning excessive nucleotide repeats"
    return "ok"



def dinucleotide_repeats(sequence):
    #Er moet 2x over de sequentie gelopen worden. De eerste keer worden er paren gevormd [0,1][2,3]..., de volgende keer [1,2][3,4]...
    for j in range(1,3):
        count = 0
        history = ''
        i = j
        while i < len(sequence):
            nuc_pair = sequence[i-1]+sequence[i]
            
            if nuc_pair == history:
                count += 1
                i += 2
            else:
                history = nuc_pair
                count = 0
                i += 2
                
            if count == 3:
                return ("warning excessive dinulceotide repeats")
    return "ok"



def hairpin_check(sequence):
    nuc_result = nucleotide_repeats(sequence)
    dinuc_result = dinucleotide_repeats(sequence)
    
    if nuc_result != "ok":
        return nuc_result
    elif dinuc_result != "ok":
        return dinuc_result
    
    if sequence == sequence[::-1]:
        return "warning possible hairpin"
    else:
        return "ok"
    
def complementary_sequence(sequence):
    
    translation_table = sequence.maketrans("ATCG", "TAGC")
    return sequence.translate(translation_table)

def compare_complementary_sequences(sequence1, sequence2):
    pass