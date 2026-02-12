# #**1. Basic Plotting**
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define the function
# def f(x):
#     return x**2 - 4*x + 4
#
# # Generate x values between -10 and 10
# x = np.linspace(-10, 10, 400)
# y = f(x)
#
# # Create the plot
# plt.figure(figsize=(8, 6))
# plt.plot(x, y, label=r'$f(x) = x^2 - 4x + 4$', color='blue')
#
# # Customize the plot
# plt.xlabel('x values')
# plt.ylabel('f(x)')
# plt.title('Plot of f(x) = x^2 - 4x + 4')
# plt.grid(True)
# plt.legend()
#
# # Show the plot
# plt.show()
#
#
# # **2. Sine and Cosine Plot**
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Generate x values from 0 to 2π
# x = np.linspace(0, 2*np.pi, 400)
#
# # Compute sine and cosine
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# # Create the plot
# plt.figure(figsize=(8, 6))
#
# # Plot sine with red dashed line and circle markers
# plt.plot(x, y_sin, 'r--o', label=r'$\sin(x)$', markevery=40)
#
# # Plot cosine with blue solid line and square markers
# plt.plot(x, y_cos, 'b-^', label=r'$\cos(x)$', markevery=40)
#
# # Customize the plot
# plt.xlabel('x (radians)')
# plt.ylabel('Function values')
# plt.title('Plot of sin(x) and cos(x)')
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()
#
#
# # **3. Subplots**
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define x ranges for each function
# x1 = np.linspace(-10, 10, 400)       # for x^3
# x2 = np.linspace(-2*np.pi, 2*np.pi, 400)  # for sin(x)
# x3 = np.linspace(-2, 2, 400)         # for e^x
# x4 = np.linspace(0, 10, 400)         # for log(x+1), domain x >= 0
#
# # Define functions
# y1 = x1**3
# y2 = np.sin(x2)
# y3 = np.exp(x3)
# y4 = np.log(x4 + 1)
#
# # Create 2x2 subplots
# fig, axs = plt.subplots(2, 2, figsize=(10, 8))
#
# # Top-left: x^3
# axs[0, 0].plot(x1, y1, color='blue')
# axs[0, 0].set_title(r'$f(x) = x^3$')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('f(x)')
# axs[0, 0].grid(True)
#
# # Top-right: sin(x)
# axs[0, 1].plot(x2, y2, color='red')
# axs[0, 1].set_title(r'$f(x) = \sin(x)$')
# axs[0, 1].set_xlabel('x')
# axs[0, 1].set_ylabel('f(x)')
# axs[0, 1].grid(True)
#
# # Bottom-left: e^x
# axs[1, 0].plot(x3, y3, color='green')
# axs[1, 0].set_title(r'$f(x) = e^x$')
# axs[1, 0].set_xlabel('x')
# axs[1, 0].set_ylabel('f(x)')
# axs[1, 0].grid(True)
#
# # Bottom-right: log(x+1)
# axs[1, 1].plot(x4, y4, color='purple')
# axs[1, 1].set_title(r'$f(x) = \log(x+1)$')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('f(x)')
# axs[1, 1].grid(True)
#
# # Adjust layout
# plt.tight_layout()
# plt.show()
#
#
# # **4. Scatter Plot**
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Generate random x and y values from uniform distribution [0, 10]
# x = np.random.uniform(0, 10, 100)
# y = np.random.uniform(0, 10, 100)
#
# # Create the scatter plot
# plt.figure(figsize=(8, 6))
#
# # Use different colors and markers
# plt.scatter(x, y, c=np.random.rand(100), marker='o', cmap='viridis', edgecolor='black')
#
# # Customize the plot
# plt.title('Scatter Plot of 100 Random Points')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.grid(True)
#
# # Show the plot
# plt.show()
#
# # **5. Histogram**
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Generate random dataset from normal distribution (mean=0, std=1)
# data = np.random.normal(loc=0, scale=1, size=1000)
#
# # Create the histogram with 30 bins
# plt.figure(figsize=(8, 6))
# plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
#
# # Customize the plot
# plt.title('Histogram of Normally Distributed Data')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.grid(True)
#
# # Show the plot
# plt.show()
#
#
# # **6. 3D Plotting**
# import numpy as np
# import matplotlib.pyplot as plt
#
# # X va Y qiymatlari (-5, 5) oralig'ida
# x = np.linspace(-5, 5, 200)
# y = np.linspace(-5, 5, 200)
# X, Y = np.meshgrid(x, y)
#
# # Funksiya qiymatlari
# Z = np.cos(X**2 + Y**2)
#
# # 3D plot yaratish
# fig = plt.figure(figsize=(10, 8))
#
# ax = plt.axes(projection='3d')
#
# # Surface plot
# surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
#
# # O‘qlar nomlari va sarlavha
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('f(x, y)')
# ax.set_title(r'3D Surface Plot of $f(x, y) = \cos(x^2 + y^2)$')
#
# # Colorbar qo‘shish (surf bilan bog‘lash kerak)
# fig.colorbar(surf, shrink=0.5, aspect=10)
#
# plt.show()
#
#
# import matplotlib.pyplot as plt
#
# # Mahsulotlar va ularning sotuv qiymatlari
# products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
# sales = [200, 150, 250, 175, 225]
#
# # Har bir ustun uchun ranglar
# colors = ['skyblue', 'salmon', 'lightgreen', 'orange', 'violet']
#
# # Bar chart yaratish
# plt.figure(figsize=(8, 6))
# plt.bar(products, sales, color=colors, edgecolor='black')
#
# # Diagrammani sozlash
# plt.title('Sales Data for Products')
# plt.xlabel('Products')
# plt.ylabel('Sales Values')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
#
# # Ko‘rsatish
# plt.show()
#
# # **8. Stacked Bar Chart**
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Vaqt davrlari
# time_periods = ['T1', 'T2', 'T3', 'T4']
#
# # Har bir kategoriya uchun ma'lumotlar (namuna)
# category_A = [20, 35, 30, 35]
# category_B = [25, 32, 34, 20]
# category_C = [30, 25, 20, 25]
#
# # Bar chart yaratish
# fig, ax = plt.subplots(figsize=(8, 6))
#
# # Stacked bar chart
# ax.bar(time_periods, category_A, label='Category A', color='skyblue', edgecolor='black')
# ax.bar(time_periods, category_B, bottom=category_A, label='Category B', color='salmon', edgecolor='black')
# ax.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B),
#        label='Category C', color='lightgreen', edgecolor='black')
#
# # Diagramma sozlash
# ax.set_title('Stacked Bar Chart of Categories over Time')
# ax.set_xlabel('Time Periods')
# ax.set_ylabel('Values')
# ax.legend()
# ax.grid(axis='y', linestyle='--', alpha=0.7)
#
# plt.show()







