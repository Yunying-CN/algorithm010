第二周学习笔记

这周学习的主要是哈希表、树和堆与图。
在哈希表里主要是通过记录过去已经遍历或者是计算过的数据在表里，在进行之后的计算时，不需要对以往的数据进行重新计算，只需要去读取哈希表中的值即可，这可减少递归的次数，减少空间复杂度，但由于生成了哈希表来记录数据，此时的空间复杂度会增加。
在题目有效的字母异位词中，通过用哈希表来记录遍历过的字符的个数，将两个字符串进行比对，即可实现O(n)的时间复杂度。
在题目两数之后中也是同理，记录遍历过字符串的数字，再进行查表，使得空间复杂度为O(n),时间复杂度也为O(n)。

在树里，主要分为前序，中序和后序，做题关键先要熟悉模版，熟悉三种之间如何转换。其中二叉树是特殊的树，每个根节点只有两个子节点。

在堆中，可以相对将其转化成为树状来进行分析和理解。
