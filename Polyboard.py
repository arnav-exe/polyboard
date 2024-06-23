from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pynput.keyboard import Key, Controller, KeyCode, Listener
kb = Controller()

from plyer import notification
from win10toast import ToastNotifier
from tkinter import Tk
import pyperclip

import os
import sys 

def quitApp(self):
	sys.exit()

def start(self):
	clipboardContents = []
	x = 0

	iconPath = os.getcwd() + "\\final.ico"
	print(iconPath)

	def popup(num):
		if len(clipboardContents[num]) > 64:
			titletext = ((clipboardContents[num])[:60]) + "..."
		else:
			titletext = clipboardContents[num]

		try:
			from plyer import notification
			notification.notify(title=titletext, 
				message='has been copied to your clipboard',
				app_name='Polyboard',
				app_icon=iconPath,
				timeout=2.5)

		except:
			from win10toast import ToastNotifier
			toaster = ToastNotifier()
			toaster.show_toast(titletext,
							   "has been copied to your clipboard",
							   icon_path=iconPath,
							   duration=2.5)


	def clipboardToList():
		global x
		if len(clipboardContents) < 10:
			clipboardContents.append(Tk().clipboard_get())
			#print(clipboardContents) #for diagnostics
		else:
			clipboardContents[x] = (Tk().clipboard_get())
			#print(clipboardContents)
			x += 1
			
			if x == 10:
				x = 0

	def listToClipboard(text):
		pyperclip.copy(text)


	def paster1():
		if len(clipboardContents) >= 1:
			listToClipboard(clipboardContents[0])
			popup(0)
		else:
			listToClipboard("")
			

	def paster2():
		if len(clipboardContents) >= 2:
			listToClipboard(clipboardContents[1])
			popup(1)
		else:
			listToClipboard("")

	def paster3():
		if len(clipboardContents) >= 3:
			listToClipboard(clipboardContents[2])
			popup(2)
		else:
			listToClipboard("")

	def paster4():
		if len(clipboardContents) >= 4:
			listToClipboard(clipboardContents[3])
			popup(3)
		else:
			listToClipboard("")

	def paster5():
		if len(clipboardContents) >= 5:
			listToClipboard(clipboardContents[4])
			popup(4)
		else:
			listToClipboard("")

	def paster6():
		if len(clipboardContents) >= 6:
			listToClipboard(clipboardContents[5])
			popup(5)
		else:
			listToClipboard("")

	def paster7():
		if len(clipboardContents) >= 7:
			listToClipboard(clipboardContents[6])
			popup(6)
		else:
			listToClipboard("")

	def paster8():
		if len(clipboardContents) >= 8:
			listToClipboard(clipboardContents[7])
			popup(7)
		else:
			listToClipboard("")

	def paster9():
		if len(clipboardContents) >= 9:
			listToClipboard(clipboardContents[8])
			popup(8)
		else:
			listToClipboard("")

	def paster0():
		if len(clipboardContents) >= 10:
			listToClipboard(clipboardContents[9])
			popup(9)
		else:
			listToClipboard("")

	combination_to_function = {
		frozenset([Key.ctrl_l, KeyCode(vk=67)]): clipboardToList,  # ctrl_l + c
		frozenset([Key.ctrl_r, KeyCode(vk=67)]): clipboardToList,  # ctrl_r + c
		frozenset([Key.ctrl_l, KeyCode(vk=88)]): clipboardToList,  # ctrl_l + x
		frozenset([Key.ctrl_r, KeyCode(vk=88)]): clipboardToList,  # ctrl_r + x   

		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=49)]): paster1,  # ctrl_l + shift + 1
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=50)]): paster2,  # ctrl_l + shift + 2
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=51)]): paster3,  # ctrl_l + shift + 3
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=52)]): paster4,  # ctrl_l + shift + 4
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=53)]): paster5,  # ctrl_l + shift + 5
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=54)]): paster6,  # ctrl_l + shift + 6
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=55)]): paster7,  # ctrl_l + shift + 7
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=56)]): paster8,  # ctrl_l + shift + 8
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=57)]): paster9,  # ctrl_l + shift + 9
		frozenset([Key.ctrl_l, Key.shift, KeyCode(vk=58)]): paster0,  # ctrl_l + shift + 0
	}

	pressed_vks = set()

	def get_vk(key):
		#Get the virtual key code from a key.
		#These are used so case/shift modifications are ignored.
		return key.vk if hasattr(key, 'vk') else key.value.vk


	def is_combination_pressed(combination):
		#Check for combination using the keys pressed in pressedVks
		return all([get_vk(key) in pressed_vks for key in combination])


	def on_press(key):
		vk = get_vk(key)  # Get the keys vk
		pressed_vks.add(vk)  # Add it to the list of currently pressed keys

		for combination in combination_to_function:  # Loop through each combination
			if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
				combination_to_function[combination]()  # If yes then execute the function


	def on_release(key):
		vk = get_vk(key)  # Get the keys vk
		pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon("final.png")

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()
option1 = QAction("Start application")
menu.addAction(option1)
option1.triggered.connect(start)

quit = QAction("Quit application") #creating the action instance
menu.addAction(quit) #adding action to the toolbar
quit.triggered.connect(quitApp)

tray.setContextMenu(menu)

app.exec_()
