frase = 'Curso em Video Python'

# analise

print(frase.count('o', 0, 14))
print(len(frase))
print(frase[9:])
print(frase.find('deo'))
print(frase.find('android'))
print('Curso' in frase) 

# trasnformação

print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '   Aprenda Python  '

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

# divisão

print(frase.split())

# junção

print(' '.join(frase))