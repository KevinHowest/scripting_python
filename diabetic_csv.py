import bs4 
import urllib.request as request
import csv

def loadData(file):
    with open(file, mode = 'r') as f:
        content = f.readlines()
    f.close()
    
    outputVar = []
    
    for line in content:
        line = line.strip()
        outputVar.append(line.split(","))
        
    return outputVar

data = loadData('diabetic_data_initial.csv')
id_mapping = loadData('id_mapping.csv')

#Make dictionary of id_mapping

id_mapping_dict = {}
header = []
for row in id_mapping:
    try:
        row[0] = int(row[0])
    except:
        row_header = row[0].strip()
        id_mapping_dict[row_header] = {}
        header.append(row_header)
    else:
        id_mapping_dict[row_header][int(row[0])] = row[1]

del id_mapping

#Import ICD-9 and save it in a dictionary ICD9. 
with request.urlopen('https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/msp/physicians/diagnostic-code-descriptions-icd-9') as response:
    ICD9soup = bs4.BeautifulSoup(response.read(), "html.parser")

table = ICD9soup.select('tr')

#Format: {id_name: {code: meaning, code2: meaning2, ...}, id_name2: {...}}
ICD9 = {}

for tablerow in table[1:]:
    
    #Format range: <number> - <number>
    row_numbers = tablerow.select('td')[0]
    range_ICD9 = row_numbers.getText().strip()
    
    #Original format data: <a><data> (link)</a>
    row_data = tablerow.select('a')
    data_row = row_data[0].getText().split("(")[0].strip()
    
    #Replacing ',' in string to '/' because we are using a CSV-format
    data_row = data_row.replace(", ", "/")
        
    ICD9[range_ICD9] = data_row

#Cleanup data line per line

for row in data[1:]:
    
    #Replacing id's by values obtained from id_mapping.csv
    #Header[0] = 'admission_type_id', header[1] = discharge_disposition_id, header[2] = admission_source_id
    row[6] = id_mapping_dict[header[0]][int(row[6])]
    row[7] = id_mapping_dict[header[1]][int(row[7])]
    row[8] = id_mapping_dict[header[2]][int(row[8])]
    
    
    #Replace ICD9 codes in fields 18-20 with the correct terms obtained from www2.gov.....
    #Last range of ICD9 codes is V01-V82.9 -> manually enter the correct term, same with E... -E...
    for i in range(18,21):
        if row[i] == "?":
            continue
        
        #Using this try, except, else just for safety in case the value isn't in the correct format
        try:
            row[i] = float(row[i].strip())
        except:
            if row[i].strip().startswith("V"):
                row[i] = "Supplementary Classification of Factors Influencing Health Status and Contact with Health Services"
            elif row[i].strip().startswith("E"):
                row[i] = "Supplementary Classification of External Causes of Injury And Poisoning"
            else:
                row[i] = "ERROR"

        else:
            for ICD9_range in ICD9:
                interval = ICD9_range.split("-")
                
                try:
                    lower = float(interval[0].strip())
                    higher = float(interval[1].strip())
                except:
                    continue
                else:            
                    if lower <= row[i] <= higher:
                        row[i] = ICD9[ICD9_range]
                        break           

    #Changing NO and NONE to False and YES to True
    for i in range(22,50):
        row[i] = row[i].upper()
        if row[i] == "NO" or row[i] == "NONE":
            row[i] = False
        elif row[i] == "YES":
            row[i] = True

#Export data to output.csv

with open("output.csv", mode="w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
