from io import BytesIO
import win32clipboard
from PIL import Image, ImageGrab

clipboardContents = []

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


image = ImageGrab.grabclipboard()

if isinstance(image, bytes):
	output = BytesIO()
	image.convert("RGB").save(output, "BMP")
	data = output.getvalue()[14:]
	output.close()
	clipboardContents.append(data)

	send_to_clipboard(win32clipboard.CF_DIB, data)

	print(clipboardContents)
	print("clipboard contains an image")

else:
	print("clipboard doesn't contain an image")