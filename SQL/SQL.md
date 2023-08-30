# SQL


## Comandos SQL


| Comando | Descrição |
| --- | --- |
| `SELECT` | extrai dados de um banco de dados |
| `UPDATE` | atualiza dados em um banco de dados | 
|`DELETE` | exclui dados de um banco de dados |
|`INSERT INTO`       |insere novos dados em um banco de dados|
|`CREATE DATABASE`   |cria um novo banco de dados|
|`ALTER DATABASE`    |modifica um banco de dados|
|`CREATE TABLE`      |cria uma nova tabela|
|`ALTER TABLE`       |modifica uma tabela|
|`DROP TABLE`        |exclui uma tabela|
|`CREATE INDEX`      |cria um índice (chave de pesquisa)|
|`DROP INDEX`        |exclui um índice|

```SQL
SELECT * FROM Customers
```


### WHERE
O comando `WHERE` em SQL é procedido por operadores lógicos, os mesmos habituais:
| Operador | Descrição |
| --- | --- |
|=	|Equal	|
|>	|Greater than	|
|<	|Less than	|
|>=|	Greater than or equal	|
|<=|	Less than or equal	|
|<>|	Not equal. Note: In some |versions of SQL this operator may be written as !=|

Algum exemplo:
```SQL
SELECT City, CustomerName FROM Customers WHERE City="Berlin";
```

#### Operadores lógicos diferentes que podem ser usados com `WHERE`
- BETWEEN
```SQL
SELECT ProductName, Unit, Price  FROM Products
WHERE Price BETWEEN 21.2 AND 60;
```
O operador BETWEEN é usado para verificar se um valor está dentro de um intervalo inclusivo. Nesse caso, ele verificará se o valor da coluna "Price" está entre 21.2 e 60, incluindo ambos os limites `([21,2, 60])`.

- LIKE
```SQL
SELECT CustomerID, CustomerName, City FROM Customers
WHERE City LIKE 's%';
```
O operador LIKE é usado para fazer comparações de padrões. O '%' é um caractere curinga que representa zero ou mais caracteres, então 's%' significa qualquer valor que comece com 's' seguido por zero ou mais caracteres adicionais.

- IN
```SQL
SELECT * FROM Customers
WHERE City IN ('Paris','London');
```
O operador IN é usado para verificar se um valor está em um conjunto de valores especificados entre parênteses.


