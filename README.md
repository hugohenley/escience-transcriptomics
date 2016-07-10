# Trabalho Final da Disciplina e-Science - 2016.1

O trabalho foi realizado utilizando o Kepler e scripts em Python para realizar as tarefas que devem executar dinamicamente os arquivos (independente do número de cada arquivo gerado).

Para rodar, é necessário:

* Instalar o Kepler
* Alterar nos atores o diretório que contém os arquivos a serem processados
* Realizar download dos arquivos de extensão .fa, .sra e gtf e colocá-los na mesma pasta do arquivo .kar
* Neste trabalho foram utilizados os arquivos Drosophila_melanogaster.BDGP5.70.dna.chromosome.2L.fa, Drosophila_melanogaster.BDGP5.70.gtf e SRR031716.sra
* Realizar download do software que realiza o featureCounts (subread-1.5.0-p3-Linux-x86_64) no link https://sourceforge.net/projects/subread/
* Alterar o caminho no arquivo feature_counts.py para o local onde o seu featureCounts está localizado
* Executar o workflow
* Os arquivos teste.table e teste.table.summary gerados pelo workflow podem ser usados para conferência
