class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        emailToName = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for acc in accounts:
            name = acc[0]
            firstEmail = acc[1]

            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                emailToName[email] = name
                union(firstEmail, email)

        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        res = []
        for root, emails in groups.items():
            res.append([emailToName[root]] + sorted(emails))

        return res