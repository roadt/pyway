
import base64

#b64ecode(s[, altchars]) - altchars - must 2 byts, replace '+' '/'
base64.b64encode('xxxxxddfasdfa+/aa')
base64.b64encode('xxxxxddfasdfa+/aa', '+=')

#b64decode(s[, altchars])
base64.b64decode('eHh4eHhkZGZhc2RmYSsvYWE=')

#standard_b64encode(s)



#standard_b64decode(s)

#urlsafe_b64encode(s)
base64.urlsafe_b64encode('asdfasfasfa')

#urlsafe_b64decode(s)
base64.urlsafe_b64decode('YXNkZmFzZmFzZmE=')

#b32encode(s)
base64.b32encode('asdfasfasf')


#b32decode(s[, casefold[, map01]])


# b16encode(s)

# b16decode(s[, casefold])

# decode(input, output)

#decodestring(s)


#encode(intput, output)

#encodestring(s)




# exmaple
import base64
encoded = base64.b64encode('data to be encoded')
encoded
data = base64.b64decode(encoded)
data