import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraAvanzada:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Avanzada")
        self.root.geometry("500x600")
        
        # Variable para almacenar la expresión
        self.expresion = ""
        
        # Pantalla de resultados
        self.resultado = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.resultado.grid(row=0, column=0, columnspan=5, padx=10, pady=20)
        
        # Botones de la calculadora
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('√', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3), ('(', 4, 4),
            (')', 5, 0), ('.', 5, 1), ('pi', 5, 2), ('e', 5, 3), ('^', 5, 4)
        ]
        
        # Crear los botones
        for (texto, fila, col) in botones:
            button = tk.Button(root, text=texto, font=("Arial", 18), height=2, width=4, command=lambda t=texto: self.presionar(t))
            button.grid(row=fila, column=col, padx=5, pady=5)
        
    def presionar(self, boton):
        """Método para manejar las presiones de los botones."""
        if boton == 'C':
            self.expresion = ""  # Limpiar la pantalla
        elif boton == '=':
            try:
                # Evaluar la expresión matemática
                self.expresion = self.calcular(self.expresion)
            except ZeroDivisionError:
                # Mostrar un mensaje si se intenta dividir por cero
                messagebox.showerror("Error", "¡No se puede dividir por cero!")
                self.expresion = ""
            except Exception as e:
                # Manejo de errores en la entrada
                messagebox.showerror("Error", f"Entrada inválida: {e}")
                self.expresion = ""
        else:
            self.expresion += str(boton)
        
        # Actualizar la pantalla con la expresión o resultado
        self.resultado.delete(0, tk.END)
        self.resultado.insert(tk.END, self.expresion)
    
    def calcular(self, expr):
        """Evaluar la expresión matemática, manejando operaciones avanzadas."""
        # Reemplazar 'pi' y 'e' con sus valores numéricos
        expr = expr.replace('pi', str(math.pi)).replace('e', str(math.e))
        
        # Reemplazar las operaciones de raíz cuadrada y potencia
        expr = expr.replace('√', 'math.sqrt')  # Raíz cuadrada
        expr = expr.replace('^', '**')  # Potencia
        expr = expr.replace('log', 'math.log10')  # Logaritmo base 10
        
        # Evaluar la expresión con las funciones matemáticas
        try:
            return str(eval(expr))
        except Exception as e:
            raise ValueError(f"Error en la expresión: {e}")

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    calculadora = CalculadoraAvanzada(root)
    root.mainloop()
