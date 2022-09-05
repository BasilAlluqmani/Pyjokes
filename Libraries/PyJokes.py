# install on command line
## pip install pyjokes ##

# import in python idle/editor
import pyjokes

joke1 = pyjokes.get_joke(language='en', category='all')

print(joke1)

# Get Jokes


print("-------------------------------------------------")

jokes = pyjokes.get_jokes(language='en', category='all')

for i in range(5):
    print(i + 1, "-", jokes[i])
