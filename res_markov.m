format long;

%              LO       JA       CA       DA      -ESP-
prob_ini = [0.012897 0.006121 0.038676 0.048709 0.893597];

%              LO       JA         CA        DA      -ESP-
prob_matriz = [0.0      0.031646 0.044304 0.0      0.924051; 
               0.0      0.0      0.06     0.08     0.86;
               0.033994 0.0      0.002833 0.21813  0.745042;
               0.000674 0.0      0.0      0.007417 0.991908;
               0.070407 0.097212 0.411365 0.372409 0.048606];

%(n = 0)
%Proba de -ESP-LOJA-ESP-
P_LOJA = prob_ini(5)*prob_matriz(5,1)*prob_matriz(1,2)*prob_matriz(2,5);

%Proba de -ESP-JACA-ESP-
P_JACA = prob_ini(5)*prob_matriz(5,2)*prob_matriz(2,3)*prob_matriz(3,5);

%Proba de -ESP-CADA-ESP-
P_CADA = prob_ini(5)*prob_matriz(5,3)*prob_matriz(3,4)*prob_matriz(4,5);

%(n = 5)
%Proba de -ESP-CADA-ESP-
prob_matriz_n5 = prob_matriz^5;
prob_ini_n5 = prob_ini*prob_matriz_n5;

P_CADA_N5 = prob_ini_n5(5)*prob_matriz_n5(5,3)*prob_matriz_n5(3,4)*prob_matriz_n5(4,5);

P_CADA_N5           
        