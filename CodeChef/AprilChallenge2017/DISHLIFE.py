T = int(input())

for t in range(T):
    N, k = list(map(int, input().split()))
    recipe = set([])
    for n in range(N-1):
        ingredients = input().split()
        for i in range(1, len(ingredients)):
            if ingredients[i] not in recipe:
                recipe.add(ingredients[i])

    ingredients = input().split()

    if len(recipe) == k or len(ingredients)-1 == k:
        print('some')
    else:
        for i in range(1, len(ingredients)):
            if ingredients[i] not in recipe:
                recipe.add(ingredients[i])
        if len(recipe) == k:
            print('all')
        else:
            print('sad')
