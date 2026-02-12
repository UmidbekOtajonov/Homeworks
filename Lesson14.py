# """Task1"""
# import numpy as np
#
# # Oddiy funksiya
# def fahrenheit_to_celsius(f):
#     return (f - 32) * 5/9
#
# # Vectorize qilish
# vec_f_to_c = np.vectorize(fahrenheit_to_celsius)
#
# # Berilgan massiv
# temps_f = np.array([32, 68, 100, 212, 77])
#
# # Natija
# temps_c = vec_f_to_c(temps_f)
# print("Fahrenheit:", temps_f)
# print("Celsius:", temps_c)
#
#
# """Task2"""
# import numpy as np
#
# # Custom funksiya
# def custom_power(num, power):
#     return num ** power
#
# # Vectorize qilish
# vec_power = np.vectorize(custom_power)
#
# # Berilgan massivlar
# numbers = np.array([2, 3, 4, 5])
# powers  = np.array([1, 2, 3, 4])
#
# # Har bir juftlikka amal qilish
# results = vec_power(numbers, powers)
#
# print("Numbers:", numbers)
# print("Powers: ", powers)
# print("Results:", results)
#
#
# """Task3"""
# import numpy as np
#
# # Koeffitsientlar matritsasi
# A = np.array([[4, 5, 6],
#               [3, -1, 1],
#               [2, 1, -2]])
#
# # Natijalar vektori
# B = np.array([7, 4, 5])
#
# # Sistemani yechish
# solution = np.linalg.solve(A, B)
#
# print("x, y, z =", solution)
#
#
# """Task4"""
# import numpy as np
#
# # Koeffitsientlar matritsasi
# A = np.array([[10, -2, 3],
#               [-2, 8, -1],
#               [3, -1, 6]])
#
# # Natijalar vektori
# B = np.array([12, -5, 15])
#
# # Sistemani yechish
# solution = np.linalg.solve(A, B)
#
# print("I1, I2, I3 =", solution)
#
#
# """Task5"""
#
# import numpy as np
# from PIL import Image
#
# # 1. Flip Image
# def flip_image(img_array):
#     flipped_h = np.fliplr(img_array)   # Horizontal flip
#     flipped_v = np.flipud(img_array)   # Vertical flip
#     return flipped_h, flipped_v
#
#
# # 2. Add Random Noise
# def add_noise(img_array, noise_level=50):
#     noise = np.random.randint(-noise_level, noise_level, img_array.shape, dtype=np.int16)
#     noisy_img = img_array.astype(np.int16) + noise
#     noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
#     return noisy_img
#
# # 3. Brighten Channels
# def brighten_channels(img_array, value=40):
#     bright_img = img_array.astype(np.int16)
#     bright_img[..., 0] = np.clip(bright_img[..., 0] + value, 0, 255)  # Red channel
#     return bright_img.astype(np.uint8)
#
# # 4. Apply Mask
# def apply_mask(img_array, mask_size=(100, 100)):
#     h, w, _ = img_array.shape
#     mh, mw = mask_size
#     start_h = h//2 - mh//2
#     start_w = w//2 - mw//2
#     img_array[start_h:start_h+mh, start_w:start_w+mw] = [0, 0, 0]
#     return img_array
#
# # --- MAIN EXECUTION ---
# # Read image
# img = Image.open("images/birds.jpg")
# img_array = np.array(img)
#
# # Apply manipulations
# flipped_h, flipped_v = flip_image(img_array)
# noisy_img = add_noise(img_array)
# bright_img = brighten_channels(img_array)
# masked_img = apply_mask(img_array.copy())
#
# # Save results
# Image.fromarray(flipped_h).save("images/birds_flipped_h.jpg")
# Image.fromarray(flipped_v).save("images/birds_flipped_v.jpg")
# Image.fromarray(noisy_img).save("images/birds_noisy.jpg")
# Image.fromarray(bright_img).save("images/birds_bright.jpg")
# Image.fromarray(masked_img).save("images/birds_masked.jpg")
#




