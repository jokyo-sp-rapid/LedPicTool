
pitch=5

def three_quarters(img,bg_color):
  
	img_a = img.copy()
	for x in range(img_a.size[0]):
		for y in range(img_a.size[1]):
			if list( img_a.getpixel( (x,y) )[:3] ) == list( bg_color ) :
				img_a.putpixel( (x,y) , list(bg_color)+[0] )
	
	new_img = PIL.Image.new("RGBA", ( img.size[0] / 4 * 3 , img.size[1] ) , list(bg_color)+[255] )
	x_pos = 0
	
	for x_dot in range( img.size[0]/pitch ):
		if x_dot%4==2:
			temp = img_a.crop( ( x_dot*pitch , 0 , (x_dot+1)*pitch , img_a.size[1] ) )
			new_img.paste(temp,((x_pos-1)*pitch,0),temp)
		else:
			temp = img.crop( ( x_dot*pitch , 0 , (x_dot+1)*pitch , img.size[1] ) )
			new_img.paste(temp,(x_pos*pitch,0))
			x_pos+=1
	
	return new_img

def three_halves(img):
	
	new_img = PIL.Image.new("RGBA", ( img.size[0] / 2 * 3 , img.size[1] / 2 * 3 ) , (0,0,0,255) )
	
	for x in range( img.size[0]/pitch ):
		for y in range( img.size[1]/pitch ):
			x_pos = x*3//2
			y_pos = y*3//2
			temp = img.crop( ( x*pitch , y*pitch , (x+1)*pitch , (y+1)*pitch ) )
			new_img.paste(temp,(x_pos*pitch,y_pos*pitch),temp)
			if x%2 == 1:
				new_img.paste(temp,((x_pos+1)*pitch,y_pos*pitch),temp)
				if y%2 == 1:
					new_img.paste(temp,((x_pos+1)*pitch,(y_pos+1)*pitch),temp)
			if y%2 == 1:
				new_img.paste(temp,(x_pos*pitch,(y_pos+1)*pitch),temp)
	
	return new_img
