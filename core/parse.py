##
## parse argument
##
## written by @ciku370
##

def toxic(wibu_bau,bawang):
    shit = bawang.split(',')
    dan_buriq = 0
    result = {}
    for i in wibu_bau:
         if i in shit:
              try:
                   result.update({wibu_bau[dan_buriq]:wibu_bau[dan_buriq+1]})
              except IndexError:
                   continue
         dan_buriq += 1
    return result
