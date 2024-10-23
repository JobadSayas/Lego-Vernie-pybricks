from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, Remote, Light
from pybricks.parameters import Port, Stop, Button, Color
from pybricks.tools import wait

# INICIALIZAR -------------------------------------------------------

# Initialize the motors.
MotorA = Motor(Port.A);
MotorB = Motor(Port.B);
MotorC = Motor(Port.D);

# Initialize the hub.
hub = MoveHub()
hub.light.on(Color.ORANGE)

# Connect to the remote.
remote = Remote(timeout=None)
remote.light.on(Color.ORANGE)


# VARIABLES --------------------------------------------------------

global speed
speed = 50
global velocidad
velocidad = 1
global modalidad
modalidad = 1
global bailando
bailando = False
global vuelta
vuelta = 40

# MODALIDADES -------------------------------------------------------

# Cambiar modalidad
def cambiarModalidad():
    global modalidad

    if modalidad < 5:
        modalidad += 1
    else:
        modalidad = 1
    
    # Velocidades
    if modalidad is 1:
        remote.light.on(Color.ORANGE)
    # Hablar
    if modalidad is 2:
        remote.light.on(Color.YELLOW)
    # Bailar
    if modalidad is 3:
        remote.light.on(Color.CYAN)
    # Disparo
    if modalidad is 4:
        remote.light.on(Color.RED)
    # Apagar
    if modalidad is 5:
        remote.light.on(Color.NONE) 


# Velocidades
def velocidades():
    global velocidad
    global speed
    global vuelta

    velocidad +=1

    for x in range(velocidad):
        remote.light.on(Color.NONE)
        wait(100)
        remote.light.on(Color.ORANGE)

    if velocidad is 1:
        speed = 50
        vuelta = 40
    if velocidad is 2:
        speed = 100
        vuelta = 50
    if velocidad is 3:
        speed = 150
        vuelta = 75
        velocidad = 0


def apagar():
    MotorC.run_target(500, 0)
    import minBtM


def disparo():
    MotorC.run_target(1000, 105)
    MotorC.run_target(1000, 0)


def hablar():
    MotorC.run_target(500, -20)
    MotorC.run_target(500, 20)
    MotorC.run_target(500, 0, then=Stop.COAST)


def bailar():

    if bailando == False:
        bailando == True
        baile()
    elif bailando == True:
        bailando == False
        

def baile():
    MotorA.run_angle(300, 90, wait=False)
    MotorB.run_angle(300, 90)
    wait(100)
    MotorA.run_angle(300, -90, wait=False)
    MotorB.run_angle(300, -90)
    wait(100)


# CONTROLES ---------------------------------------------------------
while True:
    pressed = remote.buttons.pressed()

    drive_speed_A = 0
    drive_speed_B = 0

    if Button.LEFT_PLUS in pressed:
        drive_speed_A -= speed
        drive_speed_B += speed

    if Button.LEFT_MINUS in pressed:
        drive_speed_A += speed
        drive_speed_B -= speed

    if Button.RIGHT_PLUS in pressed:
        drive_speed_A -= vuelta
        drive_speed_B -= vuelta

    if Button.RIGHT_MINUS in pressed:
        drive_speed_A += vuelta
        drive_speed_B += vuelta

    if Button.CENTER in pressed:
        cambiarModalidad()
        wait(250)

    if Button.RIGHT in pressed:
        if modalidad is 1:
            velocidades()
        if modalidad is 2:
            hablar()
        if modalidad is 3:
            bailar()
        if modalidad is 4:
            disparo()
        if modalidad is 5:
            apagar()
        wait(250)

    if drive_speed_A != 0:
        MotorA.dc(drive_speed_A)
        MotorB.dc(drive_speed_B)
    else:
        MotorA.stop()
        MotorB.stop()

    # Wait.
    wait(10)
