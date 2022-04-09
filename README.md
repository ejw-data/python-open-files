# Python File Management

*Refs:*  https://www.kaggle.com/code/rohanrao/tutorial-on-reading-large-datasets/notebook  

## Paths in Python

When using a file path with `\` in the path, remember that the backslashes are used to escape characters.

For example:  '\r', '\n', '\b', '\c', '\t'

The solution is to either `\\` every backslash, which inserts a single backslash or use a raw string such as `print(r'.\path\file.csv')`.  The `r` instructs the interpreter to not evaluate backslashes as escapes and just as regular backslashes.


### Quick notes:
`print(u'string')` - prints 



### Remaining Questions
In BeautifulSoup, are the outputs in unicode?
*  ie.  `soup[0].encode("ascii")` or `soup[0].encode("latin-1")` or `soup[0].encode("utf-8")` or `soup[0].encode(soup.originalEncoding)` to get the output

### Escaping Refernces
1.  https://python-reference.readthedocs.io/en/latest/docs/str/escapes.html
1.  https://www.w3schools.com/python/gloss_python_escape_characters.asp   
<br>




# Python Open() Parameters

*  `Read Only (‘r’)`: Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exist, raises I/O error. This is also the default mode in which the file is opened.  

*  `Read and Write (‘r+’)`: Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.  

* `Write Only (‘w’)`: Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.  

* `Write and Read (‘w+’)`: Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.  

* `Append Only (‘a’)`: Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.  

* `Append and Read (‘a+’)`: Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.  

*Ref:* https://www.geeksforgeeks.org/open-a-file-in-python/  

<br>

## Pandas
<hr>

Reading Files in Parts  
*  `pd.read_csv(..., nrows, skiprows, chunksize)`
   *  `nrows` : int, default None Number of rows of file to read. Useful for reading pieces of large files*  
   *  `skiprows` : list-like or integer Row numbers to skip (0-indexed) or number of rows to skip (int) at the start of the file  
   *  `chunksize` : int, default None Return TextFileReader object for iteration
* Also keep in mind that this may be helpful when automating:   `skiprows = nend - nrows`



<br>

## Pandas and Dask (Parallel Processing)
<hr>



*Ref:* https://towardsdatascience.com/how-to-handle-large-datasets-in-python-with-pandas-and-dask-34f43a897d55 

<br>

## Databases
<hr>
For really large files then using a database with map reduce to get the contents would be the best route.  

The general process for SQLite is:
1.  Create database 
   ```
    conn = sqlite3.connect('pts.db')
    c = conn.cursor()
   ```

2.  Create Table  
   ```
   c.execute('''CREATE TABLE ptsdata (filename, line, x, y, z''')
   ```

3.  Insert Data  
   ```
   c.execute("INSERT INTO ptsdata VALUES (filename, lineNumber, x, y, z)")
   ```  

4.  Query Data  
   ```
   c.execute("SELECT lineNumber, x, y, z FROM ptsdata WHERE filename=file.txt ORDER BY lineNumber ASC")
   ```  

5.  Get n results  
   ```
   c.fetchmany(size=n)
   ```
