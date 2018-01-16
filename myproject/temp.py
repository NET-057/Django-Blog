import os

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(base, 'media')
print(MEDIA_ROOT)