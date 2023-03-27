import random

###################################################################
# Benford's law, also known as the Newcomb–Benford law,           #
# the law of anomalous numbers, or the first-digit law,           #
# is an observation that in many real-life sets of numerical data,#
# the leading digit is likely to be small.                        #
###################################################################

# print("hello")
# a=random.randint(0,3000)
# b=random.randint(0,3000)
# c=random.randint(0,3000)
# print(a,b,c)


##################################
#            Adjuster            #
##################################
sample_number = 9999999
##################################
#better donnot input over 9999999#
##################################


i=0
randomheads=[]
while i<sample_number:
    randomheads.append(str(random.randint(0,sample_number))[0])
    i+=1

for match in range(1,10):
    if match == 9:
        print(randomheads.count(str(match)))
    else:
        print(randomheads.count(str(match)), end=" ")
print("put results found above to the site in order to test benford's law\nhttps://www.rapidtables.com/tools/bar-graph.html")