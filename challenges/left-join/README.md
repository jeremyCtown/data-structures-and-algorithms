# Challenge: Left Join

You put your left foot in, you pull your left foot out, and swing it all about...

It's the Hokey-Pokey!

# Description

Use LEFT JOIN to combine two hash tables and create records to words that include antonyms and synonyms, return a single data structure.

# Requirements

- Read all of the following instructions carefully. Name things exactly as described, or you will get a ZERO without comment
- Do all your work in a public repository called data-structures-and-algorithms, with a well-formated, detailed top level README.md matching the example provided by your instructor
- Create a branch in your repository called left_join

On your branch, create…
- Python: a file called left_join.py
- Include any language-specific configuration files required for this challenge to become an individual component, module, library, etc.

Feature Tasks
- Write a function that LEFT JOINs two hashmaps into a single data structure.
- The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
- The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- NOTE: LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
- The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
- Avoid utilizing any of the library methods available to your language.

Structure and Testing
- Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

- Write at least three test assertions for each method that you define.

- Ensure your tests are passing before you submit your solution.

## Solution-ish

![](../../assets/33-left-join.jpg