import unicodedata

def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)

class FuzzyString:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, value):
        return FuzzyString(self.value + value)
    
    def _normalize_caseless(self, text):
        return unicodedata.normalize("NFKD", text.casefold())
    
    def __eq__(self, value):
        return self._normalize_caseless(self.value.lower()) == self._normalize_caseless(value)

    def __gt__(self, value):
        return self._normalize_caseless(self.value) > self._normalize_caseless(value)
    
    def __lt__(self, value):
        return self._normalize_caseless(self.value) < self._normalize_caseless(value)
    
    def __ge__(self, value):
        return self._normalize_caseless(self.value) >= self._normalize_caseless(value)
    
    def __le__(self, value):
        return self._normalize_caseless(self.value) <= self._normalize_caseless(value)
    
    def __contains__(self, key):
        if key and self._normalize_caseless(key) in self._normalize_caseless(self.value):
            return True
        return False
            
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return repr(self.value)



if __name__== "__main__" :
    print('>>> greeting = FuzzyString("Hey TREY!")')
    greeting = FuzzyString("Hey TREY!")
    
    print('>>> greeting')
    print(greeting)
    
    print('>>> print(greeting == "hey Trey!")')
    print(greeting == "hey Trey!")
    
    print('>>> greeting == "heyTrey"')
    print(greeting == "heyTrey")
    
    print('>>> o_word = FuzzyString("Octothorpe")')
    o_word = FuzzyString("Octothorpe")
    print(">>> 'hashtag' < o_word")
    print('hashtag' < o_word)
    
    print(">>> 'hashtag' > o_word")
    print('hashtag' > o_word)
    
    print(">>> 'OCTO' in o_word")
    print('OCTO' in o_word)
    
    print(">>> new_string = o_word + ' (aka hashtag)'")
    
    new_string = o_word + ' (aka hashtag)'
    
    print(">>> new_string == 'Octothorpe (AKA hashtag)'")
    print(new_string == 'Octothorpe (AKA hashtag)')
    ss = FuzzyString('ss')
    print(">>> '\u00df' == ss")
    print('\u00df' == ss)
    
    print(">>> e = FuzzyString('\u00e9')")
    e = FuzzyString('\u00e9')
    print(">>> '\u0065\u0301' == e")
    print('\u0065\u0301' == e)
    
    print(">>> '\u0301' in e")
    print('\u0301' in e)
