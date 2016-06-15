
s = {"a": [1, 2, 3, 4, 5],
     "x": [0, 1, 2],
     "y": [100, 200],
     "z": {"00": [11, 22]},
     "b": [10, 20, 30, 40],
     "h": {None: None}
     }

for key, val in s.items():
    if key == "z":
        print str(val)

# Inaczej:
s1= s.get('z', 'not found')
print s1.get('00', 'not found')
print s.get('z').get('00')
print s.get('h')