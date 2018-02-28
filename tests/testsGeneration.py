import polarTransform
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os
from tests.util import loadImage, saveImage

shortAxisApexImage = loadImage('shortAxisApex.png', False, True)
verticalLinesImage = loadImage('verticalLines.png', False)
horizontalLinesImage = loadImage('horizontalLines.png', False)
checkerboardImage = loadImage('checkerboard.png', False)

shortAxisApexPolarImage = loadImage('shortAxisApexPolarImage.png')
shortAxisApexPolarImage_centerMiddle = loadImage('shortAxisApexPolarImage_centerMiddle.png')
verticalLinesPolarImage = loadImage('verticalLinesPolarImage.png')
verticalLinesPolarImage_scaled = loadImage('verticalLinesPolarImage_scaled.png')
verticalLinesPolarImage_scaled2 = loadImage('verticalLinesPolarImage_scaled2.png')


def generateShortAxisPolar():
    polarImage, ptSettings = polarTransform.convertToPolarImage(shortAxisApexImage, center=[401, 365])
    saveImage('shortAxisApexPolarImage.png', polarImage)


def generateShortAxisPolar2():
    polarImage, ptSettings = polarTransform.convertToPolarImage(shortAxisApexImage)
    saveImage('shortAxisApexPolarImage_centerMiddle.png', polarImage)


def generateVerticalLinesPolar():
    polarImage, ptSettings = polarTransform.convertToPolarImage(verticalLinesImage)
    saveImage('verticalLinesPolarImage.png', polarImage)


def generateVerticalLinesPolar2():
    polarImage, ptSettings = polarTransform.convertToPolarImage(verticalLinesImage, initialRadius=30, finalRadius=100,
                                                                initialAngle=2 / 4 * np.pi, finalAngle=5 / 4 * np.pi,
                                                                radiusSize=140, angleSize=700)
    saveImage('verticalLinesPolarImage_scaled.png', polarImage)


# Enable these functions as you see fit to generate the images
# Note: It is up to the developer to ensure these images are created and look like they are supposed to
# generateShortAxisPolar()
# generateShortAxisPolar2()
# generateVerticalLinesPolar()
# generateVerticalLinesPolar2()

# TODO Remove warning skimage dtype
# TODO Dont forget note that finalRadius/Angle is NOT included. It is everything up to that
# TODO Handle rotating 90 degrees
# TODO Check ptSettings for validity
# TODO Clip the radius
# TODO Clip the angle
# TODO Add method support
# TODO Add border support and stuff
# TODO Add note about origin and stuff (should I do that)?
# TODO Check origin