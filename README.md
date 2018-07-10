# ln2sqlmodule

This is an adoption of the awesome [ln2sql](https://github.com/FerreroJeremy/ln2sql) by [Jérémy Ferrero](https://github.com/FerreroJeremy) as a python module so that people can easily use it to create some awesome things !

Things added in ln2sqlmodule :

- API for getting WHERE queries with LIKE and '%'
- INNER JOIN working correctly with FOREIGN KEY
- PRIMARY KEY and FOREIGN KEY detection from ALTER STATEMENT
- Value extraction from natural language

# INSTALLATION

- Download, unzip and place in your project directory
- `import ln2sqlmodule`

# USAGE

- **ln2sqlmodule.getSql(query, sqlDump[, outputFile])**
	returns SQL query from natural language query
	
	[**outputFile** Schema](#outputfile-schema)

	    Parameters :
			query      :    query in natural language
			sqlDump    :    path to sql dump file    
			outputFile :    path to file to output SQL query in json       
		
		returns : 
			SQL query string

		Example:
			ln2sqlmodule.getSql("get name of all emp","./emp.sql")
			-> SELECT name FROM  emp

- **ln2sqlmodule.getSql_like(query, sqlDump[, outputFile])**
	returns SQL query from natural language with **LIKE** with **%** in **WHERE** clause
	
	[**outputFile** Schema](#outputfile-schema)

	    Parameters :
			query      :    query in natural language
			sqlDump    :    path to sql dump file
			outputFile :    path to file to output SQL query in json   
		
		returns : 
			SQL query string with LIKE

		Example:
			ln2sqlmodule.getSql("all data for emp where name is rupinder","./emp.sql")
			-> SELECT * FROM  emp WHERE name LIKE '%rupinder%'

			ln2sqlmodule.getSql("all data for emp where name is 'abc xyz'","./emp.sql")
			-> SELECT * FROM  emp WHERE name LIKE '%abc%xyz'

 

### outputFile Schema
	
	{
		"select": {
			"column": "",
			"type": ""
		},
		"from": {
			"table": ""
		},
		"join": {
		},
		"where": {
		},
		"group_by": {
		},
		"order_by": {
		}
	}
