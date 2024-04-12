//{ Driver Code Starts
// Initial Template for javascript

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split('\n').map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let N = parseInt(readLine());
        let Arr = readLine().split(' ').map(x => parseInt(x));
        let obj = new Solution();
        let res = obj.pairAndSum(N, Arr);
        console.log(res);
    }
}

// } Driver Code Ends


// User function Template for javascript
/**
 * @param {number} N
 * @param {number[]} Arr
 * @returns {number[]}
 */

class Solution {
    // Function to pair and sum the elements of the array.
    pairAndSum(n, arr) {
        // your code here
        let sum = 0;
        // const n = arr.length;
    
        for (let bit = 0; bit < 32; bit++) {
            let count = 0;
    
            for (let i = 0; i < n; i++) {
                if ((arr[i] & (1 << bit)) !== 0) {
                    count++;
                }
            }
    
            sum += count * (count - 1) / 2 * (1 << bit);
        }
    
        return sum;
    }
}