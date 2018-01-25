import random

aa_name = ['Alanine', 'Arginine', 'Asparagine', 'Asparaginezuur', 'Cysteine', 'Glutaminezuur', 'Glutamine', 'Glycine', 'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Serine', 'Threonine', 'Tryptofaan', 'Tyrosine', 'Valine']
aa_3 = ['Ala', 'Arg', 'Asn', 'Asp', 'Cys', 'Glu', 'Gln', 'Gly', 'His', 'Ile', 'Leu', 'Lys', 'Met', 'Phe', 'Pro', 'Ser', 'Thr', 'Trp', 'Tyr', 'Val']
aa_1 = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

print('What is given?\n (0)Full name\n (1)3-letter code\n (2)1-letter code\n (3)Random')
user_choice = ""
while (user_choice not in range(0,4)):
	user_choice = int(input())

if user_choice == 3:
	random_choice = True
else:
	random_choice = False

print("Enter 'exit' to stop or '?' to see the remaining amount of AA")
user_input = ""
complete_list = (aa_name, aa_3, aa_1)

while (len(complete_list[0]) > 0) and (user_input != 'exit'):
	
	if random_choice:
		user_choice = random.randint(0,2)
	
	list_types = [0,1,2]
	list_types.pop(user_choice)
	
	random_number = random.randint(0,len(complete_list[0])-1)
	print('Given:', complete_list[user_choice][random_number])
	
	
	for x in list_types:
		
		user_input = "Nothing"
		while user_input.title() != complete_list[x][random_number]:
			if x == 0:
				a = "Enter the full name: "
			elif x == 1:
				a = "Enter the 3-letter code: "
			else:
				a = "Enter the 1-letter code: "
			
			if user_input == "exit":
				break
			
			if user_input == '?':
				print(len(complete_list[x]), "AA to go!")
			elif user_input != "Nothing":
				print("Wrong answer, please try again!")
				
			user_input = input(a)
		if(user_input != "exit"):	
			print("Correct!")
		else:
			break
	
	complete_list[0].pop(random_number)
	complete_list[1].pop(random_number)
	complete_list[2].pop(random_number)