import argparse

def read_user_input():
    parser = argparse.ArgumentParser(description='Process input.')
    
    parser.add_argument("infile", help='First file to perform something on')
    parser.add_argument("infile2", help='Second file to do something with')
    parser.add_argument("-a", "--arg", default='simple', help='Optional argument')
    
    args = parser.parse_args('file file2'.split())
    result = [args.infile, args.infile2, args.arg]
    return result

	
    
print(read_user_input())

def compare_complementary_sequences(seq1, seq2):
    complementary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    def compare(nuc1, nuc2, counter):
        if nuc1 == nuc2:
            return counter + 1
        else:
            return 0
    
    reverse_seq2 = seq2[::-1]

    comp_counter = 0
    comp_counter2 = 0
   
    for i in range(len(seq1)):
        s1 = complementary[seq1[i]]
        s2 = seq2[i]
        rs2 = reverse_seq2[i]
        
        if i == len(seq2)-1:
            break
        
        comp_counter = compare(s1, s2, comp_counter)
        comp_counter2 = compare(s1, rs2, comp_counter2)
            
        if comp_counter == 3 or comp_counter2 == 3:
            return ('warning long inter primer homology')
    
    return ('ok')
print(compare_complementary_sequences('ATTCA', 'TTAG'))

#def herhalingslengte(input_stringA, input_stringB):
#    
#    lenA = len(input_stringA)
#    lenB = len(input_stringB)
#    
#    
#    i = 0
#    count = 0
#    while i <= (lenA - lenB):
#        if input_stringA[i:(i+ (lenB))].lower() == input_stringB.lower():
#            count += 1
#            i = i + (lenB-1)
#            
#        i += 1
#        
#    return(count)
#
#
#print(herhalingslengte('TtTtta', 'Ta'))  

#class Huntington():
#    repeat_seq = 'CAG'
#    
#    def __init__(self, repeatcount):
#        
#        self.repeatcount = repeatcount
#        
#    @classmethod
#    def herhalingslengte(cls, input_stringA):
#        
#        lenA = len(input_stringA)
#        lenB = len(Huntington.repeat_seq)
#        
#        
#        i = 0
#        repeatcount = 0
#        while i <= (lenA - lenB):
#            if input_stringA[i:(i+ (lenB))].lower() == Huntington.repeat_seq.lower():
#                repeatcount += 1
#                i = i + (lenB-1)
#                
#            i += 1
#            
#        return cls(repeatcount)
#    
#
#    def huntingtonDiagnose(self):
#                
#        if self.repeatcount > 39:
#            self.diagnose = "Absoluut risico"
#        elif self.repeatcount >= 36:
#            self.diagnose = "Verhoogd risico"
#        elif self.repeatcount > 27:
#            self.diagnose = "Laag risico"
#        else:
#            self.diagnose = "Normaal"
#    
#        return self.diagnose
#
#
##sequence_file = open('huntington.fasta', mode="r")
##sequence = sequence_file.read()
##sequence_file.close()
#
#sequence = 'CAG'*15
#
#object_hunt = Huntington.herhalingslengte(sequence)
#diagnose = object_hunt.huntingtonDiagnose()
#print(diagnose)
