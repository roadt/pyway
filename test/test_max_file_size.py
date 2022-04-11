


def file_size(f):
    with open(f, 'rb') as f:
        f.seek(0, 2)
        return f.tell()

def create_max_file(f):
    with open(f, 'wb') as f:
        while True:
            f.write(b'0')

        
    
