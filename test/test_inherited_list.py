


class List(list):
    def __getitem__(self, idx):
        if idx >= len(self):
            return None
        else:
            list.__getitem__(self,idx)

a = List()
print a[3]
print a[0]
a.append(1)
print a[0]
