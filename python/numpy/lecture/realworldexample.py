import numpy as np

sales_data=np.array([
    [1,15000,100000,300000,40000,20000],
    [2,15000,100000,600000,40000,70000],
    [4,15000,100000,900000,40000,20000],
    [5,15000,400000,300000,40000,20000],
    [6,15000,100000,800000,40000,20000],
])

print("===zomato sales anylysis===")
print("shape",sales_data.shape)
print("sample for first three",sales_data[0:3])
print("total sell per year")
print(np.sum(sales_data,axis=0))
print("yearly totL")
print(np.sum(sales_data[:,1:],axis=0))
print("minimum sales per resturent")
print(np.min(sales_data[:,1:],axis=1))
# avg sales per resturent
print(np.mean(sales_data[::1],axis=1))
print("Platform with max sales per year:")
print(np.argmax(sales_data[:,1:], axis=1))







A = np.array([3, 4, 5])
B = np.array([2, 1, 0])

dot_product = np.dot(A, B)

cross_product = np.cross(A, B)

magnitude_A = np.linalg.norm(A)
magnitude_B = np.linalg.norm(B)

cos_theta = dot_product / (magnitude_A * magnitude_B)
angle_radians = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # Clipping ensures numerical stability
angle_degrees = np.degrees(angle_radians)

print("Vector A:", A)
print("Vector B:", B)
print("Dot Product:", dot_product)
print("Cross Product:", cross_product)
print(f"Angle between A and B: {angle_degrees:.2f} degrees")
