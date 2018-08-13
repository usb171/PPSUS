# Preparando o ambiente de desenvolvimento.

Instalar o Linux Mint 19 Cinnamon 64 bits

$ sudo apt-get update

$ sudo apt-get upgrade

$ bash <(curl -sL get.po-util.com) // instale o po-util (Ferramenta para desenvolvimento de firmware offline particle-photon)

$ sudo apt-get install python3-pip // Instalar o pip no sistema 

$ virtualenv DEV_PYTHON // Criar um ambiente de desenvolvimento python

$ source activate // Levantar o ambiente de desenvolvimento /bin/activate

(DEV_PYTHON) $ pip install django==2.0.7 // Instalar o Django 
    
(DEV_PYTHON) $ pip install paho-mqtt




# Descrição dos Exames

Exame A ID 1

TUG TESTE *</br></br>

levantar-se de uma cadeira, sem ajuda dos braços, andar a uma distância de três metros, dar a volta e retornar.</br>

a) menos de 20 segundos para realização, correspondendo a baixo risco para quedas</br>
b) de 20 a 29 segundos, a médio risco para quedas</br>
c) 30 segundos ou mais, a alto risco para quedas.</br>






Exame B ID 2

* ALCANCE FUNCIONAL *</br></br>

Procedimento: O paciente em posição ortostática, membros inferiores levemente abduzidos, descalço, coluna o mais ereta possível, olhar para o horizonte, braços em extensão a 90° e hemicorpo direito próximo à parede. A partir dessa posição, solicitava-se ao avaliado esticar-se o máximo possível para frente. A excursão do braço desde o início até o final é medida por uma fita métrica fixada na parede no sentido horizontal ao lado do paciente, na altura do acrômio. Para a aferição, a extremidade do terceiro metacarpo pode ser utilizada como marcação de partida até o alcance máximo. </br>

(4) Capaz de alcançar com confiabilidade acima de 25cm (10 polegadas)</br>
(3) Capaz de alcançar acima de 12,5cm (5 polegadas)</br>
(2) Capaz de alcançar acima de 5cm (2 polegadas)</br>
(1) Capaz de alcançar mas com necessidade de supervisão</br>
(0) Perda de equilíbrio durante as tentativas / necessidade de suporte externo</br>






Exame C ID 3



* EM PÉ SEM APOIO *</br></br>

 Por favor, fique de pé por dois minutos sem se segurar em nada.</br>
(4) Capaz de permanecer em pé com segurança por 2 minutos</br>
(3) Capaz de permanecer em pé durante 2 minutos com supervisão</br>
(2) Capaz de permanecer em pé durante 30 segundos sem suporte</br>
(1) Necessidade de várias tentativas para permanecer 30 segundos sem suporte</br>
(0) Incapaz de permanecer em pé por 30 segundos sem assistência</br>






Exame D ID 4


* EM PÉ SEM SUPORTE COM OLHOS FECHADOS *</br></br>

Por favor, feche os olhos e permaneça parado por 10 segundos</br>

(4) Capaz de permanecer em pé com segurança por 10 segundos</br>
(3) Capaz de permanecer em pé com segurança por 10 segundos com supervisão</br>
(2) Capaz de permanecer em pé durante 3 segundos</br>
(1) Incapaz de manter os olhos fechados por 3 segundos mas permanecer em pé </br>
(0) necessidade de ajuda para evitar queda</br>



Exame E ID 5


*EM PÉ, VIRAR E OLHAR PARA TRÁS SOBRE OS OMBROS DIREITO E ESQUERDO*</br></br>

Virar e olhar para trás sobre o ombro esquerdo. Repetir para o direito. O examinador pode pegar um objeto para olhar e colocá-lo atrás do sujeito para encorajá-lo a realizar o giro.</br>

(4) Olha para trás por ambos os lados com mudança de peso adequada</br>
(3) Olha para trás por ambos por apenas um dos lados, o outro lado mostra menor mudança de peso</br>
(2) Apenas vira para os dois lados mas mantém o equilíbrio</br>
(1) Necessita de supervisão ao virar</br>
(0) Necessita assistência para evitar perda de equilíbrio ou queda</br>


# Observações no tratamento das coletas
Foram excluidos todos os pacientes com nome yasmine, teste e teste(OFF), uma vez que são pacientes criados com intuito de testes. Ao serem deletados esses pacientes, em cascata, foram excluidos as suas devidas coletas. 

# Exame_A

    13/08/2018
Foram deletadas as coletas do ID 29 ao 37, do ID 55 ao 58 e do ID 78 ao 80. Não foram colocados o risco de queda.

# Exame_B

    13/08/2018
Coletas com IDs 39, 43, 65, 113, 118, 167, 199 não possuem DESLOCAMENTO. Essas coletas foram exluidas pois houve preenchimento do campo PONTUAÇÂO. 

# Exame_C

    13/08/2018
Os avaliadores reduziram o tempo desse tipo de exame de 2 minutos para 1 minuto. A coleta ID 47 foi excluída pois entra em contradição dos valores dos campos CRONOMETRO e PONTUAÇÂO. 

# Exame_D

    13/08/2018
Nenhuma coleta foi deletada. 

# Exame_E

    13/08/2018
A coleta ID 175 foi desativada pelo avaliador (VISIVEL 0). Essa coleta não deve ser utilizada mesmo não sendo deletada do banco.

