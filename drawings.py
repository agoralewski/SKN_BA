import matplotlib.pyplot as plt
import json

# airplane 
input_json = "[[[167, 109, 80, 69, 58, 31, 57, 117, 99, 52, 30, 6, 1, 2, 66, 98, 253, 254, 246, 182, 165], [140, 194, 227, 232, 229, 229, 206, 124, 123, 149, 157, 159, 153, 110, 82, 77, 74, 109, 121, 127, 120]], [[207, 207, 210, 221, 238], [74, 103, 114, 128, 135]], [[119, 107, 76, 70, 49, 39, 60, 93], [72, 41, 3, 0, 1, 5, 38, 70]]]"
# windmil 
input_json = "[[[75, 73], [255, 82]], [[68, 62, 65, 73, 86, 93, 92, 83, 73, 67, 64], [84, 73, 59, 52, 52, 61, 83, 88, 89, 88, 82]], [[76, 97], [40, 1]], [[81, 103, 138], [59, 34, 2]], [[96, 164], [65, 60]], [[86, 98, 135], [85, 91, 121]], [[66, 25, 13], [61, 34, 22]], [[55, 20, 0], [70, 78, 87]], [[63, 16, 3], [90, 123, 135]], [[75, 46], [96, 153]]]"
# washing machine 
input_json = "[[[19, 20, 12, 12, 13, 13], [1, 99, 160, 230, 235, 216]], [[16, 99, 133, 232, 235, 255, 232, 215, 150, 62, 1], [0, 2, 7, 8, 87, 226, 236, 239, 238, 225, 228]], [[144, 142, 135, 113, 80, 59, 47, 48, 62, 84, 97, 165, 186, 194, 196, 185, 170, 117], [100, 94, 89, 83, 85, 97, 116, 137, 157, 171, 173, 173, 160, 147, 123, 102, 95, 91]]]"
# trumpet 
input_json = "[[[15, 168, 172, 177, 185, 198, 219, 228, 242, 254, 255, 253, 245, 219, 197, 177, 173, 153, 132, 18], [40, 40, 36, 14, 4, 0, 0, 4, 20, 53, 86, 94, 101, 101, 88, 64, 43, 52, 54, 55]], [[36, 39, 49, 52, 56], [34, 29, 26, 29, 42]], [[61, 75, 82], [37, 32, 41]], [[94, 102, 121, 127], [36, 28, 26, 39]], [[21, 0], [51, 50]]]"
# apple  
input_json = "[[[85, 80, 65, 47, 29, 22, 11, 2, 0, 9, 24, 58, 82, 106, 123, 134, 143, 149, 149, 140, 124, 116, 102, 95, 91, 84, 34, 30, 54, 62, 91, 95, 103, 129, 143], [106, 91, 81, 75, 82, 91, 121, 173, 205, 233, 248, 255, 251, 237, 219, 202, 179, 145, 127, 103, 93, 92, 107, 110, 68, 58, 13, 6, 0, 5, 43, 60, 62, 41, 24]]]"

"""
stroke to tak jakby pociagniecie myszki (np. len(js_doodle)==1 tzn. 
ze ktos narysowal obrazek jednym pociagnieciem - bez puszczania przycisku myszy).

Format każdego obrazka (sposrod tych powyzej - one sa bez zmiennej czasowej)
to lista skladajaca sie z len(js_doodle) elementow (liczba stroke'ow), a kazdy 
stroke sklada sie z dwoch list,na ktorych sa wspolrzedne - x na pierwszej i y na drugiej. 
[x0, x1, x2, x3, ...],
[y0, y1, y2, y3, ...]
"""

js_doodle = json.loads(input_json)
print(len(js_doodle))


plt.figure(figsize=(6,3))
for stroke in js_doodle:
    x,y = stroke[0], [a - b for a, b in zip(([255]*len(stroke[1])), (stroke[1]))]
    plt.subplot(1,2,1)
    plt.plot(x, y, marker='.')
    plt.axis('off')
plt.show()


