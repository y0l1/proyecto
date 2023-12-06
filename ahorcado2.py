import random
import time
import tkinter as tk
from tkinter import messagebox

IMÁGENES_AHORCADO = ['''        
  +---+
      |        
      |        
      |        
     ===''', '''        
  +---+       
  O   |
      |       
      |       
     ===''', '''        
  +---+       
  O   |       
  |   |       
      |       
     ===''', '''        
  +---+       
  O   |       
 /|   |       
      |       
     ===''', '''        
  +---+       
  O   |       
 /|\  |       
      |       
     ===''', '''        
  +---+       
  O   |       
 /|\  |       
 /    |       
     ===''', '''        
  +---+       
  O   |       
 /|\  |       
 / \  |       
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

palabras = {'Colores': 'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split(),
            'Formas': 'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentágono hexágono heptágono octágono'.split(),
            'Frutas': 'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split(),
            'Animales': 'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

class AhorcadoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("A H O R C A D O")

        self.letras_incorrectas = ''
        self.letras_correctas = ''
        self.palabra_secreta, self.conjunto_secreto = self.obtener_palabra_al_azar(palabras)
        self.juego_terminado = False
        self.inicio_juego = time.time(3)

        self.etiqueta_palabra = tk.Label(root, text=f"La palabra secreta pertenece al conjunto: {self.conjunto_secreto}",font=("garamond Bold",20))
        self.etiqueta_palabra.pack()

        self.etiqueta_tablero = tk.Label(root, text="", bg="#e44fcd", width="80", height="20")
        self.etiqueta_tablero.pack()

        self.entry_intento = tk.Entry(root, bg="#e3e13b" ) 
        self.entry_intento.pack()

        self.boton_adivinar = tk.Button(root, text="Adivinar", command=self.adivinar_letra,bg="pink",padx=200,pady=15 )
        self.boton_adivinar.pack()

        self.iniciar_juego()
    

    def obtener_palabra_al_azar(self, diccionario_de_palabras):
        clave_de_palabra = random.choice(list(diccionario_de_palabras.keys()))
        índice_de_palabra = random.randint(0, len(diccionario_de_palabras[clave_de_palabra]) - 1)
        return diccionario_de_palabras[clave_de_palabra][índice_de_palabra], clave_de_palabra

    def mostrar_tablero(self):
        imagen_ahorcado = IMÁGENES_AHORCADO[len(self.letras_incorrectas)]
        letras_incorrectas = ' '.join(self.letras_incorrectas)
        espacios_vacíos = ''.join([letra if letra in self.letras_correctas else '_' for letra in self.palabra_secreta])
        tablero = f"{imagen_ahorcado}\n\nLetras incorrectas: {letras_incorrectas}\n{espacios_vacíos}"
        self.etiqueta_tablero.config(text=tablero)

    def adivinar_letra(self):
        intento = self.entry_intento.get().lower()

        if len(intento) != 1 or intento not in 'abcdefghijklmnñopqrstuvwxyz':
            messagebox.showwarning("Error", "Por favor, introduce una letra válida.")
            return

        if intento in self.letras_correctas or intento in self.letras_incorrectas:
            messagebox.showwarning("Error", "Ya has probado esa letra. Elige otra.")
            return

        if intento in self.palabra_secreta:
            self.letras_correctas += intento
            encontrado_todas_las_letras = all(letra in self.letras_correctas for letra in self.palabra_secreta)
            if encontrado_todas_las_letras:
                self.finalizar_juego(ganador=True)
        else:
            self.letras_incorrectas += intento
            if len(self.letras_incorrectas) == len(IMÁGENES_AHORCADO) - 1:
                self.finalizar_juego(ganador=False)

        self.mostrar_tablero()

    def finalizar_juego(self, ganador):
        tiempo_juego = round(time.time() - self.inicio_juego, 2)
        mensaje = f"Tiempo de juego: {tiempo_juego} segundos\n"
        if ganador:
            mensaje += f"¡Sí! ¡La palabra secreta es '{self.palabra_secreta}'! ¡Has ganado!"
        else:
            mensaje += f"Te has quedado sin intentos.\nDespués de {len(self.letras_incorrectas)} intentos fallidos y {len(self.letras_correctas)} aciertos, la palabra era '{self.palabra_secreta}'."
        messagebox.showinfo("Fin del juego", mensaje)
        self.iniciar_juego()

    def iniciar_juego(self):
        self.letras_incorrectas = ''
        self.letras_correctas = ''
        self.palabra_secreta, self.conjunto_secreto = self.obtener_palabra_al_azar(palabras)
        self.juego_terminado = False
        self.inicio_juego = time.time()
        self.etiqueta_palabra.config(text=f"La palabra secreta pertenece al conjunto: {self.conjunto_secreto}")
        self.mostrar_tablero()


if __name__ == "__main__":
    root = tk.Tk()
    app = AhorcadoGUI(root)
    root.mainloop()
