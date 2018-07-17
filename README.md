# procurando_neymo
Jogo inspirado no melhor jogador da história do esporte.


# Protocolo Cliente-Servidor(tipos de mensagem):
1. Solicitação para ser host de uma partida. Primeiro byte é o tipo de mensagem. Próximos 16 bytes são o nome da sala, que será o identificador do usuário para ser localizado.
2. Solicitação para jogar com outro usuário. Primeiro byte é o tipo de mensagem. Próximos 16 bytes são o nome da sala.
3. Solicitação para jogar com qualquer um. 1 byte com tipo de mensagem.  
4. Resposta do servidor para quem criou a sala. Apenas uma mensagem de "ok" em caso de sucesso ou "nope" em caso de falha.
5. Resposta do servidor para quem pediu para entrar numa sala. Primeiro byte é o tipo de mensagem. Próximos 4 bytes são o endereço de IP do dono da sala. Próximos 2 bytes são a porta do dono da sala.  

# Protocolo P2P (tipos de mensagem):
1. Handshaking de 3 etapas:
- Na primeira mensagem o usuário que buscou a sala informa seu nickname. Portanto, 1 byte de tipo de mensagem e 16 bytes de nickname.
- Na segunda mensagem o usuário que criou a sala retorna seu nome de usuário e as informações iniciais do jogo. Portanto, 1 byte de tipo de mensagem, 16 bytes de nickname e 18 bytes sequenciais, onde cada byte é um ID de carta naquela posição do tabuleiro.
- Na terceira mensagem o usuário que está entrando na sala envia um "ok". Portanto, 1 byte de tipo de mensagem. Isso informa ao host que ele pode começar a jogar.

2. Mensagem de jogada de 3 etapas:
- A primeira mensagem é uma sequencia de bytes, onde o primeiro byte é o tipo da mensagem. Os próximos 2 bytes são os IDs das cartas viradas. Próximo byte identifica se as cartas são iguais ou diferentes, e o último byte informa a pontuação atualizada do jogador que enviou a mensagem. 
- A segunda mensagem é uma resposta de 1 byte com o "ok".
- A terceira mensagem também é um "ok", devolvendo o controle para o outro ponto.

3. Mensagem de final de jogo de 3 etapas.
- Quando as cartas se esgotarem, o jogador informa em 16 bytes o nome do ganhador e pergunta para o outro se quer jogar de novo. É uma mensagem de 18 bytes, 1 com o tipo de mensagem, 16 com o nome do jogador e outro com o convite (ou com a despedida).
- O outro jogador responde com uma mensagem de "ok" ou de "nope".
- O jogador recebe a mensagem anterior e volta para o ou termina a conexão.