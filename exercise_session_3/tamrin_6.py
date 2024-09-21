def print_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(' '.join(str(x) for x in row))
tedad = int(input('tedad_ra_vared_konid: '))
print_pascals_triangle(tedad)