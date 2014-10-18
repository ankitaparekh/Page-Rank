from __future__ import division
import math
import sys


#function to calculate perplexity
############################################################################
def perpexity(PR):
	sum1 = 0
	per=0
	P = PR.values()
	for p in P:
		if p != 0:
			sum1 = sum1 + p*math.log(1/float(p),2)
	per = pow(2,sum1)
	return per
############################################################################



#decarling all the global variables
############################################################################
#dict for M(p) is the set (without duplicates) of pages that link to page p
M={}
# P is set of all pages
P=[]
# d is the PageRank Damping factor
d = 0.85
#S is set of sink nodes, i.e., pages that have no out links
S=[]
#dict for PageRank of each page
PR={}
#dict for L(q) is the number of out-links (without duplicates) from page q
L={}
#dict for unlinks. node as the value and list of nodes that point to that node
inlinks={}
############################################################################
		
def small_file(P,M,N,L,S,PR,iteration):

	newPR={}
	k = 0
	while k<iteration:
  		sinkPR = 0
  		for p in S:
			sinkPR += PR[p]
  		for p in P:
			newPR[p] = (1-d)/float(N)                 
			newPR[p] += d * sinkPR/float(N)
             
    			for q in M[p]:
				newPR[p] +=d * PR[q]/float(L[q])      
  		for p in P:
    			PR[p] = newPR[p]
  		k = k + 1
	print " \nPageRank for iterations" , iteration , " :" 
	print PR		


def big_file(P,M,N,L,S,PR):
	newPR={}
	old_perplexity = 0
	new_perplexity = 0
	k = 0
	i=0

	print " \nQuestion 2:\n "
	print " \nPerplexities:\n "

	#calculate the page rank
	############################################################################
	while k < 4:
		new_perplexity = perpexity(PR) 
  		change_perplexity = new_perplexity - old_perplexity
  		if change_perplexity < 1:
			k = k + 1
  		else:
			k = 0
	
  		old_perplexity = new_perplexity
  		print("Perplexity: " ,old_perplexity)

  		sinkPR = 0
  		for p in S:
			sinkPR += PR[p]
  		for p in P:
			newPR[p] = (1-d)/float(N)                 
			newPR[p] += d * sinkPR/float(N)
             
    			for q in M[p]:
				newPR[p] +=d * PR[q]/float(L[q])      
  		for p in P:
    			PR[p] = newPR[p]
  		i = i + 1
	print " Iterations:  " ,i
		

	#Sort the collection of web pages by the PageRank values you obtain and 
	#display top 50 pages with its document id.
	############################################################################
	print " \nQuestion 3:\n "
	print " \nTop 50 Pages sorted by PageRank values: \n "

	count_pr=0
	for p in sorted(PR, key=PR.get, reverse=True):
  		count_pr = count_pr + 1
  		if count_pr <= 50:
  			print p, " : " , PR[p]


	#Sort the collection of web pages by the inlinks and display top 50 pages
	#with its document id.
	############################################################################
	print " \nTop 50 Pages sorted by inlinks values: \n  "

	count_inlink=0

	for inlink in sorted(inlinks,key=inlinks.get,reverse=True):
  		count_inlink = count_inlink + 1
  		if count_inlink <= 50:
  			print inlink, " : " ,inlinks[inlink]

	

def main(arg):
	#open the file and read the file and initialize P , M and N	
	############################################################################
	file = open(arg, 'r')

	for line in file:
		inlink_pages=[]
		current_line = line.strip()
		info = current_line.split(" ")
		dest = info[0]
		#append this node to the set of pages
		P.append(dest)
		src_links = info[1:]
		for src in src_links:
			inlink_pages.append(src)
		if dest in M:
			inlinks_dest = []
			inlinks_dest = M.get(dest)
			M[dest] = a + list(set(inlink_pages) - set(inlinks_dest))
		else :
			M[dest]= inlink_pages

	file.close()
	N= len(P)

	############################################################################


	#initialize L
	############################################################################
	#add the number of out-links from page p in L
	for links in M.itervalues():
        	for link_node in links:
            		count = 1
            		if link_node in L:
                		count = L[link_node]
	                	count =count + 1
        		L[link_node] = count

	for key in M.iterkeys():
		val = M[key]
		inlinks[key]=len(val)
	############################################################################


	#initialize S
	############################################################################
	for p in P:
		if p not in L:
			S.append(p)
	############################################################################


	#initialization of page rank
	############################################################################
	initial_rank = 1/float(N)

	for p in P:
		#add initial_rank to the PR[p]
		PR[p]= initial_rank
	############################################################################
	file = open(arg, 'r')
	count_lines = len(file.readlines())
	file.close()

	if count_lines > 6:
		big_file(P,M,N,L,S,PR)
	else:
		print " \nQuestion 1:\n "
		# 1 iteration
		small_file(P,M,N,L,S,PR,1)
		# 10 iteration
		small_file(P,M,N,L,S, PR,10)
		# 100 iteration
		small_file(P,M,N,L,S, PR,100)
	



if(__name__=="__main__"):
    main(sys.argv[1])




