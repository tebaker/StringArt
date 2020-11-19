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
        img = img.convert('1')

        # Scribing circle based on short side of image
        if self.w > self.h:
            img = self.scribeCircle(img, self.h)
        else:
            img = self.scribeCircle(img, self.w)

        # Writing img data into img matrix
        self.extractImgData(img, self.imgMatrix)

        # img.show()

    def scribeCircle(self, img, shortSide):
        # Drawing a circle on the image from the center out
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, self.w, self.h), outline="green", width=2)
        del draw

        return img

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