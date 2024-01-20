print('Hello'.lower() )              # 'hello'
print('Straﬂe'.lower()       )       # 'straﬂe'
print('Straﬂe'.upper().lower()  )    # 'strasse'
# Example of incorrect result when used for unicode case-insensitive matching
print('Straﬂe'.upper().lower() == 'Straﬂe'.lower()) # False ('strasse' != 'straﬂe')

'Hello'.casefold()            # 'hello'
'Straﬂe'.casefold()           # 'strasse'
'Straﬂe'.upper().casefold()   # 'strasse'
# Returns the correct result when used for unicode case-insensitive matching
'Straﬂe'.upper().casefold() == 'Straﬂe'.casefold() # True