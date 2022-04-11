from sgmllib import SGMLParser

import htmlentitydefs

class BaseHTMLProcessor(SGMLParser):
	def reset(self):
		# extend (called b SGMLParser.__init__)
		self.pieces = []
		SGMLParser.reset(self)

	def unkown_starttag(self, tag, attrs):
		# called for each start tag
		# attrs is a list of (attr, value) tuples
		strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
		self.pieces.append("<%(tag)s%(strattrs)s>" % locals())
		
	def unknown_endtag(self, tag):
		self.pieces.append("</%(tag)s>" % locals())
		
	def handle_charref(self, ref):
		self.pieces.append("&#%(ref)s;" % locals())
		
	def handle_entityref(self, ref):
		self.pieces.append("&%(ref)s" % locals())
		if htmlentitydefs.entitydefs.has_key(ref):
			self.pieces.append(";")
		
	def handle_data(self, text):
		self.pieces.append(text)
		
	def handle_comment(self, text):
		self.pieces.append("<!--%(text)s-->" % locals())
		
	def handle_pi(self, text):             
    # called for each processing instruction, e.g. <?instruction>
    # Reconstruct original processing instruction.
		self.pieces.append("<?%(text)s>" % locals())

	def handle_decl(self, text):
    # called for the DOCTYPE, if present, e.g.
    # <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    #     "http://www.w3.org/TR/html4/loose.dtd">
    # Reconstruct original DOCTYPE
		self.pieces.append("<!%(text)s>" % locals())

	def output(self):              
		"""Return processed HTML as a single string"""
		return "".join(self.pieces)	
        
        