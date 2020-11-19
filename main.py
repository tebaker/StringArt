from PIL import Image, ImageDraw
import numpy as np

class imgController:
    # Init will take in an image and prepare it for string processing
    def __init__(self, img):
        # Grabbing image width, height
        self.w, self.h = img.size
        
        # Creating image matrix, filling all with False (eg white pixels) 
        self.imgMatrix = [[False for i in range(self.w)] for j in range(self.h)]

        # Converting image to black and white and adding dithering
        # imgBW = img.convert('1')

        # Scribing circle based on short side of image
        self.scribeCircle(img, self.h)
        self.scribeNails(img, self.h)
        img.show()

        # Writing img data into img matrix
        # self.extractImgData(img, self.imgMatrix)

        # img.show()

    def scribeCircle(self, img, shortSide):
        # Drawing a circle on the image from the center out
        draw = ImageDraw.Draw(img)

        # Drawing circle matching short side boarders of image
        # first argument = (upperX, upperY, lowerX, lowerY). circle will be drawn in that bounding box 
        draw.ellipse((0, 0, shortSide, shortSide), outline="green", width=2)
        del draw

    def scribeNails(self, img, shortSide):
        draw = ImageDraw.Draw(img)
        # Drawing 100 'nails' on the image
        for i in range(100):
            degree = round(i / 100 * 360)

            xCenter = round(shortSide / 2)
            yCenter = round(shortSide / 2)

            xOff = round(np.cos(degree) * xCenter) + xCenter
            yOff = round(np.sin(degree) * yCenter) + yCenter

            draw.ellipse((xOff, yOff, xOff + 5, yOff + 5), outline="green", width=2)

        print(degree, (xOff, yOff))

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