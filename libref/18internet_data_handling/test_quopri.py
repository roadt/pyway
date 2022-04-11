
from quopri import*

# Encode and decode MIME quoted-printable data

# quopri.decode(input, output[, header])

# quopri.encode(input, output, quotetabs)


# quopri.encodestring(s[, quotetabs])
es = encodestring('asdfafasfsafas我们sadfsafdsaf')
es

# quopri.decodestring(s[, header])
ds = decodestring(es)
ds

