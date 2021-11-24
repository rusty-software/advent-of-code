expenses = [
    1509
    , 1857
    , 1736
    , 1815
    , 1576
    , 1970
    , 1567
    , 1778
    , 1508
    , 1833
    , 1377
    , 1890
    , 1375
    , 1396
    , 1102
    , 1639
    , 1818
    , 1469
    , 1138
    , 1333
    , 1906
    , 1557
    , 1686
    , 1712
    , 1990
    , 1930
    , 1761
    , 1881
    , 1551
    , 1627
    , 1801
    , 1728
    , 1960
    , 1407
    , 1832
    , 1842
    , 1393
    , 1870
    , 1295
    , 1528
    , 251
    , 1945
    , 1589
    , 1850
    , 1650
    , 1793
    , 1997
    , 1758
    , 1477
    , 1697
    , 1081
    , 1825
    , 1899
    , 1171
    , 1104
    , 1839
    , 1974
    , 1630
    , 1831
    , 1671
    , 1723
    , 1811
    , 1489
    , 1647
    , 1486
    , 1107
    , 1786
    , 1680
    , 1942
    , 1640
    , 1112
    , 1703
    , 1315
    , 1769
    , 1966
    , 997
    , 2010
    , 1635
    , 1196
    , 383
    , 1986
    , 1860
    , 1743
    , 1756
    , 1555
    , 1111
    , 1823
    , 48
    , 1953
    , 1083
    , 1804
    , 1933
    , 1626
    , 1895
    , 1807
    , 1669
    , 1783
    , 389
    , 1821
    , 1883
    , 1114
    , 1587
    , 1941
    , 1725
    , 1646
    , 456
    , 1550
    , 1939
    , 1975
    , 1324
    , 1201
    , 1018
    , 1001
    , 1402
    , 1885
    , 1481
    , 1633
    , 1781
    , 1622
    , 1822
    , 1559
    , 1696
    , 1510
    , 1251
    , 1732
    , 1790
    , 1813
    , 1695
    , 1121
    , 704
    , 1964
    , 1984
    , 1763
    , 1656
    , 1183
    , 1771
    , 1276
    , 1764
    , 1810
    , 1992
    , 1213
    , 1840
    , 1318
    , 1965
    , 1943
    , 1549
    , 1768
    , 1506
    , 1949
    , 1739
    , 1852
    , 1787
    , 1570
    , 1988
    , 1357
    , 1909
    , 1837
    , 561
    , 1994
    , 1777
    , 1547
    , 1925
    , 1897
    , 1817
    , 1677
    , 1668
    , 1982
    , 1667
    , 1753
    , 1041
    , 1826
    , 1961
    , 1797
    , 1765
    , 1720
    , 1835
    , 1688
    , 1705
    , 1744
    , 1977
    , 1971
    , 1775
    , 1782
    , 1661
    , 1385
    , 1162
    , 1755
    , 1846
    , 1674
    , 1698
    , 1882
    , 1766
    , 1820
    , 1531
    , 1577
    , 1710
    , 1382
    , 1246
    , 1864
    , 1702]


def find_pair_summing_to(expected_sum):
    """
    This one is a poor performer, but gets the job done.
    """
    for left in expenses:
        for right in expenses:
            if left + right == expected_sum:
                return left, right


def find_triple_summing_to(expected_sum):
    """
    Yikes, now we're talking an even faster road to processor ruination.
    """
    for left in expenses:
        for middle in expenses:
            for right in expenses:
                if left + middle + right == expected_sum:
                    return left, middle, right


def find_pair_improved(expected_sum):
    """
    Seems like this algorithm would scale linearly.

    Tanya told me about this one (she's gone through an algorithms course
    """
    diffs = {}
    for expense in expenses:
        diffs[expected_sum - expense] = expense

    for expense in expenses:
        if expense in diffs.keys():
            return expense, diffs[expense]


def find_triple_improved(expected_sum):
    """
    Sorting and two-pointer technique

    I looked this one up. Seems reasonable that it would be a better performer than the n^3.
    """
    # sort the array. ah, mutability
    expenses.sort()

    upperbound = len(expenses)
    # fix the first of the triple values and try to find the other two values
    for i in range(0, upperbound - 2):
        # start the pointers at opposite eligible ends of the array
        left = i + 1
        right = upperbound - 1

        while left < right:
            current_sum = expenses[i] + expenses[left] + expenses[right]
            if current_sum == expected_sum:
                return expenses[i], expenses[left], expenses[right]
            elif current_sum < expected_sum:
                # too small: move the left pointer
                left += 1
            else:
                # too large: move the right pointer
                right -= 1

    return None, None, None


def calc():
    [left, right] = find_pair_summing_to(2020)
    print('find_pair: {:d} * {:d} == {:d}'.format(left, right, left * right))
    [left, right] = find_pair_improved(2020)
    print('find_pair_improved: {:d} * {:d} == {:d}'.format(left, right, left * right))
    [left, middle, right] = find_triple_summing_to(2020)
    print('find_triple: {:d} * {:d} * {:d} == {:d}'.format(left, middle, right, left * middle * right))
    [left, middle, right] = find_triple_improved(2020)
    print('find_triple_improved: {:d} * {:d} * {:d} == {:d}'.format(left, middle, right, left * middle * right))


if __name__ == "__main__":
    calc()
