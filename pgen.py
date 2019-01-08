import itertools

def getp(upto:int,bottom:int=0):
    # prepare sieve and domain
    top = ((upto+1)//6)+1
    factop = int((top/6)**0.5)+2
    sel_p = bytearray([True]) * top
    sel_s = bytearray([True]) * top

    # sieve
    for x in range(1,factop):
        if sel_p[x-1]:
            m1 = 6*x+1
            sel_p[7*x::m1]=bytearray((top-x)//m1)
            sel_s[5*x::m1]=bytearray((top+x)//m1)

        if sel_s[x-1]:
            m2=6*x-1
            sel_p[5*x-2::m2]=bytearray( (top+x)//m2 )
            sel_s[7*x-2::m2]=bytearray( (top-x)//m2 )
    

    # prime list
    ## is it bottom bounded?
    if bottom:
        bot_lo = ( bottom-1)//6  +1
        bot_hi = (bottom+1)//6   +1
        out = []
    else:
        bot_hi = 1
        bot_lo = 1
        out = [2,3]
    
    out += itertools.compress(range(bot_hi*6 - 1,top*6-1,6),sel_s[bot_hi-1:])
    out += itertools.compress(range(bot_lo*6 + 1,top*6,6),sel_p[bot_lo-1:])
    out.sort()

    # WARNING: sometimes returns 1 prime over given bound.
    # try [30, 60, 600, 3000, 9000, 9*10**4,9*10**5]
    # For given values, the one over is always from sel_p
    # i.e. prime_over_bound = upto+1 
    # which is equivalent to: ( prime_over_bound - 1) is dividable by 6.
    # Two lines below make up a crude fix for this.
    while out[-1]>upto:
        out.pop()

    return out
