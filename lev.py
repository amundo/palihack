def distance(a, b):
    """
    Computes the levenshtein distance between two strings
    """
    m, n = (len(a),a), (len(b),b)
    if(m[0] < n[0]):                #ensure that the 'm' tuple holds the longest string
        m, n = n, m
    dist = m[0]                     #assume distance = length of longest string (worst case)
    for i in range(0, n[0]):       # reduce the distance for each char match in shorter string
        if m[1][i] == n[1][i]:
            dist = dist - 1
    return dist 
