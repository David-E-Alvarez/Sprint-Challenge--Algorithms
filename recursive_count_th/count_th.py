'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th_len = len("th")
    # TBC
    #test case #1:
    if len(word) == 0:#base case
        return 0
    #else: #recursive case
        #if "th" add 1

        
        

    #return "word"
    return word

word = "abcthxyz"
print(f"count_th(cat): ", count_th(word))
#len(word)
