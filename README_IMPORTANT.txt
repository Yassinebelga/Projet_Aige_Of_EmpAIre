Hello everyone,

I’ll speak in English to express myself more easily, haha.

I’ve pushed the new models to GitHub. Please check the updated files. I’ve removed the older versions we created (don’t worry, I didn’t change the initial content). However, I made a lot of optimizations and modifications. Initially, the files contained nothing particularly special—just the constructors.

Here’s what’s new:
1. Matrix Logic in the Game

    Previously, the cell matrix was an NxN 2D array. While not incorrect, it was inefficient in terms of memory usage and performance.
    I’ve replaced the NxN 2D array with a sparse matrix (a.k.a. matrice creuse). This change significantly improved both the mechanics and performance of the code.

2. Entity Classes and Projectiles

    I adjusted the constructors and added the necessary attributes for animations. This setup makes it easier to implement new animations and images without redefining attributes for each entity.
    I’ve also created the projectile classes. For now, we only have arrows, but more will follow (e.g., for the keep).

3. Sprites, Image Processing, and Camera View

    Regarding animations, I extracted all the required sprites and coded the necessary functions to handle various sprite types (e.g., static sprites, animated sprite sheets) with predefined zoom levels.
    Simple display functions were created to position elements (e.g., centered or in a corner) using flags.
    A camera and viewport class were introduced to handle 2D plane conversions to 2.5d isometric and allow the player to change their point of view (POV).

4. Globals

    The files GLOBAL_IMPORT.py and GLOBAL_VAR.py now contain the necessary variables and libraries for the codebase.
    GLOBAL_IMPORT.py uses a function from PACKAGE_IMPORT.py to dynamically import libraries. This eliminates the need for writing multiple lines of import statements—work smarter, not harder!

5. MAIN

    I’ve created a small test in the main file to visualize and test current functionality. It’s not perfect, but it works for now:
        Use "P" to zoom in and "O" to zoom out.
        Use your mouse to change the game’s field of view.
        Note: Clicking anywhere on the screen will cause the horse to move to that position, haha. For now, this is a basic test to check the functionality of the move_to_position(self) function.

What to Do Next

    READ THE CODE. Take time to understand the logic behind the animations and how they work. I’ve used clear variable names and organized everything well. If you have any questions, don’t hesitate to ask!

    Group Division:
        One group will work with me on developing the core game mechanics.
        The other group will focus on creating AI strategies for the game. Even though the game isn’t complete yet, you can start drafting the logic and events. Write them in pseudo-code or as clear, step-by-step procedures.

Thank you! 

TERRO Ali ( 0xTristo )