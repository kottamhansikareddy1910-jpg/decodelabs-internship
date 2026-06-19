import cv2

img = cv2.imread("sample.png")

if img is None:
    print("Image not found!")
else:
    print("Image loaded successfully!")
    print("Width:", img.shape[1])
    print("Height:", img.shape[0])

    cv2.imshow("Sample Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()