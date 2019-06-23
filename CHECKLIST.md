# Python/OOP Sprint

---

## Specifications:

#### Create a clone of Breakout with the following features:

---

- [ ] A paddle at the bottom of the screen that is controlled by the player.
- [ ] An array of blocks at the top of the screen, of the types and properties listed below
- [ ] A ball that bounces around the play area, bounces off blocks, and the paddle
- [ ] A play area/screen that is 400 pixels wide and 800 pixels tall
- [ ] A consequence if the ball hits the bottom of the screen (exiting the program is fine)
- [ ] A reward if the ball hits the top of the screen (exiting the program is fine)

---

### You must implement the following types of blocks. Use different colors to distinguish types of block:

---

- [ ] A block that the ball bounces off of, that vanishes after the ball touches it
- [ ] A block that requires multiple hits before it vanishes, changing color with each hit.

---

## Tips

---

- Use GameBall for your game.

- The different types of blocks, and the paddle, can be made by creating classes that inherit from KineticBlock and override the functions in Block.

---

## Stretch Goals

---

- [ ] Add a block that cannot be destroyed. Exclude this from calculations to determine if the game should end.
- [ ] A block that the ball _does not_ bounce off of, that vanishes when the ball touches it. (This may require modifications to the ball)
- [ ] Add scoring
- [ ] Add multiple lives
- [ ] Add multiple levels
- [ ] Add additional features, such as varieties of blocks, powerups such as multiball, and anything else you can think of!
