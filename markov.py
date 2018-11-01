def calcPalavras(fname):
    "Calcula o numero de palavras em um arquivo de texto."
    infile = open(fname, "r")
    p = 0
    
    for linha in infile:
        p = p + len(linha.split())
    
    infile.close()
    return p

def calcEsp(fname):
    "Calcula o numero de espaços em um arquivo de texto."
    infile = open(fname, "r")
    esp = 0
    
    for linha in infile:
        esp = esp + linha.count(" ")
    
    infile.close()
    return esp

def calcLO(fname):
    "Calcula o numero da silaba LO presente em um arquivo de texto."
    infile = open(fname, "r")
    lo = 0
    
    for linha in infile:
        linha = linha.lower()
        linha = linha.replace('á', 'a').replace('à', 'a').replace('ó', 'o').replace('ò', 'o')
        lo = lo + linha.count("lo")
    
    infile.close()
    return lo

def calcJA(fname):
    "Calcula o numero da silaba JA presente em um arquivo de texto."
    infile = open(fname, "r")
    ja = 0
    
    for linha in infile:
        linha = linha.lower()
        linha = linha.replace('á', 'a').replace('à', 'a').replace('ó', 'o').replace('ò', 'o')
        ja = ja + linha.count("ja") 
    
    infile.close()
    return ja

def calcCA(fname):
    "Calcula o numero da silaba CA presente em um arquivo de texto."
    infile = open(fname, "r")
    ca = 0
    
    for linha in infile:
        linha = linha.lower()
        linha = linha.replace('á', 'a').replace('à', 'a').replace('ó', 'o').replace('ò', 'o')
        ca = ca + linha.count("ca")
    
    infile.close()
    return ca

def calcDA(fname):
    "Calcula o numero da silaba DA presente em um arquivo de texto."
    infile = open(fname, "r")
    da = 0
    
    for linha in infile:
        linha = linha.lower()
        linha = linha.replace('á', 'a').replace('à', 'a').replace('ó', 'o').replace('ò', 'o')
        da = da + linha.count("da")
    
    infile.close()
    return da

def main():
    #fname = input ("Informe o nome do arquivo: " )
    fname = "teste.txt"
    
    palavras = calcPalavras(fname)
    
    ESP = calcEsp(fname)
    
    LO = calcLO(fname)
    
    JA = calcJA(fname)
    
    CA = calcCA(fname)
    
    DA = calcDA(fname)
    
    print("O total de palavras é {0}, total de espaços é {1}, totalizando {2}.".format(palavras, ESP, (palavras+ESP)))
    print("O total de LO é {0}, total de JA é {1}, total de CA é {2}, total de DA é {3}.".format(LO, JA, CA, DA))
    
if __name__=="__main__":
    main()