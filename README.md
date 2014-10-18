Page-Rank
=========

---------------------------------------------------
Implementation of Iterative Page Rank Algorithm
---------------------------------------------------

This code contains 3 parts:

1.Using the iterative version of PageRank algorithm,list the PageRank values you obtain for each of the six vertices after 1, 10, and 100 iterations of the PageRank algorithm.

2.Calculate and list the perplexity values obtained in each round until convergence (change in perplexity is less than 1 for at least four iterations)

3.Sort the collection of web pages by the PageRank values obtained by above algorithm and print top 50 documents with highest PageRank and top 50 documents with highest in-link count.


------------------------
How to run code:
------------------------

This program needs no special libraries.

To run the code:

1.for the file with 6 nodes:
$ python Page_Rank_Ankita.py input.txt > q1_result.txt

the results will be stored in q1_result.txt


2.for the large file:
$ python Page_Rank_Ankita.py wt2g_inlinks.txt > q23_result.txt

the results will be stored in q23_result.txt
