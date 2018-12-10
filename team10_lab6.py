# Team 10 - Tech Life Balance Best Engineers
# Module 2 Lab 6
# M. Mariscal, C. Piwarski, W. Robleh
# 04 November 2018

def getPic():
  filename = pickAFile()
  pic = makePicture(filename)
  return pic

def fixRedEye(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  redEyeColor = makeColor(150, 5, 50)
  dist = 200.0
  # Left Eye
  for x in range(120, 155):    
    for y in range(150, 190):
      p = getPixel(pic, x, y)
      color = getColor(p)
      if distance(redEyeColor, color) < dist:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        a = (r + g + b) / 3
        newColor = makeColor(a, a, a)
        setColor(p, newColor)  
    # Right Eye
    for x in range(358, 390):    
      for y in range(150, 190):
        p = getPixel(pic, x, y)
        color = getColor(p)
        if distance(redEyeColor, color) < dist:
          r = getRed(p)
          g = getGreen(p)
          b = getBlue(p)
          a = (r + g + b) / 3
          newColor = makeColor(a, a, a)
          setColor(p, newColor)  
  return pic

#Problem 1- version 2
def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    b = getBlue(p)
    g = getGreen(p)
    r = getRed(p)
    avg = (b*0.114) + (g*0.587) + (r*0.299)
    setRed(p, avg)
    setGreen(p, avg)
    setBlue(p, avg)
  return pic

def makeSepia(pic):
  # betterBnW() process
  pic = betterBnW(pic)
  # sepia process
  for p in getPixels(pic):
    b = getBlue(p)
    g = getGreen(p)
    r = getRed(p)
    # apply sepia values
    if r < 63:
      r = r * (1.1)
      b = b * (0.9)
    elif r > 62 and r < 192:
      r = r * (1.15)
      b = b * (0.85)
    else: 
      r = r*(1.08)
      b = b*(0.93)
    color = makeColor(r, g, b)
    setColor(p, color) 
  return pic

# Problem 2 - Artify
#calculateColor for red,green and blue
def calculateColor(color):
    if color < 64:
      color = 31
    elif color >63 and color < 128:
      color = 95  
    elif color > 127 and color < 192:
      color = 159
    else:
      color = 223
    return color

def Artify(pic):
  for p in getPixels(pic):
    b = getBlue(p)
    g = getGreen(p)
    r = getRed(p)
    # apply Artify
    r = calculateColor(r)
    b = calculateColor(b)
    g = calculateColor(g)
    color = makeColor(r, g, b)
    setColor(p, color) 
  return pic
  
# Problem 3 - Green Screen
def chromakey(greenScreenPic, backgroundPic):

  # pull green screen color from image
  greenScreenColor = makeColor(50, 200, 70)

  # adjust distance depending on background
  dist = 103.0
  
  for p in getPixels(greenScreenPic):
    color = getColor(p)
    if distance(greenScreenColor, color) < dist:
      x = getX(p)
      y = getY(p)
      new_p = getPixel(backgroundPic, x, y)
      newColor = getColor(new_p)
      setColor(p, newColor)
  return greenScreenPic

