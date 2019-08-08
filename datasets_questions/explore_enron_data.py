#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

#enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb")) # in 2.7 use "r" only.
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
##print enron_data.keys()
##print enron_data.values()[0].keys()
print "number of individuals: ", len(enron_data.keys())
print "number of features: ", len(enron_data.values()[0])
print "number of POI's in 'enron_data': ", sum([1 for name in enron_data if enron_data[name]["poi"]==1])

#../ final_project / poi_email_addresses.py
poi_raw_txt = open("../final_project/poi_names.txt", "r").readlines()
poi_text = [t for t in poi_raw_txt if t[0]=='(']
##print "number of POI's from manually currated list: ", len(poi_text)
'''
'METTS MARK', 'BAXTER JOHN C', 'ELLIOTT STEVEN', 'CORDES WILLIAM R', 'HANNON KEVIN P', 'MORDAUNT KRISTINA M', 'MEYER ROCKFORD G',
'MCMAHON JEFFREY', 'HORTON STANLEY C', 'PIPER GREGORY F', 'HUMPHREY GENE E', 'UMANOFF ADAM S', 'BLACHMAN JEREMY M', 'SUNDE MARTIN',
'GIBBS DANA R', 'LOWRY CHARLES P', 'COLWELL WESLEY', 'MULLER MARK S', 'JACKSON CHARLENE R', 'WESTFAHL RICHARD K', 
'WALTERS GARETH W', 'WALLS JR ROBERT H', 'KITCHEN LOUISE', 'CHAN RONNIE', 'BELFER ROBERT', 'SHANKMAN JEFFREY A', 'WODRASKA JOHN', 
'BERGSIEKER RICHARD P', 'URQUHART JOHN A', 'BIBI PHILIPPE A', 'RIEKER PAULA H', 'WHALEY DAVID A', 'BECK SALLY W', 'HAUG DAVID L', 
'ECHOLS JOHN B', 'MENDELSOHN JOHN', 'HICKERSON GARY J', 'CLINE KENNETH W', 'LEWIS RICHARD', 'HAYES ROBERT E', 'MCCARTY DANNY J', 
'KOPPER MICHAEL J', 'LEFF DANIEL P', 'LAVORATO JOHN J', 'BERBERIAN DAVID', 'DETMERING TIMOTHY J', 'WAKEHAM JOHN', 'POWERS WILLIAM', 
'GOLD JOSEPH', 'BANNANTINE JAMES M', 'DUNCAN JOHN H', 'SHAPIRO RICHARD S', 'SHERRIFF JOHN R', 'SHELBY REX', 'LEMAISTRE CHARLES', 
'DEFFNER JOSEPH M', 'KISHKILL JOSEPH G', 'WHALLEY LAWRENCE G', 'MCCONNELL MICHAEL S', 'PIRO JIM', 'DELAINEY DAVID W', 
'SULLIVAN-SHAKLOVITZ COLLEEN', 'WROBEL BRUCE', 'LINDHOLM TOD A', 'MEYER JEROME J', 'LAY KENNETH L', 'BUTTS ROBERT H', 
'OLSON CINDY K', 'MCDONALD REBECCA', 'CUMBERLAND MICHAEL S', 'GAHN ROBERT S', 'MCCLELLAN GEORGE', 'HERMANN ROBERT J', 
'SCRIMSHAW MATTHEW', 'GATHMANN WILLIAM D', 'HAEDICKE MARK E', 'BOWEN JR RAYMOND M', 'GILLIS JOHN', 'FITZGERALD JAY L', 
'MORAN MICHAEL P', 'REDMOND BRIAN L', 'BAZELIDES PHILIP J', 'BELDEN TIMOTHY N', 'DURAN WILLIAM D', 'THORN TERENCE H', 
'FASTOW ANDREW S', 'FOY JOE', 'CALGER CHRISTOPHER F', 'RICE KENNETH D', 'KAMINSKI WINCENTY J', 'LOCKHART EUGENE E', 'COX DAVID', 
'OVERDYKE JR JERE C', 'PEREIRA PAULO V. FERRAZ', 'STABLER FRANK', 'SKILLING JEFFREY K', 'BLAKE JR. NORMAN P', 'SHERRICK JEFFREY B', 
'PRENTICE JAMES', 'GRAY RODNEY', 'PICKERING MARK R', 'THE TRAVEL AGENCY IN THE PARK', 'NOLES JAMES L', 'KEAN STEVEN J', 'TOTAL', 
'FOWLER PEGGY', 'WASAFF GEORGE', 'WHITE JR THOMAS E', 'CHRISTODOULOU DIOMEDES', 'ALLEN PHILLIP K', 'SHARP VICTORIA T', 
'JAEDICKE ROBERT', 'WINOKUR JR. HERBERT S', 'BROWN MICHAEL', 'BADUM JAMES P', 'HUGHES JAMES A', 'REYNOLDS LAWRENCE', 
'DIMICHELE RICHARD G', 'BHATNAGAR SANJAY', 'CARTER REBECCA C', 'BUCHANAN HAROLD G', 'YEAP SOON', 'MURRAY JULIA H', 'GARLAND C KEVIN', 
'DODSON KEITH', 'YEAGER F SCOTT', 'HIRKO JOSEPH', 'DIETRICH JANET R', 'DERRICK JR. JAMES V', 'FREVERT MARK A', 'PAI LOU L', 
'BAY FRANKLIN R', 'HAYSLETT RODERICK J', 'FUGH JOHN L', 'FALLON JAMES B', 'KOENIG MARK E', 'SAVAGE FRANK', 'IZZO LAWRENCE L', 
'TILNEY ELIZABETH A', 'MARTIN AMANDA K', 'BUY RICHARD B', 'GRAMM WENDY L', 'CAUSEY RICHARD A', 'TAYLOR MITCHELL S', 
'DONAHUE JR JEFFREY M', 'GLISAN JR BEN F'

'salary', 'to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 'bonus', 'restricted_stock',
'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value', 'expenses', 'loan_advances', 'from_messages',
'other', 'from_this_person_to_poi', 'poi', 'director_fees', 'deferred_income', 'long_term_incentive', 'email_address',
 'from_poi_to_this_person'
'''
def explore_data(name,feature):
    try:
        stock_value = enron_data[name][feature]
        return stock_value
    except:
        try:
            enron_data[name]
        except:
            print "'", name, "' not found."
            return None
        try:
            enron_data[name][feature]
        except:
            print "'", feature, "' not found."
'''
name = "COLWELL WESLEY"
enron_key = 'from_this_person_to_poi'
print name, enron_key, explore_data(name,enron_key)

name = "SKILLING JEFFREY K"
enron_key = "exercised_stock_options"
print name, enron_key, ": ", explore_data(name,enron_key)

name = "LAY KENNETH L"
enron_key = "total_payments"
ken = explore_data(name, enron_key)
name = "SKILLING JEFFREY K"
jeff = explore_data(name, enron_key)
name = "FASTOW ANDREW S"
andy = explore_data(name, enron_key)
print "ken, jeff, andy", ken, jeff, andy
'''

##print "explicit salaries", sum([1 for name in enron_data.keys() if type(enron_data[name]['salary']) is int])
##print   "email addresses", sum([1 for name in enron_data.keys() if enron_data[name]['email_address'] != "NaN"])

# -*- coding: utf-8 -*-
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

Q29 = '''How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
What percentage of people in the dataset as a whole is this?'''
nan = sum([1 for name in enron_data.keys() if enron_data[name]['total_payments'] == "NaN"])
print "nan:",nan
tot = len(enron_data.keys())
print   "% of total payments which are NaN", 100.0*nan/tot

Q30 = '''How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?'''
poi = [name for name in enron_data if enron_data[name]["poi"]==1]
print "poi's", len(poi)
poi_nan = sum([1 for name in poi if enron_data[name]['total_payments']=="NaN"])
print poi_nan