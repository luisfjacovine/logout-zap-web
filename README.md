# Automação de Logout do WhatsApp Web

Este projeto tem como objetivo garantir a segurança das suas conversas no WhatsApp Web ao desconectar automaticamente a sessão quando você se afasta de dispositivo. 

## Funcionamento

1. **Detecção de saída de casa**: Quando você sai de um raio de 200 metros da localização do seu PC, o seu celular acessa a URL `seudominio.com.br/caminho/completo/index.php/?id=1&stts=1&dispositivo=s23+`, inserindo um registro no banco de dados indicando que você está fora de casa. Para mais informações sobre rotinas de automação em dispositivos Smartphone, segue um tutorial do aplicativo Macrodroid `https://www.youtube.com/watch?v=GbtGoM-3B9Y`

2. **Orquestrador**: O orquestrador (`orquestrador.py`) verifica periodicamente o status no banco de dados:
    - Se o valor encontrado for `0`, não faz nada.
    - Se o valor encontrado for `1`, executa o arquivo `logout.py`.

3. **Execução do Logout**: O `logout.py` se encarrega de realizar o logout do WhatsApp Web, independentemente da quantidade de monitores conectados ou do estado do aplicativo (aberto ou minimizado).

4. **Verificação de Desconexão**: Após a tentativa de logout, o sistema busca pela imagem `boas-vindas.jpg` na tela para confirmar o sucesso da operação.
    - Se a imagem for encontrada, o WhatsApp Web foi desconectado com sucesso e o aplicativo é encerrado com o comando `Alt+F4`.
    - Se a imagem não for encontrada, uma nova tentativa de logout é feita, com um máximo de 3 tentativas.

5. **Atualização do Status**: Após a desconexão bem-sucedida, o orquestrador atualiza o status no banco de dados para indicar que o WhatsApp foi desconectado com sucesso.

## Arquivos do Projeto

- `logout.py`: Script responsável por realizar o logout do WhatsApp Web.
- `orquestrador.py`: Script que verifica o status no banco de dados e orquestra a execução do `logout.py`.
- `index.php`: Página contendo o script que conecta ao banco de dados para atualizar o status utilizando a rotina de automação.
- `query.sql`: Arquivo de configuração da tabela VERIFICADOR no banco de dados.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `requests`
  - `pyautogui`
  - `time`
  - `cv2` (OpenCV)
  - `pymysql` 

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/luisfjacovine/logout-zap-web/
    ```

2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure o banco de dados conforme necessário no `orquestrador.py`.

## Uso

1. Inicie o orquestrador:
    ```sh
    python orquestrador.py
    ```

2. Certifique-se de que seu dispositivo móvel está configurado para acessar a URL de verificação de status ao sair do raio de 200 metros.

## Contribuição

Sinta-se à vontade para contribuir com o projeto. Faça um fork do repositório, crie um branch para sua feature ou correção e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: luisfernandojacovine@gmail.com

---

Esperamos que este projeto ajude a manter suas conversas no WhatsApp Web seguras!
