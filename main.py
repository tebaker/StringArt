from PIL import Image, ImageDraw
import numpy as np

class imgController:
    # Init will take in an image and prepare it for string processing
    def __init__(self, img, nails):
        # Width, height of the image
        self.w, self.h = img.size

        # Center of the image
        self.xCenter = np.floor(self.w / 2)
        self.yCenter = np.floor(self.h / 2)
        
        self.radius = 0

        if self.xCenter >= self.yCenter:
            self.radius = self.xCenter
        else:
            self.radius = self.yCenter

        # Creating image matrix, filling all with False (eg white pixels) 
        self.imgMatrix = [[False for i in range(self.w)] for j in range(self.h)]

        # Converting image to black and white and adding dithering
        # img = img.convert('1')

        # Scribing circle from the center of the image to the edge
        self.drawCircle(img, self.xCenter, self.yCenter, self.radius, "green", 5)
        self.drawCircle(img, self.xCenter, self.yCenter, 10, "blue", 5)

        # Placing a set amount of 'nails' around the image, following the line of the circle
        self.scribeNails(img, self.h, nails)
        img.show()

        # Writing img data into img matrix
        # self.extractImgData(img, self.imgMatrix)

        # img.show()

    # Draws a circle at center (x, y) with radius r
    def drawCircle(self, img, x, y, r, outlineColor, lineWidth):
        # Drawing a circle on the image from the center out
        draw = ImageDraw.Draw(img)

        # Drawing circle matching short side boarders of image
        # first argument = (upperX, upperY, lowerX, lowerY). circle will be drawn in that bounding box 
        draw.ellipse((x - r, y - r, x + r, y + r), outline=outlineColor, width=lineWidth)

        # Drawing circle to image
        del draw

    def scribeNails(self, img, shortSide, numNails):
        draw = ImageDraw.Draw(img)

        # Drawing 'nails' on the image
        for i in range(numNails):
            degree = (i / numNails * 360)

            # Converting deg to rad
            x = np.cos(degree*np.pi/180)
            y = np.sin(degree*np.pi/180)

            # Calculating x offset from cartesian plane to image grid plane
            xOffset = self.xCenter + self.xCenter * x
            
            # Calculating y offset requires flipping the sign of sin(theta) because
            # the point (0, 0) starts at the upper left and (n, n) ends at the lower right
            if y < 0:
                yOffset = self.yCenter + np.abs(self.yCenter * y)
            else:
                yOffset = self.yCenter - (self.yCenter * y)

            self.drawCircle(img, xOffset, yOffset, 10, "blue", 5)

            # print(degree, xOffset, yOffset)
        del draw


    # Given an image and an array matrix
    def extractImgData(self, img, mat):
        for i in range(self.w):
            # Looping through columns
            for j in range(self.h):
                px = img.getpixel((i, j))
                # If px is 0, means black, True
                if px == 0:
                    mat[i][j] = True
                # If px is 255, means white, False
                else:
                    mat[i][j] = False


def main():
    # Path to image
    path = "jackBlack.png"
    # Opening image as img
    img = Image.open(path)

    # Passing image, 
    imgController(img, 8)
        




if __name__ == "__main__":
    main()