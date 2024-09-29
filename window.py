import tkinter as tk

class Window :

    def __init__(self, width, height, name, bg_color):
        self.window = tk.Tk()
        self.window.title(name)
        self.window.geometry(width + "x" + height)
        self.window.config(bg=bg_color)

        self.isFullscreen = False
        self.changeFullscreen() # Fenetre en plein écran par défaut

        self.nameField = tk.Entry(self.window, font=("Arial", 14), width=48)
        self.nameField.pack(pady=(int(height)/2,20))  # Placement du champ de saisie
        self.newUserButton = tk.Button(self.window, text="Commencer", command=self.newUser)
        self.newUserButton.pack(pady=(0,20))
        self.warningText = tk.Label(self.window, font=("Arial", 16), fg="black")

        self.analyseButton = tk.Button(self.window, text="Analyse", width=30)
        self.geometrieButton = tk.Button(self.window, text="Géométrie", width=30)
        self.probastatButton = tk.Button(self.window, text="Probas/Stats", width=30)
        self.specialiteButton = tk.Button(self.window, text="Spécialité", width=30)

        self.window.bind("<F2>", self.changeFullscreen)
        self.window.bind("<Escape>", self.closeWindow)
    
    def changeFullscreen(self, event=None):
        self.isFullscreen = not self.isFullscreen
        self.window.attributes("-fullscreen", self.isFullscreen) 
    
    def newUser(self):
        username = self.nameField.get()
        if username.strip():
            self.newUserButton.destroy()
            self.nameField.destroy()
            self.warningText.destroy()


            self.analyseButton.grid(row=0, column=0, padx=10, pady=10) 
            self.geometrieButton.grid(row=0, column=1, padx=10, pady=10) 
            self.probastatButton.grid(row=1, column=0, padx=10, pady=10)
            self.specialiteButton.grid(row=1, column=1, padx=10, pady=10)
        else :
            self.warningText.config(text="Veuillez saisir un nom valide") 
            self.warningText.pack(pady=0)

    
    def closeWindow(self, event=None):
        self.window.destroy()

    def show(self):
        self.window.mainloop()