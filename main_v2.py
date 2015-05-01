import sys, math

# ****************   Main program  *********************************************
def main():
    #   File IO ###############################################
    txt = open("in9.txt", 'r')
    
    N = int (txt.readline())
    n = 2 * N       
    
    a = [[0 for x in range(1)] for y in range(n)] 
    
    # print >> sys.stderr, a
    print >> sys.stderr, "N=", N
     
    for line in range (0, N):
        x , y = [int(j) for j in txt.readline().split()]     
        #print >> sys.stderr, '%d %d' % (x, y)    
        m, n = sortTwo(x, y)
        
        a[m].append(n)
        a[n].append(m)
        a[m][0] += 1
        a[n][0] += 1
        
    print >> sys.stderr, "Done file IO \n \n"    
    ##############################################################
     
     
    # Init vars-------------------------------------------------
    #print >> sys.stderr, a
    
    while (a[-1]==[0]): # check for abundant [0]
        a.pop()    
    relationship = a
    
    n = len(relationship)
    
    print >> sys.stderr, "total nodes:" , n
    
    
    level = [0] * n  # contains level of nodes    
    # print >> sys.stderr, level    
    #print >> sys.stderr, "relationship: \n" , relationship
    
    countOne = 0
    oneList = []
    for elem in range(0, n):
        if (relationship[elem][0] == 1):
            countOne += 1
            oneList.append(elem)
    
         
    print >> sys.stderr, "countONe:", countOne
    # print >> sys.stderr,"oneList:", oneList
         
    print >> sys.stderr, "Done Var init \n \n"         
    # -------------------------------------------------------------
    
    # Engine ---------------------------------------------------
    
    for i in range(0, countOne):
        
        node = oneList[i]
        level[i] = findSingleMaxLength(node, node, oneList, countOne, relationship, n)
    
    # ------------------------------------------------------------
    
    
     
    # Report ------------------------------------------------- 
    
    
    
    #---------------------------------------------------------
     
    # No touch area ------------------------------------------
    maxi = max(level)
    if (maxi % 2 == 0):
        ans = maxi / 2
    else:
        ans = (maxi + 1) / 2
        
    print >> sys.stderr, "Answer:", ans 
     
    
#*********************** End program ************************************************










def spreadRumorNode(node, relationship, relationship_len):  # update relationship and provide bag    
    bag = []
    new_relationship = relationship
    
    if (new_relationship[node][0] > 0):
        for bag_elem in range (1, 1 + relationship[node][0]):
            node_child = relationship[node][bag_elem]
            
            if (relationship[node_child][0] > 0):
                bag.append(node_child)            
        
    new_relationship[node][0] = -2
    
    return bag, new_relationship
    



def spreadRumorOnce(target_list, relationship, relationship_len):
    new_target_list = []
    
    new_relationship = relationship
    
    number_of_target = len(target_list)
    
    target_bag = [[] for y in range(number_of_target)] 
        
    for i in range(number_of_target):
        node = target_list[i]
        target_bag[i], new_relationship = spreadRumorNode(node, new_relationship, relationship_len)
         
        new_target_list.extend(target_bag[i])

    return new_target_list, new_relationship


def findSingleMaxLength(x, x_pos, oneList, oneList_len, relationship, relationship_len):
    new_relationship = relationship    
    
    step = -1
    
    try:
        i = oneList.index(x)
    except ValueError:
        return -1  # no match
    
    nowhere_to_go = 0
    
    target_list = [x]
    
    
    while (nowhere_to_go == 0):
        step += 1
        target_list, new_relationship = spreadRumorOnce(target_list, new_relationship, relationship_len)
        if (target_list == []):
            nowhere_to_go = 1
    
    
    return step


def findMin(a, b):
    res = a
    if (res > b):
        res = b
    return res

def sortTwo(a, b):    
    if (a < b):
        x = a
        y = b
        
    else:
        x = b
        y = a
        
    return x, y        
        
main()        
