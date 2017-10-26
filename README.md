# ln2sqlmodule

This is an adoption of the awesome [ln2sql](https://github.com/FerreroJeremy/ln2sql) by [Jérémy Ferrero](https://github.com/FerreroJeremy) as a python module so that people can easily use it to create some awesome things !

# INSTALLATION

- Download, unzip and place in your project directory
- `import ln2sqlmodule`

# USAGE

- **ln2sqlmodule.getSql(query,sqlDump)**

	    Parameters :
			query      :    query in natural language
			sqlDump    :    path to sql dump file           
		
		returns : 
			SQL query string

		Example:
			ln2sqlmodule.getSql("get name of all emp","./emp.sql")
			-> "SELECT name FROM  emp"



 