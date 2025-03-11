# Automatización para leer un archivo de texto y escribir en otro archivo de texto


# Definir función para leer archivo de texto
def leer_archivo(archivo):
    header = ''
    data = []
    with open(archivo, 'r') as file:
        for i, line in enumerate(file):
            if i == 0:
                header = line
            else:
                data.append(line)
    return header, data


# Definir función para escribir archivo de texto
def escribir_archivo(archivo, texto):
    with open(archivo, 'w') as file:
        file.write(texto)


# Leer archivo de texto
header, texto = leer_archivo('texto.csv')
print(header)
print("-----")
for i in texto:
    print(i)
