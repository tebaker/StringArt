from PIL import Image, ImageDraw
import numpy as np

class imgController:
    # Init will take in an image and prepare it for string processing
    def __init__(self, img):
        # Grabbing image width, height
        self.w, self.h = img.size
        self.xCenter = np.floor(self.w / 2)
        self.yCenter = np.floor(self.h / 2)
        
        # Creating image matrix, filling all with False (eg white pixels) 
        self.imgMatrix = [[False for i in range(self.w)] for j in range(self.h)]

        # Converting image to black and white and adding dithering
        # imgBW = img.convert('1')

        # Scribing circle based on short side of image
        self.scribeCircle(img, self.h)
        self.scribeNails(img, self.h, 8)
        img.show()

        # Writing img data into img matrix
        # self.extractImgData(img, self.imgMatrix)

        # img.show()

    def scribeCircle(self, img, shortSide):
        # Drawing a circle on the image from the center out
        draw = ImageDraw.Draw(img)

        # Drawing circle matching short side boarders of image
        # first argument = (upperX, upperY, lowerX, lowerY). circle will be drawn in that bounding box 
        draw.ellipse((0, 0, shortSide, shortSide), outline="green", width=3)
        del draw

    def scribeNails(self, img, shortSide, numNails):
        draw = ImageDraw.Draw(img)
        # Dotting the middle for reference
        draw.ellipse((shortSide/2-10,shortSide/2-10,shortSide/2+10,shortSide/2+10), fill="blue", outline="blue", width=3)
        # Drawing 100 'nails' on the image
        for i in range(numNails):
            degree = round(i / numNails * 360)

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

            draw.ellipse((xOffset-10, yOffset-10, xOffset+10, yOffset+10), fill="blue", outline="blue", width=3)

            print(degree, x, y)

        # print(degree, (xOff, yOff))

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
    imgController(img)
        




if __name__ == "__main__":
    main()