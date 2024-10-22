""" 
""""""
In this code, we use a recursive backtracking approach. The function
 bkt1 is a recursive helper function that explores different combinations of coins to reach the target sum. 
The base case is when sum becomes 0, which means a valid modality is found and is added to the money list.

Now, let's analyze the time complexity:



The main work is done in the bkt1 function. In the worst case, the recursive calls explore
 all possible combinations of coins. Each recursive call considers a subset of the coins, and for each coin, it can either be included or not. 
 This leads to a binary tree-like exploration of the search space.

At each level of the recursion, you iterate through the coins array, so there are 'n' possibilities to consider.
The depth of the recursion is bounded by the sum 's'.
Considering the worst-case scenario where you explore all possible combinations, the time complexity is exponential, O(2^n), 
where 'n' is the number of coins. 

The space complexity is determined by the recursion stack and can also be exponential in the worst case. Each recursive call creates 
a copy of the vect list, and in the worst case, there can be 2^n such copies on the stack.
"""
def generate(coins, s):
    def bkt1(step, sum, vect):
        if sum == 0:
            # If we've reached the target sum, add the current combination to the results.
            money.append(vect.copy())  # Use copy() to create a copy of the list
            return
        for i in range(step, len(coins)):
            coin = coins[i]
            if coin <= sum:
                vect.append(coin)
                bkt1(i, sum - coin, vect)
                vect.pop()

    money = []

    bkt1(0, s, [])
    return money

#main content
coins = [1, 2, 5]
sum = 10
moneyfinal = generate(coins, sum)

if moneyfinal:
    print("Payment modalities")
    for x in moneyfinal:
        print(x)
else:
    print("There aren't modalities for payment")
