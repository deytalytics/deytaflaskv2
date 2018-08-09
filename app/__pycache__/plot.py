import plotly
from plotly.graph_objs import Bar, Layout
import plotly.graph_objs as go

import psycopg2

hostname = 'aa1hs7q67yf2wvi.cicyn2v77if2.us-west-2.rds.amazonaws.com'
username = 'nesta'
password = 'xedos123'
database = 'nesta'

#Connect to the database
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
cur=myConnection.cursor()

qry_string="""
select to_date(incorporationdate,'dd/mm/yyyy')::text, count(1) from uk_company_data 
where to_date(incorporationdate,'dd/mm/yyyy')>='01/01/2017'
group by to_date(incorporationdate,'dd/mm/yyyy')::text
order by 1
"""

cur.execute (qry_string)

xvals=[]
yvals=[]

for rowx, rowy in cur.fetchall():
	xvals.append(rowx)
	yvals.append(rowy)

plotly.offline.plot(
{"data": [go.Bar(x=xvals, y=yvals)], 
"layout": Layout(title="UK companies incorporated in 2017 (til end of April)")}, 
filename="../static/newukcompanies.html", show_link=False)