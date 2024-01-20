print('Hello'.lower() )              # 'hello'
print('Stra�e'.lower()       )       # 'stra�e'
print('Stra�e'.upper().lower()  )    # 'strasse'
# Example of incorrect result when used for unicode case-insensitive matching
print('Stra�e'.upper().lower() == 'Stra�e'.lower()) # False ('strasse' != 'stra�e')

'Hello'.casefold()            # 'hello'
'Stra�e'.casefold()           # 'strasse'
'Stra�e'.upper().casefold()   # 'strasse'
# Returns the correct result when used for unicode case-insensitive matching
'Stra�e'.upper().casefold() == 'Stra�e'.casefold() # True