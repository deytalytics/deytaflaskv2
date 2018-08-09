def log_visitor(env):
	import psycopg2

	hostname = 'aa1q1kus00tfvcf.cicyn2v77if2.us-west-2.rds.amazonaws.com'
	username = 'nesta'
	password = 'xedos123'
	database = 'nesta'

	#Connect to the database
	myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
	cur=myConnection.cursor()
	if 'HTTP_REFERER' in env:
		ins_string = "insert into ip_traffic values (current_timestamp, '"+env['REMOTE_ADDR']+"','"+env['HTTP_REFERER']+"')"
		cur.execute(ins_string)
	myConnection.commit()
	myConnection.close()
	return