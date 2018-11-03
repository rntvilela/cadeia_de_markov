#Trabalho sobre cadeia de Markov

def calcStr(fname, str):
    "Calcula o numero de ocorrencia de uma String em um arquivo de texto."
    infile = open(fname, "r", encoding="iso-8859-1")
    strCounter = 0
    
    for linha in infile:
        linha = linha.lower()
        linha = linha.replace(',', '').replace('.', '').replace(';', '').replace(':', '').replace('?', '').replace('!', '').replace('-', '')
        linha = linha.replace('á', 'a').replace('à', 'a').replace('â', 'a').replace('ã', 'a')
        linha = linha.replace('ó', 'o').replace('ò', 'o').replace('ô', 'o').replace('õ', 'o')
        strCounter = strCounter + linha.count(str)
    
    infile.close()
    return strCounter

def calcProb(n, t):
    "Calcula probabilidade de ocorrencia de um item"
    
    return round(n/t, 6)

def writeList(list, fname, mode):
    "Escreve os valores de uma lista em um arquivo de texto."
    
    strList = '\n'.join(str(e) for e in list)
    f = open(fname, mode)
    f.write('\n'+strList+'\n')
    f.close()
    
    return 0

def main():
    #fname = input("Informe o nome do arquivo: " )
    #fname = "teste.txt"
    #fname = "bn000013.pdf"
    fname = "Policarpo.txt"
    
    #Estado inicial
    ESP = calcStr(fname, " ")
    LO = calcStr(fname, "lo")
    JA = calcStr(fname, "ja")
    CA = calcStr(fname, "ca")
    DA = calcStr(fname, "da")
    
    totalp = ESP + LO + JA + CA + DA
    
    P_ESP = calcProb(ESP, totalp)
    P_LO = calcProb(LO, totalp)
    P_JA = calcProb(JA, totalp)
    P_CA = calcProb(CA, totalp)
    P_DA = calcProb(DA, totalp)
    
    #Probabilidade de estado inicial
    P_INI = [P_LO, P_JA, P_CA, P_DA, P_ESP]
        
    #Numero de transições de ESP
    ESPtoLO = calcStr(fname, " lo")
    ESPtoJA = calcStr(fname, " ja")
    ESPtoCA = calcStr(fname, " ca")
    ESPtoDA = calcStr(fname, " da")
    ESPtoESP = calcStr(fname, "  ")
    
    #Total de transições de ESP
    totalESPtoN = ESPtoLO + ESPtoJA + ESPtoCA + ESPtoDA + ESPtoESP 
    
    #Probabilidades de transições de ESP
    P_ESPtoLO = calcProb(ESPtoLO, totalESPtoN)
    P_ESPtoJA = calcProb(ESPtoJA, totalESPtoN)
    P_ESPtoCA = calcProb(ESPtoCA, totalESPtoN)
    P_ESPtoDA = calcProb(ESPtoDA, totalESPtoN)
    P_ESPtoESP = calcProb(ESPtoESP, totalESPtoN)
    
    #Primieira linha da matriz de probabilidades de transições de estados
    P_ESPtoN = [P_ESPtoLO, P_ESPtoJA, P_ESPtoCA, P_ESPtoDA, P_ESPtoESP]
    
    #Numero de transições de LO
    LOtoLO = calcStr(fname, "lolo")
    LOtoJA = calcStr(fname, "loja")
    LOtoCA = calcStr(fname, "loca")
    LOtoDA = calcStr(fname, "loda")
    LOtoESP = calcStr(fname, "lo ")
    
    #Total de transições de LO
    totalLOtoN = LOtoLO + LOtoJA + LOtoCA + LOtoDA + LOtoESP
    
    #Probabilidades de transições de LO
    P_LOtoLO = calcProb(LOtoLO, totalLOtoN)
    P_LOtoJA = calcProb(LOtoJA, totalLOtoN)
    P_LOtoCA = calcProb(LOtoCA, totalLOtoN)
    P_LOtoDA = calcProb(LOtoDA, totalLOtoN)
    P_LOtoESP = calcProb(LOtoESP, totalLOtoN)
    
    #Segunda linha da matriz de probabilidades de transições de estados
    P_LOtoN = [P_LOtoLO, P_LOtoJA, P_LOtoCA, P_LOtoDA, P_LOtoESP]
    
    #Numero de transições de JA
    JAtoLO = calcStr(fname, "jalo")
    JAtoJA = calcStr(fname, "jaja")
    JAtoCA = calcStr(fname, "jaca")
    JAtoDA = calcStr(fname, "jada")
    JAtoESP = calcStr(fname, "ja ")
    
    #Total de transições de JA
    totalJAtoN = JAtoLO + JAtoJA + JAtoCA + JAtoDA + JAtoESP
    
    #Probabilidades de transições de JA
    P_JAtoLO = calcProb(JAtoLO, totalJAtoN)
    P_JAtoJA = calcProb(JAtoJA, totalJAtoN)
    P_JAtoCA = calcProb(JAtoCA, totalJAtoN)
    P_JAtoDA = calcProb(JAtoDA, totalJAtoN)
    P_JAtoESP = calcProb(JAtoESP, totalJAtoN)
    
    #Terceira linha da matriz de probabilidades de transições de estados
    P_JAtoN = [P_JAtoLO, P_JAtoJA, P_JAtoCA, P_JAtoDA, P_JAtoESP]
    
    #Numero de transições de CA
    CAtoLO = calcStr(fname, "calo")
    CAtoJA = calcStr(fname, "caja")
    CAtoCA = calcStr(fname, "caca")
    CAtoDA = calcStr(fname, "cada")
    CAtoESP = calcStr(fname, "ca ")
    
    #Total de transições de CA
    totalCAtoN = CAtoLO + CAtoJA + CAtoCA + CAtoDA + CAtoESP
    
    #Probabilidades de transições de CA
    P_CAtoLO = calcProb(CAtoLO, totalCAtoN)
    P_CAtoJA = calcProb(CAtoJA, totalCAtoN)
    P_CAtoCA = calcProb(CAtoCA, totalCAtoN)
    P_CAtoDA = calcProb(CAtoDA, totalCAtoN)
    P_CAtoESP = calcProb(CAtoESP, totalCAtoN)
    
    #Quarta linha da matriz de probabilidades de transições de estados
    P_CAtoN = [P_CAtoLO, P_CAtoJA, P_CAtoCA, P_CAtoDA, P_CAtoESP]
    
    #Numero de transições de DA
    DAtoLO = calcStr(fname, "dalo")
    DAtoJA = calcStr(fname, "daja")
    DAtoCA = calcStr(fname, "daca")
    DAtoDA = calcStr(fname, "dada")
    DAtoESP = calcStr(fname, "da ")
    
    #Total de transições de DA
    totalDAtoN = DAtoLO + DAtoJA + DAtoCA + DAtoDA + DAtoESP
    
    #Probabilidades de transições de DA
    P_DAtoLO = calcProb(DAtoLO, totalDAtoN)
    P_DAtoJA = calcProb(DAtoJA, totalDAtoN)
    P_DAtoCA = calcProb(DAtoCA, totalDAtoN)
    P_DAtoDA = calcProb(DAtoDA, totalDAtoN)
    P_DAtoESP = calcProb(DAtoESP, totalDAtoN)
    
    #Quinta linha da matriz de probabilidades de transições de estados
    P_DAtoN = [P_DAtoLO, P_DAtoJA, P_DAtoCA, P_DAtoDA, P_DAtoESP]
    
    #Matriz de probabilidades de transições de estados
    P_MATRIZ = [P_LOtoN, P_JAtoN, P_CAtoN, P_DAtoN, P_ESPtoN]
    
    print("\nProbabilidades de estados iniciais: \n", P_INI)
    print("\nMatriz de probabilidades de transições de estados: \n", P_MATRIZ)
    
    writeList(P_MATRIZ, "matrizdeprob.txt", "w")
    writeList(P_INI, "matrizdeprob.txt", "a")
        
    input("\nPressione <Enter> para sair.")
    
if __name__=="__main__":
    main()