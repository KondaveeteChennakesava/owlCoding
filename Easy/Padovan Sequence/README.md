<h2><a href="https://www.geeksforgeeks.org/problems/padovan-sequence2855/1?page=1&category=series&difficulty=Easy,Medium&sortBy=submissions">Padovan Sequence</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">A <strong>Padovan Sequence</strong>&nbsp;is a sequence&nbsp;which is represented by the following recurrence relation<br>
P(N) = P(N-2) + P(N-3)<br>
P(0) = P(1) = P(2) = 1<br>
Given a number N,&nbsp;find the N<sup>th</sup> number in this sequence.</span></p>

<p><span style="font-size:18px"><strong>Note:</strong>&nbsp;Since the output may&nbsp;be very large, compute the answer&nbsp;modulus 10^9+7.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 3
<strong>Output:</strong> 2
<strong>Explanation</strong>: P<sub>1</sub> + P<sub>0</sub> = P<sub>3<sub>
</sub></sub>P<sub>1 </sub>= 1 and P<sub>0</sub> = 1
</span></pre>

<p><br>
<span style="font-size:18px">â€‹<strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: 
N = 4
<strong>Output:</strong> 2
<strong>Explanation</strong>: P<sub>2</sub>&nbsp;+ P<sub>1</sub>&nbsp;= P<sub>4</sub>
<sub> </sub>P2 = 1 and P<sub>1</sub>&nbsp;= 1
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>padovanSequence()&nbsp;</strong>which takes&nbsp;integer N as input parameter and return N<sup>th</sup>&nbsp;number in Padovan Sequence.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N)<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N&nbsp;&lt;= 10<sup>6</sup></span></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>series</code>&nbsp;<code>Modular Arithmetic</code>&nbsp;<code>Algorithms</code>&nbsp;