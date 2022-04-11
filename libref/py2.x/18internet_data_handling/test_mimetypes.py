
import mimetypes

#mimetypes.guess_type(url, strict=True) - >  (type, encoding)
mimetypes.guess_type('http://www.163.com/index.html')

#mimetypes.guess_all_extensions(type, strict=True
mimetypes.guess_all_extensions('text/html')
mimetypes.guess_all_extensions('image/jpeg')

#mimetypes.guess_extension(type, strict=True)
mimetypes.guess_extension('text/html')

#mimetypes.init(files=None)
mimetypes.init()

#mimetypes.read_mime_types(filename)

#mimetypes.add_type(type, ext, strict=True)


#
mimetypes.inited



#mimetypes.knownfiles
mimetypes.knownfiles
#['/etc/mime.types', '/etc/httpd/mime.types', '/etc/httpd/conf/mime.types', '/etc/apache/mime.types', '/etc/apache2/mime.types', '/usr/local/etc/httpd/conf/mime.types', '/usr/local/lib/netscape/mime.types', '/usr/local/etc/httpd/conf/mime.types', '/usr/local/etc/mime.types']


#mimetypes.suffix_map
mimetypes.suffix_map


mimetypes.encodings_map
#{'.bz2': 'bzip2', '.Z': 'compress', '.gz': 'gzip', '.xz': 'xz'}

mimetypes.types_map
#{'.obj': 'application/octet-stream', '.ra': 'audio/x-pn-realaudio', '.wsdl': 'application/xml', '.dll': 'application/octet-stream', '.ras': 'image/x-cmu-raster', '.ram': 'application/x-pn-realaudio', '.bcpio': 'application/x-bcpio', '.sh': 'application/x-sh', '.m1v': 'video/mpeg', '.xwd': 'image/x-xwindowdump', '.doc': 'application/msword', '.bmp': 'image/x-ms-bmp', '.shar': 'application/x-shar', '.js': 'application/javascript', '.src': 'application/x-wais-source', '.dvi': 'application/x-dvi', '.aif': 'audio/x-aiff', '.ksh': 'text/plain', '.dot': 'application/msword', '.mht': 'message/rfc822', '.p12': 'application/x-pkcs12', '.css': 'text/css', '.csh': 'application/x-csh', '.pwz': 'application/vnd.ms-powerpoint', '.pdf': 'application/pdf', '.cdf': 'application/x-netcdf', '.pl': 'text/plain', '.ai': 'application/postscript', '.jpe': 'image/jpeg', '.jpg': 'image/jpeg', '.py': 'text/x-python', '.xml': 'text/xml', '.jpeg': 'image/jpeg', '.ps': 'application/postscript', '.gtar': 'application/x-gtar', '.xpm': 'image/x-xpixmap', '.hdf': 'application/x-hdf', '.nws': 'message/rfc822', '.tsv': 'text/tab-separated-values', '.xpdl': 'application/xml', '.p7c': 'application/pkcs7-mime', '.ico': 'image/vnd.microsoft.icon', '.eps': 'application/postscript', '.ief': 'image/ief', '.so': 'application/octet-stream', '.xlb': 'application/vnd.ms-excel', '.pbm': 'image/x-portable-bitmap', '.texinfo': 'application/x-texinfo', '.xls': 'application/vnd.ms-excel', '.tex': 'application/x-tex', '.rtx': 'text/richtext', '.html': 'text/html', '.aiff': 'audio/x-aiff', '.aifc': 'audio/x-aiff', '.exe': 'application/octet-stream', '.sgm': 'text/x-sgml', '.tif': 'image/tiff', '.mpeg': 'video/mpeg', '.ustar': 'application/x-ustar', '.gif': 'image/gif', '.ppt': 'application/vnd.ms-powerpoint', '.pps': 'application/vnd.ms-powerpoint', '.sgml': 'text/x-sgml', '.ppm': 'image/x-portable-pixmap', '.latex': 'application/x-latex', '.bat': 'text/plain', '.mov': 'video/quicktime', '.ppa': 'application/vnd.ms-powerpoint', '.tr': 'application/x-troff', '.rdf': 'application/xml', '.xsl': 'application/xml', '.eml': 'message/rfc822', '.nc': 'application/x-netcdf', '.sv4cpio': 'application/x-sv4cpio', '.bin': 'application/octet-stream', '.h': 'text/plain', '.tcl': 'application/x-tcl', '.wiz': 'application/msword', '.o': 'application/octet-stream', '.a': 'application/octet-stream', '.c': 'text/plain', '.wav': 'audio/x-wav', '.vcf': 'text/x-vcard', '.xbm': 'image/x-xbitmap', '.txt': 'text/plain', '.au': 'audio/basic', '.t': 'application/x-troff', '.tiff': 'image/tiff', '.texi': 'application/x-texinfo', '.oda': 'application/oda', '.ms': 'application/x-troff-ms', '.rgb': 'image/x-rgb', '.me': 'application/x-troff-me', '.sv4crc': 'application/x-sv4crc', '.qt': 'video/quicktime', '.mpa': 'video/mpeg', '.mpg': 'video/mpeg', '.mpe': 'video/mpeg', '.avi': 'video/x-msvideo', '.pgm': 'image/x-portable-graymap', '.pot': 'application/vnd.ms-powerpoint', '.mif': 'application/x-mif', '.roff': 'application/x-troff', '.htm': 'text/html', '.man': 'application/x-troff-man', '.etx': 'text/x-setext', '.zip': 'application/zip', '.movie': 'video/x-sgi-movie', '.pyc': 'application/x-python-code', '.png': 'image/png', '.pfx': 'application/x-pkcs12', '.mhtml': 'message/rfc822', '.tar': 'application/x-tar', '.pnm': 'image/x-portable-anymap', '.pyo': 'application/x-python-code', '.snd': 'audio/basic', '.cpio': 'application/x-cpio', '.swf': 'application/x-shockwave-flash', '.mp3': 'audio/mpeg', '.mp2': 'audio/mpeg', '.mp4': 'video/mp4'}

mimetypes.common_types
#{'.xul': 'text/xul', '.pic': 'image/pict', '.jpg': 'image/jpg', '.mid': 'audio/midi', '.rtf': 'application/rtf', '.pct': 'image/pict', '.pict': 'image/pict', '.midi': 'audio/midi'}