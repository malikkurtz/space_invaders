# importing necessary modules
import uvage
import random

# creating camera and screen width and height variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
camera = uvage.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

# loading spaceship sprite sheet and saving it into a variable
ship_images = uvage.load_sprite_sheet('spaceshipsprites.gif', 8, 3)
# creating left and right wall boundries
left_wall = uvage.from_color(0, 0, 'black', 10, 1200)
right_wall = uvage.from_color(SCREEN_WIDTH, 0, 'black', 10, 1200)
# creating a "lost" text box that will appear when the game is over
lost = uvage.from_text(400, 300, 'GAME OVER', 100, 'red')
# loading alien sprite sheet and saving it into a variable
alien_images = uvage.load_sprite_sheet('alienpics.png', 4, 4)
# creating another textbox that will include the key to press to restart the game
restart = uvage.from_text(400, 400, "Press 'R' To Play Again", 50, 'blue')
# creating a list of text boxes for the different levels that will show up at the top right of the screen
levels = [
uvage.from_text(650, 50, 'Level: 1', 50, 'white'),
uvage.from_text(650, 50, 'Level: 2', 50, 'white'),
uvage.from_text(650, 50, 'Level: 3', 50, 'white'),
uvage.from_text(650, 50, 'Level: 4', 50, 'white'),
uvage.from_text(650, 50, 'Level: 5', 50, 'white')
]
# creating a game on variable and setting it to True which will change throughout the game when the player loses
game_on = True
# creating a list of stars that will be random colors drawn from the starcolors list, used in the background
starcolors = ['yellow', 'red', 'blue', 'green', 'cyan', 'magenta']
stars = [
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
    uvage.from_text(random.randint(0, 800), random.randint(0, 600), '*', 35, random.choice(starcolors)),
]
# creating a list of the planets that will scroll through the background of the game
planets = [
    uvage.from_image(random.randint(-100, 900), -1000, 'Planet1.png'),
    uvage.from_image(random.randint(-100, 900), -3000, 'redplanet.png'),
    uvage.from_image(random.randint(-100, 900), -5000, 'purpleplanet.png'),
    uvage.from_image(random.randint(-100, 900), -7000, 'earth.png'),
]
# sizing down the planets
planets[1].scale_by(0.3)
planets[2].scale_by(0.3)
# selects the non-moving image of the ship and saves is as a variable
ship = uvage.from_image(400, 550, ship_images[5])

def reset():
    """
    declares a variety of variables that will be used in the program and when called at the end of the game, resets them
    to their initial values to restart the game
    :return: none
    """
    global totalprojectiles
    global current_frame
    global tickcounter
    global totalaliens
    global totalcoins
    global userscore
    global missile_cooldown
    global alien_frame
    global ship
    # sets ship to middle of camera
    ship.x = SCREEN_WIDTH/2
    # creates an empty list that will be used to store the projectiles on the screen shot by the spaceship
    totalprojectiles = []
    # sets the current frame of the space ship to zero (used to change sprite animation)
    current_frame = 0
    # creates an empty list that will be used to store the aliens on the screen
    totalaliens = []
    # creates a tick counter that counts the ticks as the game goes on (used for moving to different levels, timing of
    # projeciles, etc
    tickcounter = 0
    # creates an empty list that will be used to store the coins that will be added to the screen over time
    # that the user can collect to increase their score
    totalcoins = []
    # creates and sets the variable score to zero
    userscore = 0
    # creates and sets the variable projectile cooldown to zero
    missile_cooldown = 0
    # sets the current frame of the aliens to zero
    alien_frame = 1

def generate_coins():
    """
    creates a coin object using a png image and shrinks it and then appends the coin to the total coins list
    :return: none
    """
    coin = uvage.from_image(random.randint(50, 750), 550, 'img_7.png')
    coin.scale_by(0.05)
    totalcoins.append(coin)

def generate_scenery():
    """
    declares 2 global variables used for generating the background of the game and draws them accordingly
    :return: none
    """
    global scenery
    global planets
    # sets star speeds to 4 and draws them
    for star in stars:
        star.y += 4
        camera.draw(star)
     # if the star moves off the screen, move it back to the top with a random x location
    for star in stars:
        if star.y > SCREEN_HEIGHT:
            star.y = -10
            star.x = random.randint(0, 800)
     # sets planets speed to 20 and draws them
    for planet in planets:
        planet.y += 20
        camera.draw(planet)
        # if the planet moves off the screen, move it 5000 pixels above the window with a random x location
        if planet.y > 2000:
            planet.y = -5000
            planet.x = random.randint(-100, 900)


def draw_coins():
    """
    draws the coins in the total coins list
    :return: none
    """
    # draws each coin in the totalcoins list
    for coin in totalcoins:
        camera.draw(coin)
    # controls bobbing motion of the coins once they spawn
    for coin in totalcoins:
        if tickcounter % 4 == 0:
            if coin.y > 540:
                coin.y -= 4
            else:
                coin.y += 4

def generate_aliens():
    """
    declares 2 global variables, used to add aliens to the list/screen as the function is called
    :return: none
    """
    global totalaliens
    global alien_frame
    # creates a list of aliens that will be added each time the function is called in random x locations within a
    # specified range
    aliens = [
        uvage.from_image(random.randint(50, 100), -26, alien_images[alien_frame]),
        uvage.from_image(random.randint(150, 200), -26, alien_images[alien_frame]),
        uvage.from_image(random.randint(250, 300), -26, alien_images[alien_frame]),
        uvage.from_image(random.randint(350, 400), -26, alien_images[alien_frame]),
        uvage.from_image(random.randint(450, 500), -26, alien_images[alien_frame]),
        uvage.from_image(random.randint(550, 600), -26, alien_images[alien_frame]),
        uvage.from_image(random.randint(650, 700), -26, alien_images[alien_frame]),
    ]
    # resizes the aliens since they are very big in the png image and then adds them to the totalaliens list
    for alien in aliens:
        alien.scale_by(0.3)
        totalaliens.append(alien)

def move_aliens():
    """
    declares 4 global variables that will be used in this function that determines the movement of the aliens
    and their speed according to the level that the player is on
    :return: none
    """
    global totalaliens
    global tickcounter
    global game_on
    global alien_frame
    # depending on how far into the game is, the aliens will move down the screen 10 pixels at a faster rate over time
    for alien in totalaliens:
        if tickcounter < 1000:
            if tickcounter % 20 == 0:
                alien.move(0, 10)
        elif tickcounter < 1500:
            if tickcounter % 15 == 0:
                alien.move(0, 10)
        elif tickcounter < 2000:
            if tickcounter % 12 == 0:
                alien.move(0, 10)
        elif tickcounter < 2500:
            if tickcounter % 7 == 0:
                alien.move(0, 10)
        elif tickcounter >= 2501:
            if tickcounter % 5 == 0:
                alien.move(0, 10)
        # draws each of the aliens in the total aliens list, and if any aliens touches the ship of moves past the bottom
        # of the screen, sets game_on to False to trigger Game Over
        for alien in totalaliens:
            camera.draw(alien)
            if alien.touches(ship) or alien.y > SCREEN_HEIGHT:
                game_on = False



def space_ship():
    """
    declares 8 global variables in this functioin that will be used to determine the movement of the space ship,
    its projectile firing capabilities, and its interaction with other objects in the game
    :return:
    """
    global current_frame
    global totalaliens
    global totalaliens
    global totalprojectiles
    global totalcoins
    global userscore
    global missile_cooldown
    global tickcounter
    # sets a variable to false that will be set to true if the user is pressing the left or right arrow to move the ship
    ship_move = False
    # if the user presses the left or right arrow, the spaceship moves over 10 pixels in that direction
    if uvage.is_pressing('left arrow'):
        ship.x -= 10
        ship_move = True
    if uvage.is_pressing('right arrow'):
        ship.x += 10
        ship_move = True
    # creates a projectile object
    projectile = uvage.from_color(ship.x, 540, "white", 4, 8)
    # if the user presses space and the projectile cooldown is zero, a projectile is appended to the total projectiles
    # list and drawn
    if uvage.is_pressing('space') and missile_cooldown == 0:
        totalprojectiles.append(projectile)
        missile_cooldown = 10
    # mediates the cooldown of the projectiles using the tickcounter
    if tickcounter % 10 == 0:
        while missile_cooldown > 0:
            missile_cooldown -= 1
    # sets speed of projectiles = -20 and draws them
    for projectile in totalprojectiles:
        speed = -20
        projectile.speedy = speed
        projectile.move_speed()
        camera.draw(projectile)
    # keeps ship from going off screen
    if ship.touches(left_wall):
        ship.move_to_stop_overlapping(left_wall)
    if ship.touches(right_wall):
        ship.move_to_stop_overlapping(right_wall)
    # depending of if the ship is moving left or right, the ship will display a corresponding sprite image, otherwise
    # it will default to the non-moving image and then draws it
    if ship_move and uvage.is_pressing('right arrow'):
        current_frame = 5
        ship.image = ship_images[int(current_frame)]
    elif ship_move and uvage.is_pressing('left arrow'):
        current_frame = 6
        ship.image = ship_images[int(current_frame)]
    else:
        ship.image = ship_images[4]
    camera.draw(ship)
    # if the ship touches a coin, add 10 to the score and remove the coin from the total coins list
    for coin in totalcoins:
        if ship.touches(coin):
            totalcoins.remove(coin)
            userscore += 10
    # if the projectile touches an alien, remove both the alien and projectile from their corresponding lists and
    # add 1 to the score
    for projectile in totalprojectiles:
        for alien in totalaliens:
            if projectile.touches(alien):
                totalaliens.remove(alien)
                totalprojectiles.remove(projectile)
                userscore += 1
    # if the projectile goes off screen, remove it from the total projectiles list
    for projectile in totalprojectiles:
        if projectile.y < 0:
            totalprojectiles.remove(projectile)


def tick():
    """
    declares 5 global variables, this function is called every tick in within the game and is used to invoke all other
    function within the game
    :return: none
    """
    global tickcounter
    global totalcoins
    global game_on
    global totalaliens
    global alien_frame
    # removes old images from screen by setting background to black to give illusion of movement
    camera.clear('black')
    # if the game_on variable is True, call generate_scenery(), spaceship(), and move_aliens() functions and add 1 to
    # tickcounter every tick
    if game_on:
        generate_scenery()
        space_ship()
        move_aliens()
        tickcounter += 1
        # determines what levels the user is on depending on the tickcounter and generates the aleins at a specific speed
        # in accordance with the difficulty of the level and draws the level text box object from the list of 5 levels
        if tickcounter < 1000:
            camera.draw(levels[0])
            if tickcounter % 100 == 0:
                generate_aliens()
        elif tickcounter < 1500:
            camera.draw(levels[1])
            if tickcounter % 90 == 0:
                generate_aliens()
        elif tickcounter < 2000:
            camera.draw(levels[2])
            if tickcounter % 80 == 0:
                generate_aliens()
        elif tickcounter < 2500:
            camera.draw(levels[3])
            if tickcounter % 70 == 0:
                generate_aliens()
        elif tickcounter >= 2501:
            camera.draw(levels[4])
            if tickcounter % 60 == 0:
                generate_aliens()
        # calls the generate_coins() function at a specified period of time according to the tickcounter using %
        if tickcounter % 80 == 0:
            generate_coins()
        # draws all the coins
        draw_coins()
    # creates a score object
    score = uvage.from_text(100, 550, "Score: " + str(int(userscore)), 50, 'white')
    # draws the score object
    camera.draw(score)
    # if game_on variable is False (triggered by alien touching ship of moving off screen), draw the lost and restart
    # text boxes and give the option to press 'r' to restart the game without rerrunning by resetting all global variables
    # to their initial values
    if game_on == False:
        camera.draw(lost)
        camera.draw(restart)
        if uvage.is_pressing('r'):
            game_on = True
            reset()
    # displays everying into the window
    camera.display()
# makes sure all variables are set to their initial values each time the game is started
reset()
# calls the tick function 40 times per second
uvage.timer_loop(40, tick)
