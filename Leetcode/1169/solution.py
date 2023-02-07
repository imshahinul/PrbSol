class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        out = []

        for i, x in enumerate(transactions):
            name1, time1, amount1, city1 = x.split(',')
            if int(amount1) > 1000:
                out.append(x)
                continue
            for j, y in enumerate(transactions):
                if i != j:
                    name2, time2, amount2, city2 = y.split(',')
                    if name1 == name2 and city1 != city2 and abs(int(time1) - int(time2)) <= 60:
                        out.append(x)
                        break

        return out