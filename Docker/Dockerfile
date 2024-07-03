FROM python  
WORKDIR /app   
COPY . /app    
CMD ["python", "test_docker.py"]  

#FROM python  #permette di scegliere la versione di python
#WORKDIR /app   #working directory seleziona la cartella
#COPY . /app    #copia tutto quello che è all interno della directory corrente nel container
#CMD ["python", "test_docker.py"]  #versione di python e nome file

# per creare l'immagine passare da terminale il comando "docker build -t mytest ." per runnare "docker run mytest"