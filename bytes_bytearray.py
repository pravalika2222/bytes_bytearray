'''bytes is immutable datatype , modification cannot be made'''
# a=bprint(a,type(a))    #  b'pravalika'  #  "bytes" type
# print(list(a))    # [112, 114, 97, 118, 97, 108, 105, 107, 97]  
# print(tuple(a))   # (112, 114, 97, 118, 97, 108, 105, 107, 97)
# print(set(a))     # {97, 105, 107, 108, 112, 114, 118} in sets we get in the assending order'pravalika'

# r=b'parrot'
# for h in r:
#     print(h)   #  112
#                #   97
#                #  114
#                #  114
#                #  111
#                #  116   the o/p may get in the vertical 

# p=b'rat'
# print(ord('t'))      #  116   ordinary(ord): it definds "alphabets" & output may get in the numbers 
# print(chr(114))      #   r    character(chr): it definds "integer values"  & output may get in the alphabets

# print(ord('['))    # '[' open bracket value is "91"
# print(ord(','))    # ',' comma value is  "44"
# print(ord(']'))    # ']' colsed bracket value is "93"

# a=b'[1,2,3]'
# print(list(a))     # [91 49 44 50 44 51]  "0" zero value starts from "48"


'''bytearray is a mutable datatype , modificaton can be made '''
# c=bytearray(b"world")
# # print(c,type(c))     #  bytearray(b'world)     # bytearray type
# print(c[1])    # 111 bcoz the index value of 'o' means 1 index
# c[1]=112
# print(c)      # modification can be made  so here we "o" replacing with the "ASCII" values "112" so we may get  bytearray(b'wprld')

