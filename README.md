# projeto_in242
Projeto da disciplina IN242

1. Instalar MQTT e Mongo usando o AWS e deixar disponivel publicamente.
2. Usar o producer e consumer para gerar a cada segundo por 1h dados de temperatura (15-30) enviando para o MQTT e armazenando no Mongo.
3. Consumir o resultado do Mongo e salvar em CSV/XLS.
4. Fazer a analise dos dados do CSV em um notebook (media, minuto com maior media, dv, etc..).
5. Subir o codigo, arquivos do docker, notebook e csv no github.
6. Enviar o link para lucio.oliveira@inatel.br até dia 5/10

#Comandos

Protect Private Key: chmod 400 aws.pem 
Connet instance: ssh -i "private-key" ubuntu@"public_dns" -> ssh -i aws.pem ubuntu@ec2-18-228-159-69.sa-east-1.compute.amazonaws.com

Atualizar pacotes: sudo apt update

#Git

git status
adicionar ao index: git add "arquivo" / git add *
confirmar mudanças: git commit -m "comentarios"
enviar alterações ao repositorio remoto: git push origin master -> * Master pode ser alterado para qualquer ramo (branch)
atualizar repositorio local: git pull

Conectar servidor remoto ao repocitorio: git remote add origin "servidor"
Obter um repositorio: git clone usuario@servidor: /caminho repositorio

#Docker e Docker Compose

Instalar: sudo apt install docker.io
Confirmar: docker --version
Listar containers: sudo docker ps

Instalar curl
sudo apt install curl
curl --version

Instalar Docker Compose
sudo apt update
curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version

Adicionar o user ubunto no grupo docker
sudo usermod -aG docker $USER
-Necessário reiniciar o Ubuntu

Executar.....
sudo docker login
sudo docker run hello-world

#Executar Arquivos .SH
Permissão de execução: chmod +x filename.sh
Executar arquivo: sudo ./filename.sh











