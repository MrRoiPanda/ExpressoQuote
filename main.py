from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import simpledialog, scrolledtext
import textwrap

def create_image_with_quote(quote, output_path):
    image = Image.new('RGB', (1080, 1350), color='#f6eee3')
    draw = ImageDraw.Draw(image)

    font_path = "AdventPro-VariableFont_wdth,wght.ttf"
    font_size = 80
    font = ImageFont.truetype(font_path, size=font_size)

    wrapped_text = textwrap.fill(quote, width=22)
    text_x = (image.width - draw.textbbox((0, 0), wrapped_text, font=font)[2]) // 2
    text_y = (image.height - draw.textbbox((0, 0), wrapped_text, font=font)[3]) // 2 - 20

    draw.text((text_x, text_y), wrapped_text, font=font, fill='black')

    image.save(output_path)

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("ExpressoQuote")
        self.geometry("500x300")
        self.text_widget = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=10)
        self.text_widget.pack(padx=10, pady=10)
        return self.text_widget

    def apply(self):
        self.result = self.text_widget.get(1.0, tk.END)

root = tk.Tk()
root.title("ExpressoQuote")
root.withdraw() 

dialog = CustomDialog(root)
citation_utilisateur = dialog.result

if citation_utilisateur is not None:
    chemin_sortie_image = "Output/image.png"
    create_image_with_quote(citation_utilisateur, chemin_sortie_image)
    print("Image créée avec succès !")
else:
    print("Annulation de la saisie.")
