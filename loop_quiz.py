# Iterate through and sort the data  using the for loop and indexing
transaction_data = {"trasaction_id":1010101010,
"source_country":"United Kingdom",
"target_country":"Italy",
"send_currency":"GBP",
"send_amount":1000.00,
"target_currency":"EUR",
"fx_rate":1.1672887,
"fee_pct":0.50,
"platform":"mobile"}

for key in sorted(transaction_data):
    print(key, ":" ,transaction_data[key])

# iterating through using .keys() and indexing
for key in transaction_data.keys():
    print(key, "->", transaction_data[key])

# iterating through using .items() - Returns a view of 
# dictionary items as tuples
print(transaction_data.items())

for k,v in transaction_data.items():
    print(k, "~", v)

# Iterating through nested dictionaries
transaction_data_main = {"transaction_1" 
:{"trasaction_id":1010101010,
"source_country":"United Kingdom",
"target_country":"Italy",
"send_currency":"GBP",
"send_amount":1000.00,
"target_currency":"EUR",
"fx_rate":1.1672887,
"fee_pct":0.50,
"platform":"mobile"},
"transaction_2": {
    "trasaction_id":1010101066,
"source_country":"United Kingdom",
"target_country":"Italy",
"send_currency":"GBP",
"send_amount":9000.00,
"target_currency":"EUR",
"fx_rate":1.12887,
"fee_pct":0.50,
"platform":"mobile"
},
"transaction_3": {
    "trasaction_id":1010101087,
"source_country":"United Kingdom",
"target_country":"Italy",
"send_currency":"GBP",
"send_amount":7000.00,
"target_currency":"EUR",
"fx_rate":1.1672,
"fee_pct":0.50,
"platform":"mobile"
}


}



