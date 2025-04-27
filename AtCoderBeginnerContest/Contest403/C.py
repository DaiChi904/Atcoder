# 2つだけTLEで悲しい。これくらい許してほしい。。。

def main():
    N, M, Q = map(int,input().split()) 
    queries = [list(map(int, input().split())) for _ in range(Q)]

    permissions = {}

    for query in queries:
        processQuery(permissions, query)

def processQuery(permissions, query):
    if query[0] == 1:
        user = query[1]
        permit = query[2]

        if permissions.get(user) == None:
            permissions[user] = {"user": user, "permited": [permit]}
        elif permissions.get(user).get("permited")[0] != 0:
            currentPermissions = permissions.get(user).get("permited")
            currentPermissions.append(permit)
            permissions[user] = {"user": user, "permited": currentPermissions}

    if query[0] == 2:
        user = query[1]
        permissions[user] = {"user": user, "permited": [0]}

    if query[0] == 3:
        user = query[1]
        target = query[2]

        if permissions.get(query[1]) == None:
            print("No")
        else:
            permission = permissions.get(query[1]).get("permited")

            print("Yes" if target in permission or permission[0] == 0 else "No")

main()
