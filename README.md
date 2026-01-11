This project is a procedural skeletal dragon animation built using Python and Pygame.
The dragon dynamically walks toward the mouse cursor, with realistic leg movement, joints, spine, tail, and skull structure, giving it a lifelike walking behavior similar to modern cursor-following creature animations.

Unlike sprite-based animations, the dragon is generated entirely using mathematics and vectors, making it flexible, lightweight, and highly customizable.

🎯 Key Features

🖱️ Cursor Chasing Behavior – The dragon intelligently moves toward the mouse position.

🦴 Procedural Skeleton System – Spine, ribs, legs, joints, skull, and tail are drawn dynamically.

🚶 Realistic Walking Animation – Legs swing alternately using sine-wave motion.

🧠 Physics-Based Motion – Smooth following using vector math (no teleporting).

⚡ Lightweight & Fast – No sprites, no assets, pure code-driven animation.

🎮 Interactive – Real-time response to mouse movement.

🛠️ Technologies Used

Python 3

Pygame

Vector Mathematics

Trigonometric Motion (Sine Waves)

🧩 How It Works
1. Spine System

The dragon consists of multiple connected segments.

Each segment follows the previous one at a fixed distance, creating a smooth body flow.

2. Walking Legs

Each leg has:

Hip

Knee

Ankle

Foot

Legs swing using a sine function:

Front and back legs move in opposite phases.

This creates a natural walking cycle.

3. Head & Skull

The skull is direction-aware and always faces the movement direction.

Horns and jaw are added for a more dragon-like appearance.

4. Tail Motion

The tail follows the spine and spreads outward at the end to give a skeletal tail look.

🖥️ Installation & Run
Requirements

Python 3.8+

Pygame

Install Pygame
pip install pygame

Run the Project
python dragon.py

🎮 Controls

Move Mouse → Dragon walks toward the cursor

Close Window → Exit the program

📸 Preview

A skeletal dragon smoothly walking across the screen, following the mouse cursor with realistic joint movement and spine flow.

(You can add a GIF or video demo here for GitHub)

🔧 Customization Ideas

Add ground detection for feet placement

Add wing bones and flapping animation

Convert into a game enemy AI

Add color themes or glowing bones

Add sound effects or background music

🚀 Future Scope

This project can be extended into:

A game AI creature

A procedural animation engine

A cursor pet application

A hackathon visual demo

A learning project for physics-based animation

🤝 Credits

Developed by Gourab
Built with curiosity, math, and creativity 🧠✨

📜 License

This project is open-source and free to use for learning and experimentation.
