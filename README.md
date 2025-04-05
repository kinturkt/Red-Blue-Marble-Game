# 🎮 Red-Blue Nim Game (Tkinter GUI)

A fun and strategic turn-based game built using Python's Tkinter library, where a human player competes against a computer AI in a simplified Red-Blue Marble Game (Nim variant).

---

## 🧠 Game Concept

You start with a pile of red and blue marbles. On each turn, a player can remove **1 or 2 marbles** of a **selected color** (red or blue). The game ends when **either** red or blue marbles run out.

- 💡 The computer uses a greedy strategy based on a custom evaluation function.
- 🤖 Can you outsmart the machine?

---

## 🎯 Features

- GUI interface built with **Tkinter**
- Interactive **Human vs. AI** gameplay
- Smart AI using a weighted scoring system: `2 * red + 3 * blue`
- End-game result pop-ups and status updates
- Clean and simple layout

---

## 🖥️ How to Run

### ✅ Requirements

- Python 3.x  
- No external libraries required

---

### ▶️ Run the game

```bash
python red_blue_nim_gui.py

🎮 Gameplay Instructions
Choose how many marbles to remove (1 or 2).

Select the marble color (red or blue).

Click Make Move.

The computer will respond with its move.

The game ends when red or blue marbles are depleted.
