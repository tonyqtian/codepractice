# -*- encoding: utf-8 -*-

"""
@version: 0.01
@author: Tony Qiu
@contact: tony.qiu@liulishuo.com
@file: nodetest.py
@time: 2018/04/22 午前10:50
"""

from numpy.random import randint, seed

seed()


class node:
    def __init__(self, data, nextNode=None):
        self.val = data
        self.next = nextNode

    def nextNode(self):
        return self.next


def printNode(head, string=""):
    nodelist = []
    if not cycleCheck(head):
        while head:
            nodelist.append(str(head.val))
            head = head.nextNode()
    else:
        entryNode = findEntry(head)
        while head is not entryNode:
            nodelist.append(str(head.val))
            head = head.nextNode()
        nodelist.append(str(head.val))
        head = head.nextNode()
        while head is not entryNode:
            nodelist.append(str(head.val))
            head = head.nextNode()
        nodelist.append(str(head.val))
        head = head.nextNode()
        while head is not entryNode:
            nodelist.append(str(head.val))
            head = head.nextNode()
        nodelist.append(str(head.val))
    print(string + ' -> '.join(nodelist))


def delNode(node):
    if node is None:
        return None
    if node.nextNode() is None:
        print("Not work on the last element")
        return None

    tmp = node.nextNode()
    node.val = node.nextNode().val
    node.next = node.nextNode().nextNode()
    del tmp
    return node


def reverseNode(head):
    assert head is not None
    if head.nextNode() is None:
        return head

    pre = head
    cur = head.nextNode()

    pre.next = None
    while cur.nextNode():
        tmp = cur.nextNode()
        cur.next = pre
        pre = cur
        cur = tmp

    cur.next = pre
    return cur


def reverseRecursively(head):
    if head is None:
        return None
    if head.next is None:
        return head
    
    newhead = reverseRecursively(head.next)
    
    head.next.next = head
    head.next = None

    return newhead


def delbacknRecursive(head, n):
    assert head is not None
    if head.nextNode() is None:
        return 1

    backcount = delbacknRecursive(head.nextNode(), n) + 1
    if backcount == n:
        delNode(head)

    return backcount


def delbackn(head, n):
    assert head is not None
    nstart = head
    nend = head
    for _ in range(n-1):
        if nend:
            nend = nend.nextNode()
        else:
            return None
    if not nend:
        return None

    while nend.nextNode():
        nstart = nstart.nextNode()
        nend = nend.nextNode()

    delNode(nstart)
    return head


def getMiddle(head):
    assert head is not None
    if not head.nextNode():
        return head
    if not head.nextNode().nextNode():
        return head

    fast = head
    slow = head
    while fast.nextNode():
        fast = fast.nextNode()
        slow = slow.nextNode()
        if fast:
            fast = fast.nextNode()
            if not fast:
                break
        else:
            break

    return slow


def cycleCheck(head):
    assert head is not None
    fast = head
    slow = head

    while fast.nextNode():
        fast = fast.nextNode()
        slow = slow.nextNode()
        if fast:
            fast = fast.nextNode()
            if not fast:
                return False
        else:
            return False

        if fast is slow:
            return True

    return False


def pMove(step, move, entry, length):
    cycle = length - entry + 1
    base = step * move + 1
    if base < (length + 1):
        return base
    else:
        base = base % (length + 1)
        if base < cycle:
            return base + entry
        else:
            return (base % cycle) + entry


def fastSlowCheck(entry, length):
    fast_path = []
    slow_path = []
    tik = 0
    fast = pMove(tik, 2, entry, length)
    slow = pMove(tik, 1, entry, length)
    fast_path.append("%2d" % fast)
    slow_path.append("%2d" % slow)
    tik += 1
    while True:
        fast = pMove(tik, 2, entry, length)
        slow = pMove(tik, 1, entry, length)
        fast_path.append("%2d" % fast)
        slow_path.append("%2d" % slow)
        if fast == slow:
            break
        # elif tik > 30:
        #     break
        else:
            tik += 1

    print(' '.join(["%2d" % idx for idx in range(tik+1)]))
    print(' '.join(fast_path))
    print(' '.join(slow_path))


def findEntry(head):
    if cycleCheck(head):
        fast = head
        slow = head

        while fast.nextNode():
            fast = fast.nextNode()
            slow = slow.nextNode()
            if fast:
                fast = fast.nextNode()
                if not fast:
                    return False
            else:
                return False

            if fast is slow:
                fast = head
                while not fast is slow:
                    fast = fast.nextNode()
                    slow = slow.nextNode()
                return fast

    else:
        print("No cycle in this link table...")
        return node("NULL")


def findCross(a, b):
    if (not cycleCheck(a)) and (not cycleCheck(b)):
        while a.nextNode():
            a = a.nextNode()
        while b.nextNode():
            b = b.nextNode()
        if a is b:
            return True
        else:
            return False
    elif cycleCheck(a) and (not cycleCheck(b)):
        return False
    elif (not cycleCheck(a)) and cycleCheck(b):
        return False
    else:
        # intersection is out of the loop, they must share the entry node
        entryA = findEntry(a)
        entryB = findEntry(b)
        if entryB is entryA:
            return True
        # intersection is on the loop,
        # the pointer on these two link tables will eventually meet on one arbitrary node on the loop
        b = entryB.nextNode()
        while b is not entryB:
            if b is entryA:
                return True
            b = b.nextNode()
        return False


def findPointer(headA, headB):
    if headA is None:
        return node("NULL")
    if headB is None:
        return node("NULL")

    if (not cycleCheck(headA)) and (not cycleCheck(headB)):
        tmpa = headA
        tmpb = headB
        while tmpa.next and tmpb.next:
            tmpa = tmpa.next
            tmpb = tmpb.next
        if tmpa.next:
            newtmpa = headA
            while tmpa.next and newtmpa.next:
                tmpa = tmpa.next
                newtmpa = newtmpa.next
            tmpa = newtmpa
            tmpb = headB
        elif tmpb.next:
            newtmpb = headB
            while tmpb.next and newtmpb.next:
                tmpb = tmpb.next
                newtmpb = newtmpb.next
            tmpa = headA
            tmpb = newtmpb
        else:
            tmpa = headA
            tmpb = headB
        while tmpa is not tmpb:
            tmpa = tmpa.next
            tmpb = tmpb.next
        return tmpa
    else:
        print("Not implemented")
        return node("NULL")


# for i in range(1, 21):
#     for j in range(1, i+1):
#         print("")
#         print("Entry %d  Length %d" % (j, i))
#         fastSlowCheck(j, i)

# for tlen in [1, 2, 3, 5, 10, 14, 21]:
#     tmp = node(randint(100))
#     for _ in range(tlen - 1):
#         tmp1 = node(randint(100), tmp)
#         tmp = tmp1
#     printNode(tmp)

    # tmp1 = delNode(tmp.nextNode())
    # printNode(tmp, string="del2 ")

    # tmp = reverseNode(tmp)
    # printNode(tmp, string="Reverse ")
    # tmp = reverseRecursively(tmp)
    # printNode(tmp, string="ReverseRec ")

    # delbacknRecursive(tmp, 3)
    # printNode(tmp, string="delback3rec ")

    # delbackn(tmp, 3)
    # printNode(tmp, string="delback3 ")

    # mdl = getMiddle(tmp)
    # printNode(mdl, string="Middle ")

    # print(cycleCheck(tmp))

# for tlen in [1, 2, 3, 5, 10, 14, 21]:
#     tmp = node(randint(100))
#     tail = tmp
#     entry = randint(1, tlen + 1)
#     if entry == 1:
#         entryNode = tail
#     for idx in range(2, tlen + 1):
#         tmp1 = node(randint(100), tmp)
#         tmp = tmp1
#         if idx == entry:
#             entryNode = tmp
#     tail.next = entryNode
#
#     print("")
#     print("Length %d  Entry %d" % (tlen, tlen - entry + 1))
#     printNode(tmp)
#     print(cycleCheck(tmp))
#     print(findEntry(tmp).val)


for tlen in [1, 2, 3, 5, 10, 14, 21]:
    tmp = node(randint(100))
    tail = tmp
    entry = randint(1, tlen + 1)
    entry2 = randint(1, tlen + 1)
    if entry == 1:
        entryNode = tail
    if entry2 == 1:
        entryNodeB = tail
    for idx in range(2, tlen + 1):
        tmp1 = node(randint(100), tmp)
        tmp = tmp1
        if idx == entry:
            entryNode = tmp
        if idx == entry2:
            entryNodeB = tmp
    # tail.next = entryNode

    tmp2 = node(randint(100), entryNodeB)
    for idx in range(2, tlen // 2 + 1):
        tmp1 = node(randint(100), tmp2)
        tmp2 = tmp1

    print("")
    print("Length %d  EntryA -%d EntryB -%d" % (tlen, entry, entry2))
    printNode(tmp)
    # print(findEntry(tmp).val)
    printNode(tmp2)
    # print(findEntry(tmp2).val)

    # print(findCross(tmp, tmp2))
    print(findPointer(tmp, tmp2).val)