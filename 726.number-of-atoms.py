#
# [726] Number of Atoms
#
# https://leetcode.com/problems/number-of-atoms
#
# algorithms
# Hard (44.89%)
# Total Accepted:    2.5K
# Total Submissions: 5.6K
# Testcase Example:  '"H2O"'
#
# Given a chemical formula (given as a string), return the count of each atom.
# 
# An atomic element always starts with an uppercase character, then zero or
# more lowercase letters, representing the name.
# 
# 1 or more digits representing the count of that element may follow if the
# count is greater than 1.  If the count is 1, no digits will follow.  For
# example, H2O and H2O2 are possible, but H1O2 is impossible.
# 
# Two formulas concatenated together produce another formula.  For example,
# H2O2He3Mg4 is also a formula.  
# 
# A formula placed in parentheses, and a count (optionally added) is also a
# formula.  For example, (H2O2) and (H2O2)3 are formulas.
# 
# Given a formula, output the count of all elements as a string in the
# following form: the first name (in sorted order), followed by its count (if
# that count is more than 1), followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.
# 
# Example 1:
# 
# Input: 
# formula = "H2O"
# Output: "H2O"
# Explanation: 
# The count of elements are {'H': 2, 'O': 1}.
# 
# 
# 
# Example 2:
# 
# Input: 
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: 
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# 
# 
# 
# Example 3:
# 
# Input: 
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: 
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# 
# 
# 
# Note:
# All atom names consist of lowercase letters, except for the first character
# which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses, and is a
# valid formula as defined in the problem.
# 
#
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        atom = num = ''
        stack = [collections.defaultdict(int)]
        for ch in formula[::-1]:
            if ch in '01234567890':
                num = ch + num
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                atom = ch + atom
            if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                atom = ch + atom
                stack[-1][atom] += int(num) if num else 1
                atom = num = ''
            if ch == ')':
                stack.append(int(num) if num else 1)
                stack.append(collections.defaultdict(int))
                atom = num = ''
            if ch == '(':
                atoms = stack.pop()
                prev_num = stack.pop()
                for k in atoms:
                    val = atoms[k]*prev_num
                    stack[-1][k] += val
                atom = num = ''
            #print(stack)
        ans = ''
        for k in sorted(stack[-1]):
            val = str(stack[-1][k]) if stack[-1][k]>1 else ''
            ans = ans + k + val
        return ans        
