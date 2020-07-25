'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th_len = len("th")
    # TBC
    #test case #1:
    th_str = "th"
    th_len = len("th")
    if len(word) == 0:#base case
        return 0
    else: #recursive case
        #check to see if first two letters are t and h; "th"
        if word[0:th_len] == th_str:
            #if so return rest of string without the first letter to
            # check for first two letters again and see if they are "th"
            return count_th(word[th_len - 1:]) + 1
        else:
            #return rest of string to repeat process of checking
            # to see if first two letters are "th"
            return count_th(word[th_len - 1:])
        
    

        
        

    #return "word"
    #return word


#len(word)
