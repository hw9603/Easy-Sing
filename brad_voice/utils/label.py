
print '''<?xml version="1.0" encoding="UTF-8"?><maryxml xmlns="http://mary.dfki.de/2002/MaryXML" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="0.5" xml:lang="en-US">
<p>
<s>'''

for i in range(600):
	print '''<prosody rate="500ms" pitch="''' + str(1200 + 1*i) + '''abs">
<t ph="i" >i</t>
</prosody><boundary duration="500"/>'''
#<break time="1s" />
print '''</s>
</p>
</maryxml>'''




