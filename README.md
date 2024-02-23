# Counting-Letters
The goal is to identify the most frequent letters in text files (literary works) using different methods, and to evaluate the quality of estimates regarding the exact counts. In order to accomplish that, develop and test three different approaches:

- Exact counters,
- Approximate counters,
- Lossy Counting algorithm.

An analysis of the computational efficiency and limitations of the developed approaches has to be carried out. For example, in terms of absolute and relative errors (lowest value, highest value, average value, etc.), average values, etc. It can also be verified whether the same most frequent letters are identified, and in the same relative order. And if the most frequent letters are similar in the text files of the same literary work in different languages.

For this you must:

1. Compute the exact number of occurrences of each letter.

2. Estimate the n most frequent letters, running your data stream algorithm for n = 3, n = 5, and n = 10.

3. Perform a set of tests, repeating the approximate counts a few times.

4. Compare the performance of the approximate counters and the data stream algorithm (for the different k values), between themselves and regarding the exact counts.
