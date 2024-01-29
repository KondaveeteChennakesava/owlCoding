<h2><a href="https://www.geeksforgeeks.org/problems/set-in-python-i/1?page=1&category=python&sortBy=submissions">Set in Python - I</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px"><strong>Congratulations</strong>...! You have arrived at the last module successfully. This module talks about <strong>Set </strong>in Python. A set is an <strong>unordered collection </strong>of items where every element is unique and must be <strong>immutable</strong>, but the set is <strong>mutable</strong>. You cannot access an element of the set using indexing or slicing, but you can update the set.</span></p>

<p><span style="font-size:18px">Some important functions in Set in Python:<br>
<strong>add</strong>(): Adds an element to the set.<br>
<strong>clear</strong>(): Removes all elements from the set<br>
<strong>discard</strong>(): Removes an element from the set if present.<br>
<strong>remove</strong>(): Removes an element from the set. If the element is not present, it raises an error.<br>
<strong>pop</strong>(): Removes and returns an arbitrary set element. Raise the error if the set is empty.<br>
<strong>union</strong>(): Returns the union of sets in a new set<br>
<strong>update</strong>(): Updates the set with the union of itself and others<br>
<strong>len</strong>(): Return the length of the set.<br>
<strong>sorted</strong>(): Return a new sorted list from elements in the set.<br>
<strong>sum</strong>(): Return the sum of all elements in the set.</span></p>

<p><span style="font-size:18px">Let's implement these methods through a question. Given Q queries to do some operation on Set, the task is to perform all the queries in the Set as given below:<br>
<strong>a. i element</strong>: Adds an element to the set.<br>
<strong>b.</strong> <strong>r element</strong>: Remove an element from the set.<br>
<strong>c.</strong> <strong>s</strong>: Find the sum of elements in the set. Returns the sum of elements in the set.</span></p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
Q = 4
S = {1, 2}
i 5
i 6
r 5
s
<strong>Output:</strong>
6</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">5 is added into the set
6 is added into the set
5 is removed from the set
So, now set is S = {1, 2, 6}
sum = 9</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong></span></p>

<p><span style="font-size:18px">Your task is to complete the functions <strong>insert()</strong>, <strong>remove_from_set()</strong> and <strong>sum_set()</strong> that performs the specified tasks.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= S[i] &lt;= 10<sup>4</sup></span></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python-set</code>&nbsp;<code>python</code>&nbsp;