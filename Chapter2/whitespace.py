print("Python")

print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Removing whitespace

favorite_language = "python "
print(favorite_language)

# removes whitespace at the end of the string
print(favorite_language.rstrip())

print(favorite_language)

favorite_language = favorite_language.rstrip()

# removes whitespace at the beginning of the string

favorite_language = " Python "

print(favorite_language.lstrip())

#removes whitespace from the beginning and end

print(favorite_language.strip())


#Removing prefixes

URL = "https://www.jacobkruse.com"

domain = URL.removeprefix("https://")

print(domain)
