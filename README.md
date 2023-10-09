### What?
This is a project generated by Phind AI in a small experiment by myself to see if it can teach me to get better at python.

It was originally given this context: 
```
Act as a professor and give me projects to learn Python with, one project will be provided until the parameters of the application is complete. You will also act as a tutor while I work on these projects.
```

As well as my Python projects directory, which is looked through to get an idea of what I have already built.

### Okay.. This Project though?
The following is my copypasta from the AI output for this project.

```
User:
I'm ready to begin.
```

```
Phind AI:
Great! I'm glad to hear that you're ready to start learning Python with some hands-on projects. Let's start with a project that will help you understand the basics of Python, such as variables, loops, conditionals, and functions.

Project 1: Text-based Adventure Game

In this project, you'll create a simple text-based adventure game. The game will present the player with a series of choices, and the outcome of the game will depend on the choices the player makes.

Here are the basic requirements for the game:

1. The game has at least three different "rooms" or stages. The player starts in one room and can move to others based on their choices.

2. The player can interact with the game by choosing from a list of options presented at each stage. For example, "You are in a dark room. Do you want to (1) turn on the light, or (2) feel around in the dark?"

3. The game has at least one "win" condition and one "lose" condition.

4. The game uses Python concepts such as variables to keep track of the player's state, loops to handle game progression, conditionals to handle player choices, and functions to organize your code.

Once you have a basic version of the game working, you can add more features if you want, such as:

- More rooms or stages
- More complex interactions and choices
- Random events or choices
- A system for the player to keep track of items or points

Remember, the goal of this project is to practice Python, so focus on using Python concepts and structures effectively, rather than making the game complex or visually impressive.

Feel free to ask me any questions you have while working on this project. I'm here to help!
```

### The Process
Periodically through the development of this project, I will copy all my code into the context and as Instructor Phind how I am doing. In return it will point out different things that I have done, and attempt to understand where I plan to go with the project. So far this has been correct.
It will also point out spelling errors, implementation errors (failed to use variables, functions correctly, etc). It has also been known to tell me that although what I am doing will work, there are easier and better ways to do a thing. It has even gotten onto me about not commenting my code enough, and although it can see what I am doing, that others reading it might not, or even myself if I plan to come back to this project at a later time.

### The Conclusion
After I got it working, and resolved most of the errors (there are probably still more.) This is what I did.

```
User:
So has my codebase met the requirements?
```

```
Phind AI:
Yes, your codebase appears to meet all the basic requirements for the game:

1. Multiple Rooms/Stages: Your game has three rooms (Room 1, Room 2, Room 3) that the player can move between.
2. Player Interaction: The player can interact with the game by using commands like "use", "pickup", "drop", "inspect", and "check". These commands allow the player to interact with items and doors in the rooms.
3. Win/Lose Conditions: The game has a win condition (the player finds the key and unlocks the exit door before time runs out) and a lose condition (the game clock runs out before the player can escape).
4. Use of Python Concepts: Your game uses variables to keep track of the player's state (such as their location and inventory), loops to handle game progression (the main game loop that continues until the game clock runs out), conditionals to handle player choices (the if statements in the parseCommands function), and functions to organize your code (such as the parseCommands function and the methods in your classes).

As for the additional features, your game already includes a system for the player to keep track of items (the player's inventory). If you want to add more features, you could consider adding more rooms or stages, more complex interactions and choices, random events or choices, or a point system.
```

All in all, this was a challenge for me and I spend a lot of time solving my own problems instead of relying on the AI to write everything.
So far I would say its okay. Now on to the next project with the experiment.