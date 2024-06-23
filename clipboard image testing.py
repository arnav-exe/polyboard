#copy pasting images to and from clipboard using BytesIO

import io
from PIL import Image
import win32clipboard

def send_to_clipboard(clip_type, contents):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(clip_type, contents)
	win32clipboard.CloseClipboard()

try:
	image = "test string"

	with io.BytesIO() as output:
		image.save(output, format="PNG")
		contents = output.getvalue()
		print(contents)

except:
	image = Image.open("picture1.png")

	with io.BytesIO() as output:
		image.save(output, format="PNG")
		contents = output.getvalue()
		image = Image.open(io.BytesIO(contents))

		#pyperclip.copy(image)
		send_to_clipboard(win32clipboard.CF_DIB, contents)
#SO FAR PASTING FROM CLIPBOARD PRODUCES UNREADABLE IMAGE. IDK WHY