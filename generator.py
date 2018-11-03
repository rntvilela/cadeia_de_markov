#Gerador de palavras aleatorias utilizadno LO, JA, CA, DA e -ESP-
import random as rd

def prandom(dic, freq):
    "Gera silabas de acordo com a cadeia de Markov"
    
    Prefix=[]

    for item in range(len(freq)):
        if item < 1:
            Prefix.append(freq[item])
        else:
            Prefix.append(Prefix[item-1] + freq[item])

    rdnumber = rd.random()
    if rdnumber <= Prefix[0]:
        return dic[0]

    elif rdnumber <= Prefix[1]:
        return dic[1]
        
    elif rdnumber <= Prefix[2]:
        return dic[2]
        
    elif rdnumber <= Prefix[3]:
        return dic[3]
        
    elif rdnumber <= Prefix[4]:
        return dic[4]
        
    else:
        return dic[5]

def main():
    dic = ("LO", "JA", "CA", "DA", " ")
    
    ini = [0.012897, 0.006121, 0.038676, 0.048709, 0.893597]   
    LO = [0.0, 0.031646, 0.044304, 0.0, 0.924051]
    JA = [0.0, 0.0, 0.06, 0.08, 0.86]
    CA = [0.033994, 0.0, 0.002833, 0.21813, 0.745042]
    DA = [0.000674, 0.0, 0.0, 0.007417, 0.991908]
    ESP = [0.070407, 0.097212, 0.411365, 0.372409, 0.048606]
    
    #number = int(input("Informe o numero de interaçoes: "))
    number = 10000
    
    palavrasgeradas = []
    
    palavrasgeradas.append(prandom(dic, ini))
    for i in range(number-1):        
        if palavrasgeradas[i] == "LO":
            palavrasgeradas.append(prandom(dic, LO))
        
        elif palavrasgeradas[i] == "JA":
            palavrasgeradas.append(prandom(dic, JA))

        elif palavrasgeradas[i] == "CA":
            palavrasgeradas.append(prandom(dic, CA))
            
        elif palavrasgeradas[i] == "DA":
            palavrasgeradas.append(prandom(dic, DA))
        
        else:
            palavrasgeradas.append(prandom(dic, ESP))
     
    palavrasgeradas = ''.join(palavrasgeradas)
    
    infile = open("palavrasgeradas.txt", "w")
    infile.write(palavrasgeradas)
    infile.close()
    
    input("Pressione <Enter> para sair.")
    
if __name__ == "__main__":
    main()