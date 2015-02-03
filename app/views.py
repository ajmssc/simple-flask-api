from flask import render_template, request, jsonify
from app import app
import math
# import mysql.connector
# from cassandra.cluster import Cluster
# from cassandra.query import BatchStatement

# import happybase

# ROUTING/VIEW FUNCTIONS
@app.route('/')
@app.route('/index')
def index():
	# Renders index.html.
	return render_template('index.html')

@app.route('/presentation')
def presentation():
	return render_template('presentation.html')

@app.route('/history_blocks')
def history_blocks():
	return render_template('history_blocks.html')

@app.route('/history_transactions')
def history_transactions():
	return render_template('history_transactions.html')

@app.route('/history_prices')
def history_prices():
	return render_template('history_prices.html')


@app.route('/live')
def live():
	return render_template('live.html')

@app.route('/api')
def api_index():
	return render_template('api.html')

@app.route('/wallets')
def wallets():
	return render_template('wallets.html')

@app.route('/wallets_timed')
def wallets_timed():
	return render_template('wallets_timed.html')




def calculate_granularity(start, end):
	if (int(end)-int(start) > (2*30*24*60*60)): # > 2 month
		g = "daily"
	elif (int(end)-int(start) > (10*24*60*60)): # > 10 days
		g = "hourly"
	else:
		g = "minutely"
	print g + " - Start:%s - End:%s  Diff:%s" % (int(start), int(end), int(end)-int(start))
	return g


@app.route("/api/<api_id>")
@app.route("/api/<api_id>/")
@app.route("/api/<api_id>/<value>")
def api(api_id, value = None):
	return jsonify("")
	#app.logger.debug("Call to " + str(api_id) + " with param " + str(value))
	# if api_id == 'getrealtimestats':
	# 	hbase = happybase.Connection('cloud.soumet.com')
	# 	hbase_realtime_table = hbase.table('realtime_counters')
	# 	result = hbase_realtime_table.row("statistics")
	# 	return jsonify(result)

	# elif api_id == 'gethistory':
	# 	hbase = happybase.Connection('cloud.soumet.com')
	# 	hbase_blocks_table = hbase.table('block_data')
	# 	start = request.args.get("start") if request.args.get("start") != None else "0"
	# 	end = request.args.get("end") if request.args.get("end") != None else "999999999999"
	# 	callback = request.args.get("callback") if request.args.get("callback") != None else ""
	# 	granularity = calculate_granularity(start, end)
	# 	data = hbase_blocks_table.scan(row_start="blockcount_" + granularity + "_" + start.rjust(10, '0'), 
	# 							row_stop="blockcount_" + granularity + "_" + end.rjust(10, '0'))
	# 	results = []
	# 	for val in data:
	# 		results.append([ int(val[0].rsplit("_")[2])*1000, int(val[1]["metadata:count"])])
	# 	return callback + "(" + str(results) + ");"



	# elif api_id == 'gettransactionhistory':
	# 	hbase = happybase.Connection('cloud.soumet.com')
	# 	hbase_blocks_table = hbase.table('block_transactions')
	# 	start = request.args.get("start") if request.args.get("start") != None else "0"
	# 	end = request.args.get("end") if request.args.get("end") != None else "999999999999"
	# 	callback = request.args.get("callback") if request.args.get("callback") != None else ""
	# 	granularity = calculate_granularity(start, end)
	# 	data = hbase_blocks_table.scan(row_start="transactioncount_" + granularity + "_" + start.rjust(10, '0'), 
	# 							row_stop="transactioncount_" + granularity + "_" + end.rjust(10, '0'))
	# 	results = []
	# 	for val in data:
	# 		results.append([ int(val[0].rsplit("_")[2])*1000, int(val[1]["metadata:count"])])
	# 	return callback + "(" + str(results) + ");"

	# elif api_id == 'getpricehistory':
	# 	hbase = happybase.Connection('cloud.soumet.com')
	# 	hbase_blocks_table = hbase.table('exchange_transactions')
	# 	currency = request.args.get("currency")
	# 	currency = currency if currency != None else "ALL"
	# 	start = request.args.get("start") if request.args.get("start") != None else "0"
	# 	end = request.args.get("end") if request.args.get("end") != None else "999999999999"
	# 	callback = request.args.get("callback") if request.args.get("callback") != None else ""
	# 	granularity = calculate_granularity(start, end)
	# 	if currency == "ALL":
	# 		data = {}
	# 		data["USD"] = hbase_blocks_table.scan(row_start="BTC_USD_" + granularity + "_" + start.rjust(10, '0'), 
	# 							row_stop="BTC_USD_" + granularity + "_" + end.rjust(10, '0'))
	# 		data["EUR"] = hbase_blocks_table.scan(row_start="BTC_EUR_" + granularity + "_" + start.rjust(10, '0'), 
	# 							row_stop="BTC_EUR_" + granularity + "_" + end.rjust(10, '0'))
	# 		data["RUR"] = hbase_blocks_table.scan(row_start="BTC_RUR_" + granularity + "_" + start.rjust(10, '0'), 
	# 							row_stop="BTC_RUR_" + granularity + "_" + end.rjust(10, '0'))
	# 		results = { "USD":[], "EUR":[], "RUR":[] }
	# 		for val in data["USD"]:
	# 			results["USD"].append([ int(val[0].rsplit("_")[3])*1000, float(val[1]["metadata:price"])])
	# 		for val in data["EUR"]:
	# 			results["EUR"].append([ int(val[0].rsplit("_")[3])*1000, float(val[1]["metadata:price"])])
	# 		for val in data["RUR"]:
	# 			results["RUR"].append([ int(val[0].rsplit("_")[3])*1000, float(val[1]["metadata:price"])])
	# 	else:
	# 		data = hbase_blocks_table.scan(row_start="BTC_" + currency + "_" + granularity + "_" + start.rjust(10, '0'), 
	# 							row_stop="BTC_" + currency + "_" + granularity + "_" + end.rjust(10, '0'))
	# 		results = []
	# 		for val in data:
	# 			results.append([ int(val[0].rsplit("_")[3])*1000, float(val[1]["metadata:price"])])
	# 	return callback + "(" + str(results) + ");"



	# #wallets.html
	# elif api_id == 'getwalletbuckets':
	# 	hbase = happybase.Connection('cloud.soumet.com')
	# 	hbase_wallets_table = hbase.table('wallet_classes')
	# 	drilldown_level = int(request.args.get("drilldown_level"))
	# 	start = request.args.get("start") if request.args.get("start") != None else "0"
	# 	end = request.args.get("end") if request.args.get("end") != None else "999999999999"
	# 	callback = request.args.get("callback") if request.args.get("callback") != None else ""
	# 	data = hbase_wallets_table.scan(row_start="wallet_" + str(drilldown_level) + "_" + start.rjust(12, '0'), 
	# 							row_stop="wallet_" + str(drilldown_level) + "_" + end.rjust(12, '0'))
	# 	results = {}
	# 	results["name"] = "Number of wallets in category" #wallet_3_000000000001 => 1000 to 2000
	# 	results["colorByPoint"] = True
	# 	if drilldown_level == 3:
	# 		results["dataLabels"] = { 'enabled': True, 'color': '#FFFFFF', 
	# 				'align': 'right', 'x': 4, 'y': 10, 'rotation': -90,
	# 				'style': { 'fontSize': '13px', 'fontFamily': 'Verdana, sans-serif', 'font-decoration': 'none'} }
	# 	else :
	# 		results["dataLabels"] = { 'enabled': True, 'color': '#FFFFFF', 
	# 				'align': 'center', 'y': 29,
	# 				'style': { 'fontSize': '18px', 'fontFamily': 'Verdana, sans-serif', 'font-decoration': 'none'} }
	# 	results["data"] = []
	# 	for entry in data:
	# 		base = int(entry[0].split("_")[2])
	# 		multiplier = math.pow(10, drilldown_level) #ex 1000, 100, 10
	# 		lowrange =  int(base * multiplier) #ex 1000
	# 		highrange = int((base + 1) * multiplier) #ex 2000
	# 		newentry = {"name": "%s to %s BTC" % (lowrange, highrange), "y": int(entry[1]["metadata:count"]), "color": "#27B863"}
	# 		if drilldown_level > 0:
	# 			newentry["drilldown"] = "walletdrill_%s_%s_%s" % (drilldown_level - 1,base * 10,(base+1) * 10)
	# 		results["data"].append(newentry)
	# 	return jsonify(results)


	# elif api_id == 'getwalletlist_cassandra':
	# 	# cluster = Cluster(['cassandra1.soumet.com','cassandra2.soumet.com','cassandra3.soumet.com'])
	# 	# session = cluster.connect('wallets')
	# 	#start = request.args.get("start")
	# 	#end = request.args.get("end")
	# 	results = { "wallets" : []}
	# 	# if start != None and end != None:
	# 	# 	rows = session.execute('SELECT address, balance from data \
	# 	# 		where balance >= %s and balance <= %s limit 1500 ALLOW FILTERING;', (float(start), float(end)))
	# 	# 	rows = sorted(rows, key=lambda x: x.balance, reverse=True)
	# 	# 	for row in rows:
	# 	# 		#print row.address, row.balance
	# 	# 		results["wallets"].append({"address":str(row.address), "balance":str(row.balance)})
	# 	return jsonify(results)

	# elif api_id == 'getwalletlist':
	# 	db = mysql.connector.connect(user='bitcoin', password='insightPassword0944$!',host='bitcoin.soumet.com', database='bitcoin')
	# 	cursor = db.cursor()
	# 	query = ("SELECT wallet, balance FROM wallets WHERE balance >= %s AND balance <= %s order by balance desc LIMIT 1500;")
	# 	start = request.args.get("start")
	# 	end = request.args.get("end")
	# 	results = { "wallets" : []}
	# 	if start != None and end != None:
	# 		cursor.execute(query, (start, end))
	# 	for (wallet, balance) in cursor:
	# 		#print "%s - %s" % (wallet, balance)
	# 		results["wallets"].append({"address":str(wallet), "balance": str(balance)})
	# 	cursor.close()
	# 	db.close()
	# 	return jsonify(results)





	# elif api_id == 'getlivetransactions':
	# 	hbase = happybase.Connection('cloud.soumet.com')
	# 	hbase_transactions_table = hbase.table('realtime')
	# 	if value == None:
	# 		value = "0000000000"
	# 	data = hbase_transactions_table.scan(row_start="transaction_" + str(value), row_stop="transaction_9999999999")
	# 	results = {}
	# 	results["transactions"] = []
	# 	for txid, transaction in data:
	# 		#app.logger.debug(transaction)
	# 		temp_dict = {}
	# 		for key in transaction:
	# 			temp_dict[key.split(':')[1]] = transaction[key]
	# 		temp_dict["time"] = txid.split("_")[1]
	# 		temp_dict["txid"] = txid.split("_")[2]
	# 		#results[txid.split("_")[2]] = temp_dict
	# 		results["transactions"].append(temp_dict)
	# 	results["transactions"] = sorted(results["transactions"], key=lambda k: k['time'], reverse=True) 
	# 		#results.append(elem)
	# 	#app.logger.debug(results)
	# 	#results = hbase_transactions_table.scan( filter=b"SingleColumnValueFilter('metadata','timestamp',>, 'int:" + str(value) + "')")
	# 	#results = [key for key,data in results] #results = hbase_transactions_table.rows()
	# 	#KeyOnlyFilter() AND FirstKeyOnlyFilter()
	# 	#row_start=b'1', row_stop=b'116010',
	# 	#transactions_list=[key for key, data in results]
	# 	return jsonify(results)
	# 	#return ""
	# return jsonify({'error' : 'unknown API call'})
