zappos-challenge
================

My solution to the Zappos [coding challenge](http://doll-view.zappos.biz/coding-challenge/) presented at UNLV

It essentially creates a tree by enumerating all possible next states based on current state and specified valid moves. A state is defined as a list of buckets and their respective volumes. A hashmap of states is updated at every visit to ensure a single state is only visited once.

The solution is found by traversing the tree in A* fashion. The heuristic is calculated by finding the difference between the desired volume and current volume of each bucket and summing these differences together.
