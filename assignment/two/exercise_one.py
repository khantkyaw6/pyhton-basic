def TriangleArea(H, W):
    area = 0.5 * H * W
    return area


Height = float(input("Enter Height: "))
Width = float(input("Enter Width: "))

print("Triangle Area = ", TriangleArea(H=Height, W=Width))
