def verificar_letra_a(string):

   string = string.lower() # Converte a string para minúscula

   count_a = string.count('a')  # Conta quantas vezes 'a' aparece

   if count_a > 0:

       print(f"A letra 'a' aparece {count_a} vezes.")

   else:

       print("A letra 'a' não foi encontrada.")