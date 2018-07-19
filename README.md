# PPSUS - Aplicação do Avaliador 

Preparando o ambiente de desenvolvimento.

Instalar o Linux Mint 19 Cinnamon 64 bits

$ sudo apt-get update

$ sudo apt-get upgrade

$ bash <(curl -sL get.po-util.com) // instale o po-util (Ferramenta para desenvolvimento de firmware offline particle-photon)

$ sudo apt-get install python3-pip // Instalar o pip no sistema 

$ virtualenv DEV_PYTHON // Criar um ambiente de desenvolvimento python

$ source activate // Levantar o ambiente de desenvolvimento /bin/activate

(DEV_PYTHON) $ pip install Django==2.0.7 // Instalar o Django 
    
(DEV_PYTHON) $ pip install paho-mqtt
