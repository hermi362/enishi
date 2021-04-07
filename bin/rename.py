import os

# [os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]

[os.rename(f, f.replace('JPG', 'jpg')) for f in os.listdir('.') if not f.startswith('.')]
[os.rename(f, f.replace('a', 'A')) for f in os.listdir('.') if not f.startswith('.')]
[os.rename(f, f.replace('b', 'B')) for f in os.listdir('.') if not f.startswith('.')]
[os.rename(f, f.replace('c', 'C')) for f in os.listdir('.') if not f.startswith('.')]
[os.rename(f, f.replace('d', 'D')) for f in os.listdir('.') if not f.startswith('.')]

