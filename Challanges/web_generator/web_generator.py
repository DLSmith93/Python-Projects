
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # label fro text box
        self.customLabel = tk.Label(text="Enter the text for your custom HTML page: ")
        self.customLabel.grid(row=0, column=0, padx=(30, 0), pady=(5,0), sticky=N+W)
        # text entry box for creating a custom HTML page
        self.custom_HTML = Entry(width=100)
        self.custom_HTML.grid(row=1, column=0, columnspan=2, padx=(30,10), pady=(5,10))

        # button for generating default web page
        self.default_btn = Button(text="default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=1, padx=(10,10), pady=(10,10))
        # button for generating a custom web page
        self.custom_btn = Button(text="Custom HTML Page", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for an amazing sale!"
        htmlFile = open("./index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("./index.html")

    def customHTML(self):
        htmlText = self.custom_HTML.get()
        htmlFile = open("./index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("./index.html")


if __name__ == "__main__":

    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

