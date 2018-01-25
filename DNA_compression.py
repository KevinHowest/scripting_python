import string

alphabet = list(string.ascii_uppercase)

input = 'ACCC-GTTTTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

previous_nuc = ''
compressed_DNA = ''
repeat_count = 1
position_count = 0
length = len(input)

for nuc in input:
    
    position_count += 1
    if position_count == length and nuc == previous_nuc:
        repeat_count += 1
        
    if (repeat_count >= 4) and (nuc != previous_nuc or position_count == length):
        
        while repeat_count > 26:
            compressed_DNA += '-Z'+previous_nuc
            repeat_count -= 26
            
        compressed_DNA += '-' + alphabet[repeat_count-1] + previous_nuc
        repeat_count = 1
        
    elif (nuc != previous_nuc) or (position_count == length):
                
        if previous_nuc != '-':
            compressed_DNA += (previous_nuc * repeat_count)
        else:
            compressed_DNA += '-' + alphabet[repeat_count-1 ]+ previous_nuc
        repeat_count = 1
        
    else:
        repeat_count += 1
    
    previous_nuc = nuc
    
print(compressed_DNA)