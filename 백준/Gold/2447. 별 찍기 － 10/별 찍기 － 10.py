def draw_star(size):
    if size == 1:
        return ["*"]

    stars = draw_star(size//3)
    res = []

    for star in stars:
        res.append(star*3)
    for star in stars:
        res.append(star+" "*(size//3)+star)
    for star in stars:
        res.append(star*3)
    return res
    
N = int(input())
print("\n".join(draw_star(N)))