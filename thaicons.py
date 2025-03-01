import tkinter as tk
import random

# Thai consonants dictionary: {symbol: name}
thai_consonants = {
    "ก": "กอ ไก่ (gor gai)",
    "ข": "ขอ ไข่ (khor khai)",
    "ฃ": "ฃอ ขวด (khor khuat)",
    "ค": "คอ ควาย (khor khwai)",
    "ฅ": "ฅอ คน (khor khon)",
    "ฆ": "ฆอ ระฆัง (khor rakhang)",
    "ง": "งอ งู (ngor ngu)",
    "จ": "จอ จาน (jor jan)",
    "ฉ": "ฉอ ฉิ่ง (chor ching)",
    "ช": "ชอ ช้าง (chor chang)",
    "ซ": "ซอ โซ่ (sor so)",
    "ญ": "ญอ หญิง (yor ying)",
    "ฎ": "ฎอ ชฎา (dor chada)",
    "ฏ": "ฏอ ปฏัก (tor patak)",
    "ฐ": "ฐอ ฐาน (thor than)",
    "ฑ": "ฑอ มณโฑ (thor montho)",
    "ณ": "ณอ เณร (nor nene)",
    "ด": "ดอ เด็ก (dor dek)",
    "ต": "ตอ เต่า (tor tao)",
    "ถ": "ถอ ถุง (thor thung)",
}

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcard Game")

        self.current_consonant = None
        self.flipped = False

        self.card_frame = tk.Frame(root, width=300, height=200, bg="white", relief="raised", bd=3)
        self.card_frame.pack(pady=20)

        self.card_label = tk.Label(self.card_frame, text="", font=("Arial", 40), bg="white")
        self.card_label.pack(expand=True)

        self.flip_button = tk.Button(root, text="Flip Card", command=self.flip_card, font=("Arial", 14))
        self.flip_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack()

        self.next_card()

    def next_card(self):
        self.flipped = False
        self.current_consonant = random.choice(list(thai_consonants.keys()))
        self.card_label.config(text=self.current_consonant, font=("Arial", 60))
    
    def flip_card(self):
        if not self.flipped:
            self.card_label.config(text=thai_consonants[self.current_consonant], font=("Arial", 20))
            self.flipped = True
        else:
            self.card_label.config(text=self.current_consonant, font=("Arial", 60))
            self.flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()
