# **Regular Expression Notes**

### 1. Modes of Regular Expression
  - **Standard:** /re/
  - **Global:** /re/g
  - **Case-insensitive:** /re/i
  - **Multi-line:** /re/m
  - **Dot-matches-all:** /re/s

### 2. Literal Characters
  literal characters that we are looking in the text for ex: cow , car one more thing to keep in mind that regex search is case sensitive by default . 
  so, cow and Cow are two different texts.

### 3. META Characters
    
    \ . \* + - {} [] ^ $ | ? () : ! = 

**# Wildcard Metacharacter**

| symbol | meaning |
|--- | --- |
| **.** (dot) | Any character except new line |


Ex: h.t will match hat, hot, hit but it will not match heat

Note: /h/nt/ will be a match if we use the mode &quot;dot-matches-all&quot; this will match everything include the new line character

**# Escaping Metacharacters**

| symbol | meaning |
|--- | --- |
| \ | Escape the next character |



- this will allow use of meta-characters as literal characters.

Ex: match a period with /9\.00/ So, this will match only 9.00 not 9500

- literal characters should never be escaped, it gives them a meaning ex: \w
- quotation marks are not meta characters, do not need to be escaped

**# Other special characters**

- Spaces : for spaces you just need to literally put spaces in your search text
- Tabs: (\t)
- Line Returns: (\r, \n, \r\n) note: \r- line return , \n- new line
- None Printable Characters: bell(\a), escape(\e), form feed(\f), vertical tab(\v)
- There is also ASCII and ANSI code that control terminal appearance of text terminal , but they&#39;re not used very often

**# Defining a character set**

| symbol | meaning |
|--- | --- |
| [ | Beginning a character set |
| ] | End a character set |


- It will march any of the several characters inside the [], but only one character. Order of the character doesn&#39;t matter
- Ex h[aeiou]t hot heavy piece of hammer . it will match any one character from character set that is present between literal character h and t

###  4. POXIS Bracket Expression

| **Class** | **Meaning** | **Equivalent** |
| --- | --- | --- |
| [:alpha:] | Alphabetic characters | A-Za-z |
| [:digit:] | Numeric Characters | 0-9 |
| [:alnum:] | Alphanumeric characters | A-Z-a-z0-9 |
| [:lower:] | Lowercase alphabets | a-z |
| [:upper:] | Uppercase alphabets | A-Z |
| [:punct:] | Punctuations characters |   |
| [:space:] | Space characters | \s |
| [:blank:] | Blank Characters (space, tab) |   |
| [:print:] | Printable characters, spaces |    |
| [:graph:] | Printable characters, no spaces |   |
| [:cntrl:] | Control characters (non printable) |    |
| [:xdigit:] | Hexadecimal characters | A-Fa-f0-9 |

- Correct: [[:alpha:] ] , [^[:alpha:] ]
- Incorrect: [:alpha:]
- Doesn&#39;t Support: java, javascript, python, .NET
- Support: PHP, Perl, UNIX, Ruby

### 5. Repetition Metacharacters

| symbol | meaning |
|--- | --- |
| * | Preceding item **zero or more** times |
| + | Preceding item **one or more** times  |
| ? | Preceding item **zero or one** times  |


### 6. Quantified Repetition

| symbol | meaning |
|--- | --- |
| { | Start quantified repetition of preceding item |
| } | End quantified repetition of preceding item |


- {min, max}
- Min and Max are positive numbers
- Min must always be included ; it can be zero
- Max is optional
- Ex: \d{4,8} , \d{4} here min is also max, \d{4,} here max is infinite

### 7. Greedy Expression

- 01\_FY\_07\_report\_99.xls
- /\d+\w+\d+/ this will match the entire filename instead of just before report
- Standard repetition quantifiers are greedy , Expression will try to match longest possible string

### 8. Lazy Expression

- We can make our regular expression less greedy by using lazy expression
- \*?
- +?
- {min, max}?
- ??
- apples??

**# Efficiency when using Repetition**

- Efficient matching + less backtracking = speedy result
- Define the quantity of repeated expression
  - /.+/ is faster than /.\*/
  - /.{5} and /.{3, 7}/ are even faster
- Narrow the scope of repeated expression
  - /.+/ can become /[A-Za-z]+/
- Provide clear starting and ending points
  - /\&lt;.+\&gt; can become /[^\&gt;]/ (in case of html tags)
  - Use anchors and word boundaries

### 9. Grouping Meta Characters

| symbol | meaning |
|--- | --- |
| ( | Start grouped expression |
| ) | End grouped expression |



- Group portion of expression
  - Apply repetition operators to a group
  - Makes expression easier to read
  - Captures group for use in matching and replacing
  - Ex: /(in)?dependent/ matches &quot;independent&quot; and &quot;dependent&quot;

### 10. Alteration Meta Character

| symbol | meaning |
|--- | --- |
|  \|  | Matches previous or next expression |

- I (Pipe) is OR operator
  - Either match expression on the left or on the right or both
  - Ordered, leftmost expression gets precedence
  - Multiple choices can be daisy chained
  - Group alternation expression to keep them distinct
- Example:
  - /apple|orange/ matches &quot;apple&quot; and &quot;oranges&quot;
  - /abc/def/ghi/jkl/ matches &quot;abc&quot; , &quot;def&quot;, &quot;ghi&quot; and &quot;jkl&quot;
  - /apple(sauce|juice)/

**# Writing logical and efficient Alteration**

- Penut|penutbutter it&#39;ll return penut instead of penut butter because it&#39;s eager to return result, if you want to return penut butter we can use penut(butter)? Because it&#39;s greedy
- Alteration will not scan the whole thing and it&#39;ll return the first result that it can find . for example, xyz|abc|def|ghi|xyz this expression will return abc from the string abcdefghijkl….xyz because it&#39;s eager to written the result . (global is turned off),

Regression backtracking

- Put most efficient expression first
  - /\w+\_\d{2, 4}|\d{4}\_\d{2}\_\w+|export\d{2}/ ( **incorrect** )
  - /export\d{2} |\d{4}\_\d{2}\_\w+|\w+\_\d{2, 4}/ ( **Efficient** )
- **Repeating**
  - First matched alteration does not affect the rest matches
  - /(AA|BB|CC){6}/ matches &quot;AABBAACCAABB&quot;

### 11. Start and End Anchors

| symbol | meaning |
|--- | --- |
| ^ | Start of a string/line |
| $ | End of a string/line |
| \A | Start of a string, never end of a line |
| \Z | End of a string, never end of a line |


- Reference of a position, not an actual character
- Ex: /^apple/ will written the string which contains apple only at thebeginning matches &quot;applesauce&quot;
- /apple$/ will return the string which contains apple at the end of the line will not match &quot;applepie&quot;
- /^apple$/ if apple is not the begning or the end then you don&#39;t have a match will not match
- \A and \Z are supported in java, python , PHP, Perl, Ruby, .NET
- Trailing whitespace or tab ^[\t] or leading white spaces or tab [\t]$

**# Line breaks and Multiline mode**

- **Single line mode**
  - ^ and $ don&#39;t match at line breaks
  - \A and \Z also don&#39;t match at the line breaks
- **Multiline mode**
  - ^ and $ will match at the start and the end of the line
  - \A and \Z do not match at line breaks
- **Multiline mode for python**
  - search(&quot;^regex$&quot;, string, re.MULTILINE)

### 12. Word Boundaries

| symbol | meaning |
|--- | --- |
| \b | Word boundary(start and end of word) |
| \B | Not a word boundary |


- **Condition for matching**
  - Before the first word character in the string
  - After the last word character in the string
  - Between a word character and a non-word character
  - Boundary example :
  - \b\w+\b find four matches in &quot;This is a test.&quot;
- **Caution**
  - A space is not a word boundary
  - Word boundaries references a position not an actual character (zero length)

### 13. Back References

- Grouped expressions are captured .
  - Stores the match portion in parentheses
    - /a(p{2}l)e/ matches &quot;apple&quot; and stores &quot;ppl&quot;
    - Regex stored the matched data of group, not the expression and it happens automatically, by default
- Backreference allow access to captured data
  - Refer to first backreference with \1

| symbol | meaning |
|--- | --- |
| \1 through \9 | Backreference from position 1 to 9 |


- **Usage**
  - Can be used in the same expression as the group
  - Can be accessed after the match is complete (Programming language)
  - Cannot be used inside character class

- **Examples**
  - /(apples) to \1 / matches &quot;apples to apples&quot;
  - / (ab) (cd) (ef) /3 /2 /1 / matches &quot;abcdefefcdab&quot;
  - /\&lt;(i|em)\&gt;.+?\&lt;/\1\&gt;/ matches &quot;\&lt;i\&gt; Hello\&lt;/i\&gt; &quot; and &quot;\&lt;em\&gt;Hello\&lt;/em\&gt;&quot;
    - Does not match \&lt;i\&gt;Hello\&lt;/em\&gt;
  - Duplicate words in document: \b(\w+)\s+ \1\b

**# Backreferences to optional Expression**

- Element is optional, group/capture is not optional
  - /(A?)B/ matches &quot;B&quot; and captures &quot;&quot;
- Element is not optional, group/capture is optional
  - /(A)?B/ matches B and does not capture anything

### 14. Find and Replace using Backreference

- Create a regex that captures the target data
- Test regex, use anchors and specificity to narrow the scope
- Add capturing groups, capture anything that varies row-to-row
- Use all captures and add back anything that is not captures but still needed like space or coma
- replace using \1 or $1 depending on the text editor or language

**# Non-Capturing Group Expression**

| symbol | meaning |
|--- | --- |
| ?: | Specify a non-capturing group |



- Syntax:
  - /(\w+)/ becomes /(?:\w+)/
- Why turn of capture and backreference?
  - Optimize speed
  - Preserve space for more captures (remember we only have 9 from \1 to \9)
- Example:
  - (?: oranges) and (apples) to \1
  - Will match oranges and apples to apples . because we turned off the capturing for oranges so the \1 spot is taken by apples
- /(?: regex)/
  - ? = &quot;Give this group a different meaning &quot;
  - : = &quot;the meaning is non capturing group&quot;

### 15. Positive Look Ahead Assertions

| symbol | meaning |
|--- | --- |
| ?= | Positive lookahead assertion |

- Assertions about what ought to be ahead
  - If lookahead expressions fails, the match fails
  - Any valid regular expression can be used
  - Zero width, doesn&#39;t include group in the match
- Syntax: /(?=regex)/ don&#39;t give spaces between regex and =
- Examples:
  - /(?=seashore)sea/ matches &quot;sea&quot; in &quot;seashore&quot; but not &quot;seaside&quot;
    - Same as /sea(?=shore)/
  - In other words, don&#39;t match shore just see if it is there . we&#39;re not making it a part of our match.
  - First it will assert and check If seashore is there (zero width) then if the assert is there it will start matching in our case sea
- So, the order is very important to make our regex optimize
- So, with look ahead assertion we have ability to run multiple regex at the same time for example: check for password which has one digit in it and also one capital letter
- /^.{8,15}$/ so here we&#39;ll make sure that our password can have anything in it and it is 8-15 characters long
- /^(?=.\*\d).{8,15}$/ now we are using look ahead assertion to check if it has zero or more digit
- /^(?=.\*\d)(?=.\*[A-Z]).{8,15}$/ and here we are checking if it has zero or more uppercase letter
- Now this regex will first run for assertion if it found the match then only it will search and match for actual regex

### 16a. Negative Look Ahead Assertions

| symbol | meaning |
|--- | --- |
| ?! | Negative lookahead assertion |



- Opposite of positive look ahead assertion
- /(?!seashore)sea/ matches &quot;sea&quot; in &quot;seaside&quot; but not &quot;seashore&quot;
- Example:
  - /online(?! training)/ matches &quot;online courses&quot; but doesn&#39;t match online training
  - /online(?! .\*training)/ matches &quot;online courses&quot; but doesn&#39;t match

Online video training

  - (\bword\b)(?!.\*\1) matches only last occurrence of word

### 16b. Look Behind Assertions

| symbol | meaning |
|--- | --- |
| ?\&lt;= | Positive look behind assertion |
| ?\&lt;! | Negative look behind assertion |


- /(?\&lt;=base)ball/ matches &quot;ball&quot; in &quot;baseball&quot; but not &quot;football&quot; same as /ball(?\&lt;=baseball)
- /(?\&lt;!base)ball/ matches &quot;ball&quot; in &quot;football&quot; but not &quot;baseball&quot;

### 17. Unicode in Regular Expression

- \u followed by a four-digit hexadecimal number (0000-FFFF)
- /caf\u00E9/ matches &quot;café&quot; but not &quot;café&quot;

### **Useful Regular Expressions**

#### 1. Matching Names

^([A-Z][A-Za-z.&#39;\-]+) (?:[A-Z][A-Za-z.&#39;\-]+) )? ([A-Z][A-Za-z.&#39;\-]+) $

#### 2. Matching postal codes

- **US:** ^\d{5}-(?:\d{4})$
- **Canada:** ^[A-Z]\d[A-Z] \d[A-Z]\d$
- **UK:** ^([A-Z]{1,2}\d{1,2}|[A-Z]{1,2}\d[A-Z]) \d[A-Z]{2}$

#### 3. Matching Email Addresses

^[\w.%+\-]+@[\w.\-]+\.[A-Za-z]{2,6}$


Page: 6
