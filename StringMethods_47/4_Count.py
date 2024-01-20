print("4. COUNT\n" + "*" * 83)
print(
    """1. Return number of non-overlapping occurrences of substring subs in a \
string
2. Counts the number of occurrences of sub string present in the given string
3. Can also check with slicing the string as well
4. Case sensitive
5. Returns Integer"""
)

print("*" * 83)
print(
    """SYNTAX => String.count(substring,start_index,end_index)
start_index and end_index are optional"""
)
print("*" * 83)

word = "ab_ab_abc_ab_a=abcd"

c1 = word.count("a")  # 6 occurence of 'a'
c2 = word.count("ab")  # 5 occurence of 'ab'
c3 = word.count("ab_")  # 3 occurence of 'ab_'
c4 = word.count("abcd")  # 1 occurence of 'abcd'
c5 = word.count("ab", 2, 6)  # 1 occurence of 'ab' in '_ab_'

print("Given String <=", word)
print("count of 'a' in given string =>", c1)
print("count of 'ab' in given string =>", c2)
print("count of 'ab_' in given string =>", c3)
print("count of 'abcd' in given string =>", c4)
print("count of 'ab' in given string(slice) =>", c5)

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.count)
