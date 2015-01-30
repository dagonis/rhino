# rhino
A python tool to find reverse dns records for blocks of IPs (Python3.3+).

#Usage
rhino.py [range] <br /><br />
Optional Arguments<br />
-o to write results to a file <br />
-f to log failures, will be written to the above file if that option is enabled <br />

##Example
python3 rhino.py 4.2.2.0/30 -o rhino_test.txt -f<br /><br />
Output:<br />
4.2.2.0 - none<br />
4.2.2.1 - a.resolvers.level3.net<br />
4.2.2.2 - b.resolvers.level3.net<br />
4.2.2.3 - c.resolvers.level3.net<br />