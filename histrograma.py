#Histograma para as palavras LOJA, JACA e CADA

import matplotlib.pyplot as plt

def calcStr(fname, str):
    "Calcula o numero de ocorrencia de uma String em um arquivo de texto."
    infile = open(fname, "r", encoding="iso-8859-1")
    strCounter = 0
    
    for linha in infile:
        strCounter = strCounter + linha.count(str)
    
    infile.close()
    return strCounter

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
    #fname = "Policarpo.txt"
    fname = "palavrasgeradas.txt"
    
    LOJA = calcStr(fname, " LOJA ")
    JACA = calcStr(fname, " JACA ")
    CADA = calcStr(fname, " CADA ")
    
    wordsdict = {"LOJA": LOJA , "JACA": JACA, "CADA": CADA}
    
    writeList([LOJA, JACA, CADA], "hist.txt", "w")
 
    plt.bar(range(len(wordsdict)), wordsdict.values(), align='center')
    plt.xticks(range(len(wordsdict)), wordsdict.keys())  
    plt.xlabel("Palavra")
    plt.ylabel("Frequência")
    plt.title("Histograma")
    plt.savefig("histogramapalavras.png")
    plt.show()
    
    #writeList(histograma, "histograma.txt", "w")
            
if __name__=="__main__":
    main()
