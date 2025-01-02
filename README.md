# Mini programa Agenda Telefonica

Este projeto é um formulário simples em PHP para coleta de dados de clientes. Os dados coletados incluem nome, email, telefone, gênero, data de nascimento, cidade, estado e endereço. O formulário utiliza HTML e CSS para a apresentação e estilo, além de PHP para manipulação de dados.

## Estrutura do Projeto

- `formulario.php`: O arquivo principal que contém o formulário HTML e o código PHP para processar os dados enviados.
- `config.php`: Um arquivo que deve conter as configurações de conexão ao banco de dados (não incluído no código fornecido).

## Tecnologias Utilizadas

- **PHP**: Linguagem de programação para o processamento do formulário.
- **HTML**: Estruturação do formulário.
- **CSS**: Estilização do formulário para melhorar a aparência.

## Funcionalidade

 **Coleta de Dados**: O formulário coleta as seguintes informações:
   - Nome
   - Email
   - Telefone
   - Gênero (feminino, masculino, outro)
   - Data de Nascimento
   - Cidade
   - Estado
   - Endereço

 **Armazenamento de Dados**: Após o envio do formulário, os dados são inseridos em uma tabela `usuarios` no banco de dados.

**Execução do Projeto**
1 -Coloque os arquivos no diretório do servidor (ex: htdocs se estiver usando XAMPP).
2 -Acesse http://localhost/formulario.php no seu navegador.
3 -Lembre de estar acessando a porta http://localhost:8000/
4 -Preencha os campos do formulário e clique em "Enviar".

## Considerações Finais !!!
Certifique-se de que a extensão mysqli está habilitada em seu servidor PHP.
Os dados são inseridos diretamente no banco de dados sem validação adicional. Em um ambiente de produção, implemente medidas de segurança, como sanitização de entradas para evitar SQL Injection.

**Contribuições**
Contribuições são bem-vindas! Se você deseja melhorar este projeto, sinta-se à vontade para enviar um pull request ou abrir um issue. Um Grande abraço do Jeff.
