# Project Title
Duck Hunt (how original)
> One-sentence tagline describing your pygame experience.
A pygame reaction of Duck hunt with a player uses their mouse to shoot ducks before running out of bullets.
[Optional: drop in a screenshot or GIF of your game here so readers can see what the screen looks like when it opens.]

![screenshot](assets/screenshot.png)

## Description

What is this project? Describe the interactive experience: what kind of game/experience it is, what the player is trying to do, and what makes it interesting. (2 to 4 sentences.)
This project is just a recreation of the game Duck Hunt with a bit of a twist. The player uses the mouse to aim for the ducks with each round the amount of ducks increasing +1 per round, max of 10 rounds. Each round you have an equal amount of bullets to shoot the ducks. If their is zero bullets and still ducks on the screen you lose and get a score. The interesting part is it trains your hand eye co-ordination and their is difficulty to get all 10 rounds. I was actually debating whether to do blackjack or duck hunt.
## How to Run

1. Make sure you have **Python 3.13** installed.
2. Install the dependencies:
   *For most of you, this is just `pip install pygame-ce`.*
3. Run the game:
   ```
   python main.py
   ```

## Controls

| Input | Action |
|-------|--------|
| Mouse / Aim with the crosshair | 
| Spacebar | play again on the game over screen |
| Esc | Quit the game |
| left click | Shoot |

## Features

- [x ] Screen opens to show the environment
- [x ] Elements drawn on the screen  [briefly: what is drawn]
- [ x] User-controlled elements [briefly: what the user controls]
- [ x] [Any extra features you're proud of]

## Dependencies

- Python 3.13
- pygame-ce
- No other PyPL libraries beyond pygame-ce

## Assets

List any images, sounds, fonts, or other files in the `assets/` folder, and where each came from:

assets/Images/duck-right.gif - Duck sprite image
assets/Images/duck-left.gif - Duck sprite image
assets/Images/dog-duck1.png - Dog holding one duck image
assets/Images/dog-duck2.png - Dog holding two ducks image
assets/Images/target.png - Crosshair image
assets/Images/duckhunt-bg-4k.png - Game background image
assets/Images/loading screen.png - Opening loading screen image
assets/Sounds/01. Title BGM(1).mp3 - Menu background music
assets/Sounds/02. GAme A - B Start.mp3 - Start game sound
assets/Sounds/03. Dog.mp3 - Dog sound
assets/Sounds/05. Got a Duck!.mp3 - Hit duck sound
assets/Sounds/06. Clear.mp3 - Round clear sound
assets/Sounds/08. Miss.mp3 - Miss sound
assets/Sounds/10. Game Over.mp3 - Game over sound
assets/Sounds/99 - Gunshot (SFX).mp3 - Gunshot sound
assets/Fonts/game-font.otf - Game font
Audio - https://downloads.khinsider.com/game-soundtracks/album/duck-hunt
Images - can't find where I got them
*(If everything is your own, just say so. Credit anything you didn't make.)*

## Starting Point (Class Code)

State which code from class you used as a starting point, as required by the guardrails:

- Started from `[e.g. 10_pygame_collision.py]` - used for [what part, e.g. the collision-detection loop].
- [Repeat for each piece of class code used, or write "No class code used as a starting point."]
Started from 14_pygame_screens.py -  Learned how to switch from menu to game screen.
Started from 10_pygame_collision.py - Helped me learn how sprite classes, sprite groups, and collisions work.
Started from 11_pygame_shmups.py - Used the most because my game also has moving targets and shooting collisions
Started from 13_pygame_sounds.py - Helped with loading and playing sounds
## AI Disclosure

Disclose code or ideas where AI was used, including the **model** and **line numbers / commits**. Per the rubric, copy-and-pasted AI code is discouraged and, if used, **pasted lines need your own explanation of what it does and why**

You could use the table below or just list using bullets.

**Model(s) used:** [e.g. Claude Opus 4.8, ChatGPT, etc.]

| Lines / Commit | What it does (in my own words) | Why I used it | AI vs. my own |
|----------------|--------------------------------|---------------|---------------|
| `main.py` lines [x-y] / commit [hash] | [explain the code] | [why] | [pasted / adapted / written by me with AI help] |
| Lines / Commit | What it does in my own words | Why I used it | AI vs. my own |
|----------------|------------------------------|---------------|---------------|
| `main.py` lines 26-31 | Loads sounds from my `assets/Sounds` folder. If a sound is missing or broken, it gives back `None` so the game does not crash right away. | Didn't really know how the file paths worked so just used chat to help me. | Adapted with chatgpt help |
| `main.py` lines 93-106 | Makes the crosshair work. loads the target image, shrinks it, gives it a hitbox, and makes it follow my mouse. | Didn't know how to make the actual duck hunt crosshair connect with the mouse| Adapted with chatgpt help |
| `main.py` lines 131-143 | Draws text on the screen using my game font if it works, or Arial if it does not. |  I needed to write out the text and I didn't want to do it so I let chat do it | Adapted with chatgpt help |
| `main.py` lines 146-158 | Makes ducks based on the round number. So round 1 makes 1 duck, round 2 makes 2 ducks, and it keeps going like that. | The game was too easy so I wanted to make it harded but I didn't really know how to add the extra ducks per round | Adapted with chatgpt help |
| `main.py` lines 161-210 | Shows the loading screen first, plays the menu music if it works, and starts the game when the player clicks. | I wanted to have a loading screen and I had the image file so why not use it| Adapted with chatgpt help |
| `main.py` lines 216-246 | Shows the dog after a round is cleared and keeps it there for about 2 seconds. It also plays the dog sound if it loads. | Wanted to show it after each round to make the game feel more sharp. | Adapted with chatgpt help |
| `main.py` lines 333-345 | Checks if my crosshair is touching a duck when I click. If it hits, the duck disappears and my score goes up. If not, it plays the miss sound. | Needed the mouse to actually count as a hit instead of jsut clicking the mouse. | Adapted with chatgpt help |
| `main.py` lines 351-375 | Handles the round ending. If all ducks are gone, it moves on and gives more ducks and bullets. If bullets run out while ducks are still alive, the game ends. | As of making the game harder and have a better leveling system this is the best I could come up with | Adapted with chatgpt help |
*(If no AI was used at all, write "No AI was used in this project." If AI was only used to learn concepts and no code was pasted, say that explicitly.)*

## Known Bugs / Limitations

- Sometimes the bug lags and jitters in the bottom row
- The accuracy of the bullets could be improved further
- No image file game would crash
- Also game sounds sound kinda crappy
## Possible Future Improvements

- Add animated duck frames
- Add a win screen after round 10
- Add more duck patterns
- Make a better leveling and scoring system

## Author

Andrew Huang
