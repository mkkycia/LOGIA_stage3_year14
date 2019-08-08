def spotkanie(robot1, robot2):
    a = max(len(robot1),len(robot2))
    robot1 += (a - len(robot1)) * '0'
    robot2 += (a - len(robot2)) * '0'
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    for i in range(max(len(robot1), len(robot2))):
        if i == 100:
            break
        if robot1[i] == 'g':
            y1 += 1
        elif robot1[i] == 'd':
            y1 -= 1
        elif robot1[i] == 'p':
            x1 += 1
        elif robot1[i] == 'l':
            y1 -= 1
        if robot2[i] == 'g':
            y2 += 1
        elif robot2[i] == 'd':
            y2 -= 1
        elif robot2[i] == 'p':
            x2 += 1
        elif robot2[i] == 'l':
            x2 -= 1
        if x1 == x2 and y1 == y2:
            return i + 1
    return 0

print(spotkanie("pd", "g"))
print(spotkanie("gp", "pg"))
print(spotkanie("dg", "ggppddll"))	
