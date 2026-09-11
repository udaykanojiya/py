print("Hello, World!")

#single line comment
'''multi-line comment
is this.'''

print("""Twinkle, twinkle, little star,
how I wonder what you are!
Up above the world so high,
like a diamond in the sky.""")

import os

import pyjokes

jokes = pyjokes.get_joke(language='en', category='all')
print(jokes)
    
dir_path = os.getcwd()
content_list = os.listdir(dir_path)
    
print(f"--- Contents of '{dir_path}' ---")
for item in content_list:
    print(item)

