# procurando_neymo
Jogo inspirado no melhor jogador da história do esporte.


# Protocolo Cliente-Servidor(tipos de mensagem):
1. Solicitação para ser host de uma partida. Primeiro byte é o tipo de mensagem. Próximos 16 bytes são o nome da sala, que será o identificador do usuário para ser localizado.
2. Solicitação para jogar com outro usuário. Primeiro byte é o tipo de mensagem. Próximos 16 bytes são o nome da sala.
3. Solicitação para jogar com qualquer um. 1 byte com tipo de mensagem.  
5. Resposta do servidor. Primeiro byte é o tipo de mensagem. Próximos 4 bytes são o endereço de IP do dono da sala. Próximos bytes são a porta do dono da sala. Caso a solicitação tenha sido para criar uma sala, retorna o próprio endereço de IP e porta do peer que fez as solicitação. 

# Protocolo P2P (tipos de mensagem):
1. Mensagens de controle:
- O primeiro byte identifica se o usuário está passando ou solicitando o controle do fluxo de execução do programa para si. Os próximos 4 bytes são reservados para identificar as cartas movidas (2 bytes para cada carta).
