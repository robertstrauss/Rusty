from SimpleCV import Camera

myCamera = Camera(prop_set={'width':320, 'height': 240})

print "--------------------------------face detctor detcting-----------"

def hasFace():
   frame = myCamera.getImage()
   #print myCamera.getImage()
   faces = frame.findHaarFeatures('face')
   if faces:
      return True
   return False

exit(hasFace())
