s = input('Type something: ')
print('The type primitive of {} is {}'.format(s, type(s)))
print('Has space? ',s.isspace())
print ('Is alphabetic?',s.isalpha())
print('Is numerical?',s.isnumeric())
print('Is alphanumeric? ',s.isalnum())
print('Is in capital letters?',s.isupper())