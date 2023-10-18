Rede social de aprendizado de programação



Banco de dados utilizado: 

- Usei o SQLite mas mais pra frente pretendo mudar para o MySQl ou Postgres

Artifícios de SEGURANÇA implementados:

- O csrf token utilizado para lidar com vulnerabilidades no envio de comandos através da url com um request POST
- O Django forms fornece uma classe de formulário que pode ser utilizada para filtrar e selecionar as informações enviadas por usuários na criação de contas, e pode englobar os models do banco de dados para também registrar essas informações no database
- Um comando "if" que usei na linha 10 do arquivo "myapp/views.py" para assegurar que a url só acessaria a outra página com as informções enviadas na url através do link da homepage para acessar uma sala

