import pyautogui as pag
import time
from PIL import Image

''' 
educational tool for scraping all the pages from an ebook in the amazon kindle app for windows

for educational purposes only, just thought it was interesting that you could do this. and it scrapes pretty quickly too.

run the program, then during the wait time switch over to the amazon kindle app for pc.

TO FORCE STOP JUST DRAG YOUR MOUSE INTO THE TOP LEFT CORNER!!!
'''

def main():
	full_book_imgs = []

	amount_of_clicks = 633 # change this to the amount of pages in the ebook
	wait_time = 8

	for i in range(wait_time):
		print(f'Starting in {wait_time-i} seconds...')
		time.sleep(1)

	# these values will probably need to be changed
	# you can use test() function to see your mouse location and do some math that way
	x, y = 980, 94
	size_x, size_y = 722, 922

	x-=size_x/2 # centers the x position in the middle of the content size_x

	for i in range(amount_of_clicks):
		img = pag.screenshot('screenshot.png', region=(980-722/2, 94, 722, 922))

		full_book_imgs.append(img)

		# next page
		if img:
			pag.click(1668, 67) # position of the next button

		img = None

	pdf_name = 'complete_book.pdf'

	# delete the first image because we append all the other ones to it later in the .save
	image1 = full_book_imgs[0]
	del full_book_imgs[0]

	image1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=full_book_imgs)
	# the result will be saved as a bunch of images in a pdf, but you can use a site like https://tools.pdf24.org to make words selectable.

def test():
	while True:
		print(pag.position())

if __name__ == '__main__':
	main()