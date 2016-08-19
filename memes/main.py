#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	generatorID ='363'
    	imageId = '19494'
    	username ='CSSIbot'
    	password ='cssi'
    	response = urllib2.urlopen(
    		'http://version1.api.memegenerator.net/Instance_Create?'+
    		'username=CSSIbot&'+
    		'password=cssi&'+
    		'languageCode=en&'+
    		'generatorID=363&'+
    		'imageID=19494&'+
    		'text0=you+got+that&'+
    		'text1=mac+and+cheese'
    	)
    	response_text = response.read()
    	response_data = json.loads(response_text)
    	meme = response_data['result']['instanceImageUrl']
    	self.response.write("<img src ="+ meme+">")
    	"""
        self.response.write('Hello world!')
        response = urllib2.urlopen('http://version1.api.memegenerator.net/Generators_Select_ByPopular?pageIndex=3&pageSize=12&days=7')
        response_text = response.read()
        response_data = json.loads(response_text)
        for generator_data in response_data['result']:
        	imgUrl = generator_data['imageUrl']
        	self.response.write('<img src='+imgUrl+'>')
        	self.response.write(str(generator_data['generatorID'])+'<br>')
        	self.response.write(generator_data['imageUrl']+ '<br>')
		"""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
