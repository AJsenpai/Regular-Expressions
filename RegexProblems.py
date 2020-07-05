# float numbers matcher
    import re
    for _ in range(int(input())):
        print(bool(re.match(r"^[+-]?\d*\.\d+$", input())))


# consecutive alphanumeric matcher
    import re
    mRegex = re.search(r"([a-zA-Z0-9])\1+", input())
    print(mRegex.group(1) if mRegex else - 1)

# match 2 or more vowels between the boundaries of consonant ex geeok
    import re
    # n = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
    m = re.findall(r"(?:[^aeiou]*)([aeiou]{2,})(?:[^aeiou])", input(), flags=re.I)
    print('\n'.join(m or ['-1']))

# match the pattern in a string 
    from re import compile
    data, pattern = input(), compile( input() )     # compile the regular expression pattern
    m = pattern.search(data)
    if not m : print( "(-1, -1)" )
    while m: 
        print( f"({m.start()}, {m.end()-1})" )
        m = pattern.search(data, m.start() + 1)

    # OR

    import re
    string, pattern = input(), input()
    m = list(re.finditer("(?=(%s))"%pattern,string))
    if not m:
        print((-1,-1))
    for i in m:
        print((i.start(1),i.end(1)-1))  




# You are given a text of  lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
    # && → and
    # || → or

    import re
    for i in range(int(input())):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group(1) == '&&' else 'or', input()))
        # positive look behind and look ahead assertions to look for spaces


# Match roman numerals from 1 - 3999 (both inclusive)
# not my solution
    import re
    regex_pattern = r"""
    M{0,3}                # thousands
    (C[MD]|D?C{0,3})      # hundreds
    (X[CL]|L?X{0,3})      # tens
    (I[VX]|V?I{0,3})$     # digit
    """
    print(str(bool(re.match(regex_pattern, input()))))

# email validator 
    import re
    for _ in range(int(input())):
        name, mail = input().split()
        emailRegex = re.match(r"^<[a-zA-Z](\w|\.|-|_)+@[a-zA-Z]+\.[a-zA-Z]{1,3}>$", mail)
        if emailRegex:
            print(name, mail)

# hexcolor code from css files
    import re
    for _ in range(int(input())):
    mo = re.findall(r"(#(?:[0-9a-fA-F]{3}){1,2})(?:,|;|\(|\))", input())
    if mo:
        print("\n".join(mo))

    # ^              anchor for start of string
    # #              the literal #
    # (              start of group
    #  ?:            indicate a non-capturing group that doesn't generate backreferences
    #  [0-9a-fA-F]   hexadecimal digit
    #  {3}           three times
    # )              end of group
    # {1,2}          repeat either once or twice
    # $


# match credit card numbers
    import re
    for _ in range(int(input())):
        s = input()
        cc = re.compile(r"^([456]\d{3})([\-]?)\d{4}\2\d{4}\2\d{4}$")
        if cc.search(s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
            print("Valid")
        else:
            print("Invalid")

####################################
#        w3resource.com            #
####################################

# 2. Write a Python program that matches a string that has an a followed by zero or more b's.  
    import re
    def aFollowedB(string):
        return bool(re.search(r"ab*?", string))

    print(aFollowedB("ac"))
    print(aFollowedB("abbbb"))
    print(aFollowedB("abbc"))
    print(aFollowedB("bb"))
    print(aFollowedB("*&%@#!}{"))

# 3. Write a Python program that matches a string that has an a followed by one or more b's
    import re
    def aFollowedB(string):
        return bool(re.search(r"ab+?", string))


# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.  
    import re
    def aFollowedB(string):
        return bool(re.search(r"ab?", string))

# 5. Write a Python program that matches a string that has an a followed by three 'b'.  
    import re
    def aFollowedB(string):
        return bool(re.search(r"ab{3}?", string))

# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
    import re
    def aFollowedB(string):
        return bool(re.search(r"ab{2,3}?", string))

# 7. Write a Python program to find sequences of lowercase letters joined with a underscore.
    import re
    def text_match(string):
        return bool(re.search(r"^[a-z]+_[a-z]+$", string))


# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters joined with underscores.
    import re

    def text_match(string):
        if not re.search(r"^[a-z]+_[a-z]+$", string):
            print("Match")
        else:
            print("Nope")

# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.  
    import re
    def text_match(string):
        return bool(re.search(r"^a.*?b$", string))

# 10. Write a Python program that matches a word at the beginning of a string.  
    import re
    def text_match(string):
        return bool(re.search(r"^\w+\b", string))

# 11. Write a Python program that matches a word at the end of string, with optional punctuation.  
    import re
    def text_match(string):
        return bool(re.search(r"\w+\S?$", string))

# 12. Write a Python program that matches a word containing 'z'.  
    import re
    def text_match(string):
        return bool(re.search(r"\w*z.\w*", string))

# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.  
    import re
    def text_match(string):
        return bool(re.search(r"\Bz\B", string))
 
# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.  
    import re
    def text_match(string):
        return bool(re.search(r"^[A-Za-z0-9_]*$", string))

# 15. Write a Python program where a string will start with a specific number.  
    import re
    def text_match(string):
            return bool(re.match(r"^5", string))

# 16. Write a Python program to remove leading zeros from an IP address.  
    def strip_zero(ip):
        pattern = re.compile(r"\.[0]")
        print(pattern.sub(r".", ip))

    strip_zero("216.08.094.196")

# 17. Write a Python program to check for a number at the end of a string.  
    def num_check(text):
        return bool(re.search('.*\d$', text))
    print(num_check('saddaf34'))

# 18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.   
    def num_search(text):
        temp = re.findall(r"([0-9]{1,3})(?:,|\s)", text)
        print("\n".join(temp))

    num_search("saddaf34, 456, 56578")
    num_search("Exercises number 1, 13, 12, and 345 are important")


# 19. Write a Python program to search some literals strings in a string.  
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
    def lit_search(find):
        text = "The quick brown fox jumps over the lazy dog."
        return bool(re.search(find, text))

    print(lit_search("fox"))
    print(lit_search("dog"))
    print(lit_search("world"))

# 20. Write a Python program to search a literals string in a string and also find the location within the original string 
#     where the pattern occurs.  
    def lit_search(find):
        text = "The quick brown fox jumps over the lazy dog."
        pattern = re.search(find, text)
        return pattern.span() if pattern else "Not found"

    print(lit_search("fox"))
    print(lit_search("dog"))
    print(lit_search("world"))


# 21. Write a Python program to find the substrings within a string.  

# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern :  'exercises'
# Note: There are two instances of exercises in the input string.
    def substr_search(find):
        text = "Python exercises, PHP exercises, C# exercises"
        return re.findall(find, text)

    print(substr_search("exercises"))
    print(substr_search("Python"))
    print(substr_search("world"))

 # 22. Write a Python program to find the occurrence and position of the substrings within a string.  
    def substr_search(find):
        text = "Python exercises, PHP exercises, C# exercises"
        for i in re.finditer(find, text):
            print(i.start(), i.end(), i.group())

    # Searched words : 'fox', 'dog', 'horse'
    print(substr_search("exercise"))
    print(substr_search("world"))

# 23. Write a Python program to replace whitespaces with an underscore and vice versa.  
    def remove(matchObj):
        return "_" if matchObj.group(1) == " " else " "
    print(re.sub(r"(\s|_)", remove, "hello world"))

# 24. Write a Python program to extract year, month and date from a an url.  
    def extract_date(url):
        pattern = re.compile(
            r"""
                ((\d{4})       # year
                [-/]
                (0?[1-9]|1[0-2])    # month
                [-/]
                (0?[1-9]|1[0-9]|2[0-9]|3[01]))   # date
                """,
            re.X,
        )
        print(pattern.search(url).group(0))

    url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
    extract_date(url)

# 25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.  
    def changeFormat(data):
        pattern = re.compile(
            r""" 
                    ((\d{4})       # year
                    [-/]
                    (0?[1-9]|1[0-2])    # month
                    [-/]
                    (0?[1-9]|1[0-9]|2[0-9]|3[01]))   # date
            
        """,
            re.X,
        )
        print(f"Original Date  : {data}")
        print("Formatted Date :", pattern.sub(r"\g<4>-\g<3>-\g<2>", data))

# 26. Write a Python program to match if two words from a list of words starting with letter 'P'.  
    def pTwice(data):
        for i in data:
            result = re.match(r"(P\w+)\s(P\w+)", i)
            if result:
                print(result.group(0))

    words = ["Python PHP", "Java JavaScript", "c c++"]
    pTwice(words)

# 27. Write a Python program to separate and print the numbers of a given string.  
    def extractNum(data):
        nums = re.findall(r"([0-9]{1,3}),?", data)
        print("\n".join(nums))

    data = "Ten 10, Twenty 20, Thirty 30"
    extractNum(data)

# 28. Write a Python program to find all words starting with 'a' or 'e' in a given string.  
    def extractNum(data):
        nums = re.findall(r"((?:a|e)\w+)", data, re.I)
        print("\n".join(nums))

    data = """The following example creates an ArrayList with a capacity of 50 elements. 
    Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."""
    extractNum(data)

# 29. Write a Python program to separate and print the numbers and their position of a given string.  
    def extractNum(data):
        for nums in re.finditer(r"\d{1,}", data):
            print(f"Number:{nums.group()}   Index:{nums.start()}")


    data = """The following example creates 2 ArrayList with a capacity of 50 elements. 
    Four elements are then added to the ArrayList of 90."""
    extractNum(data)

# 30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.  
    street = "21 Ramkrishna Road"
    print(re.sub(r"Road$", "Rd.", street))

# 31. Write a Python program to replace all occurrences of space, comma, or dot with a colon.  
    def replaceWithColon(data):
        print(re.sub(r"[\s,\.]", ":", data))

    data = "Python Exercises, PHP exercises."
    replaceWithColon(data)

# 32. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.  
    def replaceWithColon(data):
        print(re.sub(r"[\s,\.]", ":", data, count=2))

    data = "Python Exercises, PHP exercises."
    replaceWithColon(data)

# 33. Write a Python program to find all five characters long word in a string.  
    def find5(data):
        result = re.findall(r"\b\w{5}\b", data)
        print("\n".join(result))

    data = "The quick brown fox jumps over the lazy dog."
    find5(data)

# 34. Write a Python program to find all three, four, five characters long words in a string.  
    def find345(data):
        result = re.findall(r"\b\w{3,5}\b", data)
        print("\n".join(result))

    data = "The quick brown fox jumps over the lazy dog."
    find345(data)

# 35. Write a Python program to find all words which are at least 4 characters long in a string. 
    def find4OrMore(data):
        result = re.findall(r"\b\w{4,}\b", data)
        print("\n".join(result))


    data = "The quick brown fox jumps over the lazy dog."
    find345(data)

# 36. Write a python program to convert camel case string to snake case string.  
    def camelToSnake(data):
        print(re.sub(r"([a-z])([A-Z])", r"\g<1>_\g<2>", data).lower())


    camelToSnake("PythonExercisesTutorials")
    camelToSnake("ThisIsCamelCase")

# 37. Write a python program to convert snake case string to camel case string.  
    def snakeToCamel(data):
        return "".join(word.capitalize() for word in data.split("_"))

    print(snakeToCamel("python_exercises_tutorials"))
    print(snakeToCamel("this_is_camel_case"))


# 38. Write a Python program to extract values between quotation marks of a string.  
    text = '"Python", "PHP", "Java"'
    print(re.findall(r"\"(.+?)\"", text))

# 39. Write a Python program to remove multiple spaces in a string.  
    text = "Python      Exercises"
    print(re.sub(r"\s+", r" ", text))

# 40. Write a Python program to remove all whitespaces from a string.  
    text = "Python      Exercises"
    print(re.sub(r"\s+", r"", text))

# 41. Write a Python program to remove everything except alphanumeric characters from a string.  
    text = "**//Python Exercises// - 12. "
    print(re.sub(r"[\W_]", r"", text))

# 42. Write a Python program to find urls in a string.  
    text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
    text2 = """
    http://www.pythontutor.com/visualize.html#mode=edit
    https://www.w3resource.com/python-exercises/re/python-re-exercise-42.php
    https://www.google.com
    """
    pattern = re.compile(r"""
                        (
                        http[s]?://   # protocol
                        (?:[\w.\-]+)  # domain
                        (?:[\/\w\-.,@?=^%$#@\\+:;]*)?   # extra
                        )""", re.X,)
    print("\n".join(pattern.findall(text2)))


# 43. Write a Python program to split a string at uppercase letters.  
    text = "PythonTutorialAndExercises"
    print(" ".join(re.findall(r"([A-Z][^A-Z]+)", text)))
    
    # OR
    text = "PythonTutorialAndExercises"
    print(" ".join(re.split(r"([A-Z][^A-Z]+)", text)))

# 44. Write a Python program to do a case-insensitive string replacement.  
    text = "PHP Exercises"
    pattern = re.compile(re.escape("php"), re.I)
    print(pattern.sub("php", "PHP Exercises"))

# 45. Write a Python program to remove the ANSI escape sequences from a string.  
    import re
    text = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
    print(re.sub(r"\x1b[^m]*m", "", text))

# 46. Write a Python program to find all adverbs and their positions in a given sentence.  
# Sample text : "Clearly, he has no excuse for such behavior."
    text = "Clearly, he has no excuse for such behavior."
    print(re.findall(r"\w+ly", text))

# 47. Write a Python program to split a string with multiple delimiters.  
    text = "The quick brown\nfox jumps*over the lazy dog."
    print(re.split(r";|,|\*|\n", text))

# 48. Write a Python program to check a decimal with a precision of 2.  
    def checkPrecesion(num):
        return bool(re.match(r"[+-]?\d*(\.\d{1,2})?$", num))


    print(checkPrecesion("-45.34"))

# 49. Write a Python program to remove words from a string of length between 1 and a given number.  
    def removeWords(text):
        # max_range = input()
        pattern = re.compile(r"\b\w{1,4}\b")
        print(pattern.sub("", text))


    text = "The quick brown fox jumps over the lazy dog."
    removeWords(text)

# 50. Write a Python program to remove the parenthesis area in a string.  
# Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# Expected Output:
# example
# w3resource
# github
# stackoverflow
 
    def removeParanthesis(data):
        for i in data:
            print(re.sub(r" \([^)]+\)", "", i))

    removeParanthesis(["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"])

# 51. Write a Python program to insert spaces between words starting with capital letters. \
    add_spaces = lambda text: re.sub(r"([A-Z]\w*)([A-Z]\w*)", r"\g<1> \g<2> ", text)
    print(add_spaces("HelloWorld asdasf ASafd"))

# 52. Write a Python program that reads a given expression and evaluates it.  
# Terms and conditions:
# The expression consists of numerical values, operators and parentheses, and the ends with '='.
# The operators includes +, -, *, / where, represents, addition, subtraction, multiplication and division.
# When two operators have the same precedence, they are applied to left to right.
# You may assume that there is no division by zero.
# All calculation is performed as integers, and after the decimal point should be truncated Length of the expression will not exceed 100.
# -1 ? 10 9 = intermediate results of computation = 10 9
    while True:
        expression_raw = input()
        expression = re.sub(r"=", "", expression_raw)
        print(eval(expression))
        print("press ctrl+c to escape otherwise give an expression") 


# 53. Write a Python program to remove lowercase substrings from a given string.  
    # solution 1
    def rm_lower(text):
        pattern = re.compile(r"[a-z]")
        print(pattern.sub(r"", text))
    rm_lower("The quick brown fox jumps over the lazy dog")
    rm_lower("TasdadfSDFDewr")
    
    # solution 2
    remove_lower = lambda text: re.sub(r"[a-z]", "", text)
    print(remove_lower("ASsdfdfgZZZ"))

