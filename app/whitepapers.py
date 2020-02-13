from app import app
from flask import render_template, flash, request, redirect, session, url_for

@app.route('/whitepapers')
def whitepapers():
	print("whitepapers")
	return render_template('whitepapers.html')

@app.route('/whitepapers/data_in_the_clouds')
def data_in_the_clouds():
	print("data_in_the_clouds")
	return render_template('data_in_the_clouds.html')