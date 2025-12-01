def pts_to_grade(points):
    if points >= 18:
        return 'Excellent'
    if points >= 14:
        return 'Good'
    if points >= 10:
        return 'Satisfactory'
    return 'Fail'
pts = 12
grade = pts_to_grade(pts)
print(f'Twoje punkty to: {pts}. Twój wynik to: {grade}')