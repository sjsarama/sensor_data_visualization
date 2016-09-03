# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:18:40 2016

@author: ramamoorthy
"""
import json
from collections import namedtuple

def get_tag_info():
	with open('data.json', 'r') as source_file_name:         
	        json_data = json.load(source_file_name)
	        for i in range (0,len(json_data["links"])):
	            #print len(json_data["links"])
	            print json_data["links"][i]['tool_name'] 

	x = filter(lambda json_data: json_data['tool_name']=='Error',json_data["links"])
	y = filter(lambda json_data: json_data['tool_name']== None, json_data["links"])

	#print x
	print "total:", len(json_data["links"])
	print "no of tools without tag:", len(x)
	print "no of tools without tag name:", len(y)
	z= len(json_data["links"])-len(x) - len(y)
	print "no of tools with tag:", abs (z)

	tag_data = namedtuple('tag_data','x y z')
	tag_data.x = len(x)
	tag_data.y = len(y)
	tag_data.z = abs(z)

	return tag_data