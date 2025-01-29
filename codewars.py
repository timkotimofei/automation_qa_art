# test.assert_equals(f("ababab"), ("ab", 3));
# test.assert_equals(f("abcde"), ("abcde", 1));
# ('dbeac', 1) should equal ('abcde', 1)



def get_count(sentence):
    return sum([sentence.count(i) for i in 'aeiou' if i in sentence])


print(get_count("abracadabra"))


