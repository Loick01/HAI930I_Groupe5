import tkinter as tk
from tkinter import messagebox

class Window :

    def __init__(self, width, height, name, bg_color):
        self.window = tk.Tk()
        self.window.title(name)
        self.window.geometry(width + "x" + height)
        self.window.config(bg=bg_color)

        self.isFullscreen = False
        self.changeFullscreen()  # Fenetre en plein écran par défaut

        self.nameField = tk.Entry(self.window, font=("Arial", 14), width=48)
        self.nameField.pack(pady=(int(height)/2,20))  # Placement du champ de saisie
        self.newUserButton = tk.Button(self.window, text="Commencer", command=self.newUser, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.newUserButton.pack(pady=(0,20))

        self.warningText = tk.Label(self.window, font=("Arial", 16), fg="red", bg=bg_color)

        self.buttonFrame = tk.Frame(self.window, bg=bg_color)  # Créer un frame pour contenir les boutons
        self.analyseButton = tk.Button(self.buttonFrame, text="Analyse", width=30, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.geometrieButton = tk.Button(self.buttonFrame, text="Géométrie", width=30, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.probastatButton = tk.Button(self.buttonFrame, text="Probas/Stats", width=30, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.specialiteButton = tk.Button(self.buttonFrame, text="Spécialité", width=30, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))

        # Ajout d'effets de survol sur les boutons
        for button in [self.analyseButton, self.geometrieButton, self.probastatButton, self.specialiteButton]:
            button.bind("<Enter>", self.onHover)
            button.bind("<Leave>", self.onLeave)

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

            # Utilisation d'un grid dans un frame pour centrer les boutons
            self.buttonFrame.pack(expand=True, pady=20)  # Utilisation du pack pour centrer le frame contenant les boutons
            self.analyseButton.grid(row=0, column=0, padx=10, pady=10) 
            self.geometrieButton.grid(row=0, column=1, padx=10, pady=10) 
            self.probastatButton.grid(row=1, column=0, padx=10, pady=10)
            self.specialiteButton.grid(row=1, column=1, padx=10, pady=10)
        else :
            self.warningText.config(text="Veuillez saisir un nom valide") 
            self.warningText.pack(pady=0)

    def onHover(self, event):
        event.widget.config(bg="#3E8E41")

    def onLeave(self, event):
        event.widget.config(bg="#2196F3")
    
    def closeWindow(self, event=None):
        self.window.destroy()

    def show(self):
        self.window.mainloop()