import random

cpf= [0]* 11 #copy of cpf_input in a list
letters = [0] * 10 #the letters chose to cript
cripted_cpf = [] #where the cripted cpf will be saved
cpf_key = [] #salva as letras usadas
s_code = [] #salva os numque elas representamos 

cript = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #letters option
cript_c = list(cript) #copy to eliminate used letters

while True:
	opc = input('O que gostariade fazer?\n1. Criptografar um CPF\n2. Descriptografar um CPF\n3. Fechar o Programa\nOPÇÃO: ')
	opc = int(opc)
	
	if opc == 1:
		while True:
			cpf_input = input('Digite seu CPF: ') #recebe o cpf
			if cpf_input.isdigit() and len(cpf_input) == 11: #checa se eh valido
				break
			else:
				print("CPF invalido.") #avisa que nao
		
		cpf = [int(digit) for digit in cpf_input] #salva cada digito do cpf na lista
		    
		for a in range(10):
		    r_let = random.choice(cript_c) #escolhe uma letra aleatoria
		    cript_c.remove(r_let) #remove para evitar copias
		    letters[a] = r_let #salva na lista de letras, onde a posicao eh o numero
		    	
		for b in range(len(cpf)):
		    cripted_cpf.append(letters[cpf[b]]) #salva o cpf criptografado
		
		alpha = [chr(ord('A') + i) for i in range(26)] #letters
		alpha += [str(i) for i in range(10)] #numb
		alpha.append('#')
		power = [2 ** i for i in range(37)] #power of2 value
		
		for i in range(37):
			if alpha[i] in cripted_cpf:
				cpf_key.append(alpha[i]) #letras usadas
				
		for j in range(len(cpf_key)):
		    for k in range(10):
		    	if cpf_key[j] == letters[k]:
		    		s_code.append(k) #numeros que as letras representam
		    	
		aux = ''.join(map(str,s_code)) #adicionando os numeros em uma str
		aux1 = int(aux) #transformando em int
		
		print(cripted_cpf) #cpf criptogrfad
		#print(cpf_key) #letras que tem na criptografia 
		#print(s_code) 
		#print(aux1) #numeros correspondentes ja em int
		
		let_key = [] #ey in letter
		
		for x in range(36,-1,-1):
			if aux1 >= (2**x):
				aux1 -= (2**x)
				let_key.append(alpha[x]) #codificando
		
		lett_key = ''.join(let_key)
		#print(let_key)
		print(lett_key)
		#print(f"resto: {aux1}")	
	
	#decodificacao
	if opc == 2:
		letters_cpf = []
		aux3 = 0
		value_cpf = []
		final_cpf = []
		
		k_cpf = input('Escreva a chave: ')
		k_cpf = k_cpf.upper()
		k_cpf = [char for char in k_cpf]
		
		c_cpf = input('Escreva o CPF criptografado: ')
		c_cpf = c_cpf.upper()
		c_cpf = [char for char in c_cpf]
		
		for m in range(37):
			if alpha[m] in c_cpf:
				letters_cpf.append(alpha[m])
				
		#print(letters_cpf)
				
		for n in range(36,-1,-1):
			if alpha[n] in k_cpf:
				aux3 += (2**n)
				#print(aux3)
		
		#print(aux3)
		value_cpf = [int(digit) for digit in str(aux3)]
		#print(value_cpf)
		
		for o in range(len(c_cpf)):
		    for p in range(len(letters_cpf)):
		    	if c_cpf[o] == letters_cpf[p]:
		    		final_cpf.append(value_cpf[p])
		    		
		res = ''.join(map(str,final_cpf))
		print(res)
	 
	    	
	if opc == 3:
		break
		 	
	if opc != 1 and opc != 2 and opc !=3:
		print('código invalido.')
		
