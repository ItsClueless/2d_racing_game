# Final Project: Top Down 2nd Racing Game
Created by: Cal Warshaw, Dwayne Kirby, Jack Page, Walden Ng

Hi! This is a top down racing game built with the pygame module in python,
Try to make it 5 laps without hitting any walls!

## Implementations using pygame

- Player centered camera.
- Collision detection.
- A very simplistic computer to show not to crash into the walls.

## Gameplay
This game has the following components:

- 4 <b>racecars</b> that are red, green, blue and yellow respectively
- A <b>track</b> of size 900x675 in a 1280x720 window
- A track <b>border</b> that spans the length of the track
- 5 invisible <b>checkpoints</b> along the track to ensure that the player completes a whole lap
- 18 invisible <b>points</b> for the computer to follow the track

The game progresses like this:
1. As the car makes its way around the track it hits the checkpoints
2. When all 5 checkpoints are hit and the car passes the finish line, the lap counter is incremented
3. After crossing the finish line on the 6th lap, you have won the game!
4. If at any point your car hit the track wall/border the game will end.

## Rules & Mechanics

- Make it around the track 5 times without crashing
- Do not hit any walls, your car will crash and you will lose!
- Do not the wrong way around the track... you will never finish the game


### Keys
##### (<i>Click the arrow below</i>) 

<details><summary><b>Movement</b></summary>
<p>

<u>Car direction</u>:
- w : move up
- a : move left
- s : move down
- d : move right
- spacebar : boost

<u>Car rotation</u>:
- left arrow key : rotate counter-clockwise
- right arrow key : rotate clockwise

</p>
</details>
