### Task # 1:

---
***RU***:Сделать генератор геометрической прогрессии.

***EN***:Make a geometric progression generator.

---
## Result:
This program used:
- the _yield_ statement in a hidden class static method **__yield** to populate a list of progression elements.
- hidden static method **__sum** with a _recursion_ to find the sum of elements of a progression in a given range.
- empty input is equivalent to the default value = 1.
-     b(1) - start element of GP
      q - factor GP
      c - count of elements GP
      n - N element of GP to find
- the class method decorator is implemented, but it is compensated at the input stage, so always True.