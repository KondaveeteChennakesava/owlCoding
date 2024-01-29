<h2><a href="https://www.geeksforgeeks.org/problems/dictionary-in-python-ii/1?page=1&category=python&sortBy=submissions">Dictionary in Python - II</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are now familiar with the dictionary in Python. It's time to dive deeper into the dictionary in Python. How can you use a dictionary&nbsp;to store the frequency of elements in list L. Given below is one method:</span></p>

<pre><span style="font-size:18px">for i in L:
     dict[i] = 0</span>

<span style="font-size:18px">for i in L:
     dict[i] += 1</span></pre>

<p><span style="font-size:18px">Now, use this concept to solve a question. Given a list <strong>arr</strong>, of <strong>N </strong>positive integers, and a <strong>sum</strong>. The task is to check if any pair exists in the array whose sum is present in the array.</span></p>

<p><span style="font-size:18px"><strong>Example:</strong></span><span style="font-size:18px"><strong> </strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> </span>
<span style="font-size:18px">N = 7 </span>
<span style="font-size:18px">sum = 8 </span>
<span style="font-size:18px">arr = [1, 2, 3, 3, 5, 5, 5]</span> 
<span style="font-size:18px"><strong>Output:</strong> </span>
<span style="font-size:18px">Yes</span>
<span style="font-size:18px"><strong>Explanation:</strong>
Pair with sum 8 is present in
the array which is (5, 3).</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Your&nbsp;task is to complete the function <strong>pair_sum()</strong> which returns True if the required pair is present, else return False.&nbsp;driver code will take care of the printing.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N, sum&nbsp;&lt;= 10<sup>4</sup><br>
1 &lt;= arr[i] &lt;= 10<sup>4</sup></span></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python-dict</code>&nbsp;<code>python</code>&nbsp;