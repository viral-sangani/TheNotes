### These SQL commands are mainly categorized into four categories as:

1. DDL – Data Definition Language
2. DQl – Data Query Language
3. DML – Data Manipulation Language
4. DCL – Data Control Language

![alt text](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190826175059/Types-of-SQL-Commands.jpg "Diagram 1")

---------------------

# DML
DML is short name of Data Manipulation Language which deals with data manipulation and includes most common SQL statements such SELECT, INSERT, UPDATE, DELETE, etc., and it is used to store, modify, retrieve, delete and update data in a database.

* SELECT - retrieve data from a database  
    Eg. [Refer this link for All SELECT queries](https://bytescout.com/blog/20-important-sql-queries.html)  
        [Refer this link for video tutorial on Advance SELECT queries](https://youtu.be/s_RJEcMPYNE)

* INSERT - insert data into a table  
    Eg. [Refer this link for All INSERT queries](https://www.techonthenet.com/sql/insert.php)  

* UPDATE - updates existing data within a table  
    Eg. [Refer this link for All UPDATE queries](https://www.techonthenet.com/sql_server/update.php)  

* DELETE - Delete all records from a database table  
    Eg. [Refer this link for All UPDATE queries](https://www.techonthenet.com/sql/delete.php)  

* MERGE - UPSERT operation (insert or update)  
    Eg. [Refer this link for Detailed explaination about MERGE queries](https://www.mssqltips.com/sqlservertip/1704/using-merge-in-sql-server-to-insert-update-and-delete-at-the-same-time/)  

* CALL - call a PL/SQL or Java subprogram  
    This is OracleDB Syntax. Refer Below link for OracleDB.  

* EXPLAIN PLAN - interpretation of the data access path  
    This is OracleDB Syntax. Refer Below link for OracleDB.  

* LOCK TABLE - concurrency Control  
    This is OracleDB Syntax. Refer Below link for OracleDB.  

## !Important
### OracleDB
[Refer this link for all OracleDB detailed explaination](https://www.techonthenet.com/oracle/index.php)


# DDL
DDL(Data Definition Language) : DDL or Data Definition Language actually consists of the SQL commands that can be used to define the database schema. It simply deals with descriptions of the database schema and is used to create and modify the structure of database objects in the database.

* Data Definition Language is used to define the database structure or schema. DDL is also used to specify additional properties of the data. The storage structure and access methods used by the database system by a set of statements in a special type of DDL called a data storage and definition language. These statements define the implementation details of the database schema, which are usually hidden from the users. The data values stored in the database must satisfy certain consistency constraints.
For example, suppose the university requires that the account balance of a department must never be negative. The DDL provides facilities to specify such constraints. The database system checks these constraints every time the database is updated. In general, a constraint can be an arbitrary predicate pertaining to the database. However, arbitrary predicates may be costly to the test. Thus, the database system implements integrity constraints that can be tested with minimal overhead.

* Domain Constraints : A domain of possible values must be associated with every attribute (for example, integer types, character types, date/time types). Declaring an attribute to be of a particular domain acts as the constraints on the values that it can take.
Referential Integrity : There are cases where we wish to ensure that a value appears in one relation for a given set of attributes also appear in a certain set of attributes in another relation i.e. Referential Integrity. For example, the department listed for each course must be one that actually exists.
Assertions : An assertion is any condition that the database must always satisfy. Domain constraints and Integrity constraints are special form of assertions.
Authorization : We may want to differentiate among the users as far as the type of access they are permitted on various data values in database. These differentiation are expressed in terms of Authorization. The most common being :
read authorization – which allows reading but not modification of data ;
insert authorization – which allow insertion of new data but not modification of existing data
update authorization – which allows modification, but not deletion.

Examples of DDL commands:  

* CREATE – is used to create the database or its objects (like table, index, function, views, store procedure and triggers).  
...	Eg. [Refer this link for All CREATE queries](https://www.techonthenet.com/sql/tables/create_table.php)  

* DROP – is used to delete objects from the database.  
...	Eg. [Refer this link for All DROP queries](https://www.techonthenet.com/sql/tables/drop_table.php)

* ALTER-is used to alter the structure of the database.  
...	Eg. [Refer this link for All ALTER queries](https://www.techonthenet.com/sql/tables/alter_table.php)

* TRUNCATE–is used to remove all records from a table, including all spaces allocated for the records are removed.  

* COMMENT –is used to add comments to the data dictionary.  
...	Eg. [Refer this link for All Comment Options](https://dev.mysql.com/doc/refman/8.0/en/comments.html)

* RENAME –is used to rename an object existing in the database.  
...	Eg. [Refer this link for RENAME queries](https://www.javatpoint.com/sql-rename-table)


# DCl
DCL is short name of Data Control Language which includes commands such as GRANT and mostly concerned with rights, permissions and other controls of the database system.

The operations for which privileges may be granted to or revoked from a user or role apply to both the Data definition language (DDL) and the Data manipulation language (DML), and may include CONNECT, SELECT, INSERT, UPDATE, DELETE, EXECUTE and USAGE.

In the Oracle database, executing a DCL command issues an implicit commit. Hence, you cannot roll back the command.

* GRANT - allow users access privileges to the database
* REVOKE - withdraw users access privileges given by using the GRANT command
... Eg. [Reger this link for GRANT/REVOKE queries](https://www.techonthenet.com/sql_server/grant_revoke.php)