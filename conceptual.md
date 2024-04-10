### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

Postgresql is an object-relational database management system (ORDBMS) that is open-source and is known for its reliability and robustness. It is a powerful database system that is used by many companies and organizations to store and manage their data.

- What is the difference between SQL and PostgreSQL?

SQL stands for Structured Query Language and is a standard language for managing and manipulating databases. PostgreSQL is a specific database management system that uses SQL as its query language.

- In `psql`, how do you connect to a database?

Type 'psql' in the terminal to open the psql command line interface. Then type '\c database_name' to connect to a specific database. Alternatively, you can specify the database name when you open psql by typing 'psql database_name'.

- What is the difference between `HAVING` and `WHERE`?

HAVING is used to filter the results of a query based on aggregate functions, while WHERE is used to filter the results of a query based on individual rows.

- What is the difference between an `INNER` and `OUTER` join?

An INNER join returns only the rows that have matching values in both tables, while an OUTER join returns all rows from one table and the matching rows from the other table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

A LEFT OUTER join returns all rows from the left table and the matching rows from the right table, while a RIGHT OUTER join returns all rows from the right table and the matching rows from the left table.

- What is an ORM? What do they do?

An ORM (Object-Relational Mapping) is a programming technique that maps objects from an object-oriented programming language to tables in a relational database. ORMs provide a way to interact with a database using objects and classes, making it easier to work with databases in an object-oriented way.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

AJAX is typically used to update parts of a web page without reloading the entire page, while `requests` is used to interact with external APIs or web services from the server.

- What is CSRF? What is the purpose of the CSRF token?

CSRF is an abbreviation for Cross-Site Request Forgery, which is a type of attack where a malicious website tricks a user into making a request to another website on which the user is authenticated. The purpose of the CSRF token is to prevent this type of attack by including a unique token in each form submission that is validated by the server to ensure that the request is legitimate.

- What is the purpose of `form.hidden_tag()`?

`form.hidden_tag()` is used to generate a hidden input field in a WTForms form that contains a CSRF token. This token is used to prevent CSRF attacks by including a unique token in each form submission that is validated by the server to ensure that the request is legitimate.