links_list = ["Zwick USA, L.P.","11022903 Canada Inc.","101199652 Saskatchewan Ltd","10884235 CANADA INC.","Wood Mackenzie Limited","101110516 Saskatchewan Ltd","10551554 CANADA INC.","10x Genomics, Inc","101209983 Saskatchewan Ltd",]

last_ran = "10x Genomics, Inc"

i = 0
l = len(links_list)
while i < l:
    if links_list[i] == last_ran:
        break
    i+=1
if i >= l:
    print("This link was not found in the list of links (links_list) or this is the last link and there's no need to continue the program")
else:
    print("Copy paste this index into line 40 instead of 0:", i)
