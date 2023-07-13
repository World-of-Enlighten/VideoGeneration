
'''
This functions will round the number of hashtags,
by default r is 3 which is the max hashtags displayed for each click of View More button.
In TikTok Creative, by default it is displaying 3 hashtags, on click view more it displays 3 more
so if you want to display 20 hashtags, it should click on the view more button 6 times,
this function allow to find this number
'''
def roundToMultiple(n,r=3):
    if n%r:
        return n//r+r
    else:
        return n//r
    