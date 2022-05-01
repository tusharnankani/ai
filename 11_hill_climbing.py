dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def main():
    n = int(input("Enter size of matrix : "))
    mat = take_mat(n)

    cx = int(input("Enter starting x cordinate : "))
    cy = int(input("Enter starting y cordinate : "))

    px = cx
    py = cy

    while True:
        temp_cords = solve(cx, cy, mat, n)
        cx = temp_cords[0]
        cy = temp_cords[1]

        if(cx == px and cy == py):
            print(f"Stabilized at {cx+1 ,cy+1} with value {mat[cx][cy]}")
            break
        else:
            px = cx
            py = cy


def solve(x, y, mat, n):
    ans_x = x
    ans_y = y

    current = mat[x][y]
    
    for i in range(4):
        for j in range(4):
            new_x = x + dx[i]
            new_y = y + dy[j]

            if(inside(new_x, new_y, n) and current < mat[new_x][new_y]):
                ans_x = new_x
                ans_y = new_y
                current = mat[new_x][new_y]

    return [ans_x, ans_y]


def inside(x, y, n):
    if(x < 0 or y < 0 or x >= n or y >= n):
        return False
    return True


def take_mat(n):
    mat = list()
    for i in range(n):
        row = input().split()
        int_row = list()
        for x in row:
            int_row.append(int(x))
        mat.append(int_row)

    return mat


main()
