# import image_slicer
# image_slicer.slice('./images/temp.jpg', 15)

from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2
import pytesseract
from tesserocr import PyTessBaseAPI

def segment_lines(lines, delta):
    h_lines = []
    v_lines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            if abs(x2-x1) < delta: # x-values are near; line is vertical
                v_lines.append(line)
            elif abs(y2-y1) < delta: # y-values are near; line is horizontal
                h_lines.append(line)
    return h_lines, v_lines

def find_intersection(line1, line2):
    # extract points
    x1, y1, x2, y2 = line1[0]
    x3, y3, x4, y4 = line2[0]
    # compute determinant
    Px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4))/  \
        ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    Py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4))/  \
        ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    return Px, Py

def cluster_points(points, nclusters):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, _, centers = cv2.kmeans(points, nclusters, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
    return centers

cropped_file = "./images/cellflow_cropped_border.jpg"
pic = Image.open(cropped_file)
im2arr = np.array(pic) # im2arr.shape: height x width x channel
arr2im = Image.fromarray(im2arr)

M = im2arr.shape[0]//4
N = im2arr.shape[1]//3
row_range = range(0,im2arr.shape[0],M)
col_range = range(0,im2arr.shape[1],N)
tiles0 = [im2arr[x:x+M,y:y+N] for x in range(0,im2arr.shape[0],M) for y in range(0,im2arr.shape[1],N)]
tiles = []
for tile in tiles0:
    if tile.shape[0] != M or tile.shape[1] != N:
        continue
    tiles.append(tile)        

#### Test first image
i = 0
image_0 = Image.fromarray(tiles[0])
slice_file = './images/cellflow' + str(i) + '.png'
image_0.save(slice_file)



img = cv2.imread(slice_file)

# preprocessing
# img = cv2.resize(img, None, fx=.5, fy=.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
dilated = cv2.dilate(edges, np.ones((3,3), dtype=np.uint8))

cv2.imshow("Dilated", dilated)
cv2.waitKey(0)
dilated_file = slice_file.replace('.png', '_dalated.png')
cv2.imwrite(dilated_file, dilated)

# run the Hough transform
lines = cv2.HoughLinesP(dilated, rho=1, theta=np.pi/180, threshold=100, maxLineGap=20, minLineLength=50)

# segment the lines
delta = 10
h_lines, v_lines = segment_lines(lines, delta)

# draw the segmented lines
houghimg = img.copy()
for line in h_lines:
    for x1, y1, x2, y2 in line:
        color = [0,0,255] # color hoz lines red
        cv2.line(houghimg, (x1, y1), (x2, y2), color=color, thickness=1)
for line in v_lines:
    for x1, y1, x2, y2 in line:
        color = [255,0,0] # color vert lines blue
        cv2.line(houghimg, (x1, y1), (x2, y2), color=color, thickness=1)

cv2.imshow("Segmented Hough Lines", houghimg)
cv2.waitKey(0)
hough_file = slice_file.replace('.png', '_hough.png')
cv2.imwrite(hough_file, houghimg)

# find the line intersection points
Px = []
Py = []
for h_line in h_lines:
    for v_line in v_lines:
        px, py = find_intersection(h_line, v_line)
        Px.append(px)
        Py.append(py)

# draw the intersection points
intersectsimg = img.copy()
for cx, cy in zip(Px, Py):
    cx = np.round(cx).astype(int)
    cy = np.round(cy).astype(int)
    color = np.random.randint(0,255,3).tolist() # random colors
    cv2.circle(intersectsimg, (cx, cy), radius=2, color=color, thickness=-1) # -1: filled circle

cv2.imshow("Intersections", intersectsimg)
cv2.waitKey(0)
intersect_file = slice_file.replace('.png', '_intersect.png')
cv2.imwrite(intersect_file, intersectsimg)

# use clustering to find the centers of the data clusters
P = np.float32(np.column_stack((Px, Py)))
nclusters = 4
centers = cluster_points(P, nclusters)
print(centers)

# draw the center of the clusters
for cx, cy in centers:
    cx = np.round(cx).astype(int)
    cy = np.round(cy).astype(int)
    cv2.circle(img, (cx, cy), radius=4, color=[0,0,255], thickness=-1) # -1: filled circle

cv2.imshow("Center of intersection clusters", img)
cv2.waitKey(0)
corner_file = slice_file.replace('.png', '_corner.png')
cv2.imwrite(corner_file, img)


# image_1_1.show()
# text = pytesseract.image_to_string(image_1_1)
# print(text)

# with PyTessBaseAPI() as api:
#     i = 0
#     for tile in tiles:
#         image = Image.fromarray(tile)
#         api.SetImage(image)
#         size = image.size
#         w = size[0]//3
#         h = size[1]//7
#         area = (4, 4, w, h)
#         cropped_img = image.crop(area)

#         # cropped_img.show()
#         crop_name = "./images/res/crop" + str(i) + ".jpg"
#         cropped_img.save(crop_name)
#         api.SetImageFile(crop_name)
#         text = api.GetUTF8Text()
#         print(text)
#         i = i + 1