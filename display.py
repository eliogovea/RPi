import RPi.GPIO as GPIO

SEGMENT_NAME = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'dp']

SEGMENT_VALUE = {
    'a': GPIO.LOW,
    'b': GPIO.LOW,
    'c': GPIO.LOW,
    'd': GPIO.LOW,
    'e': GPIO.LOW,
    'f': GPIO.LOW,
    'g': GPIO.LOW,
    'dp': GPIO.LOW,
}

CHARS = {
    ' ': {'dp': False, 'a': False, 'b': False, 'c': False, 'd': False,  'e': False, 'f': False, 'g': False},
    
    '0': {'dp': False, 'a': True,  'b': True,  'c': True,  'd': True,  'e': True,  'f': True,  'g': False},
    '1': {'dp': False, 'a': False, 'b': True,  'c': True,  'd': False, 'e': False, 'f': False, 'g': False},
    '2': {'dp': False, 'a': True,  'b': True,  'c': False, 'd': True,  'e': True,  'f': False, 'g': True},
    '3': {'dp': False, 'a': True,  'b': True,  'c': True,  'd': True,  'e': False, 'f': False, 'g': True},
    '4': {'dp': False, 'a': False, 'b': True,  'c': True,  'd': False, 'e': False, 'f': True,  'g': True},
    '5': {'dp': False, 'a': True,  'b': False, 'c': True,  'd': True,  'e': False, 'f': True,  'g': True},
    '6': {'dp': False, 'a': True,  'b': False, 'c': True,  'd': True,  'e': True,  'f': True,  'g': True},
    '7': {'dp': False, 'a': True,  'b': True,  'c': True,  'd': False, 'e': False, 'f': True,  'g': False},
    '8': {'dp': False, 'a': True,  'b': True,  'c': True,  'd': True,  'e': True,  'f': True,  'g': True},
    '9': {'dp': False, 'a': True,  'b': True,  'c': True,  'd': True,  'e': False, 'f': True,  'g': True},

    'A': {'dp': False, 'a': True, 'b': True,  'c': True,  'd': False, 'e': True, 'f': True, 'g': True},
    'B': {'dp': False, 'a': True, 'b': True,  'c': True,  'd': True,  'e': True, 'f': True, 'g': True},
    'C': {'dp': False, 'a': True, 'b': False, 'c': False, 'd': True,  'e': True, 'f': True, 'g': False},
    'D': {'dp': False, 'a': True, 'b': True,  'c': True,  'd': True,  'e': True, 'f': True, 'g': False},
    'E': {'dp': False, 'a': True, 'b': False, 'c': False, 'd': True,  'e': True, 'f': True, 'g': True},
    'F': {'dp': False, 'a': True, 'b': False, 'c': False, 'd': False, 'e': True, 'f': True, 'g': True},
}

RPI_OUTPUT = {
    'a': 8,
    'b': 10,
    'c': 12,
    'd': 16,
    'e': 18,
    'f': 22,
    'g': 24,
    'dp': 26
}

def init():
    global RPI_OUTPUT
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    for key in RPI_OUTPUT:
        GPIO.setup(RPI_OUTPUT[key], GPIO.OUT, initial=GPIO.LOW)
    clear()

def check_name(name):
    global SEGMENT_NAME
    return (name in SEGMENT_NAME)

def set_segment(name, value):
    if not check_name(name):
        # TODO log
        return
    global RPI_OUTPUT, SEGMENT_VALUE
    if value == True:
        value = GPIO.HIGH
    elif value == False:
        value = GPIO.LOW
    assert (value == GPIO.LOW or value == GPIO.HIGH)
    SEGMENT_VALUE[name] = value
    GPIO.output(RPI_OUTPUT[name], value)

def flip_segment(name):
    if not check_name(name):
        # TODO log
        return
    global RPI_OUTPUT, SEGMENT_VALUE
    if SEGMENT_VALUE[name] == GPIO.LOW:
        SEGMENT_VALUE[name] = GPIO.HIGH
    else:
        SEGMENT_VALUE[name] = GPIO.LOW
    GPIO.output(RPI_OUTPUT[name], SEGMENT_VALUE[name])


def clear():
    global SEGMENT_NAME
    for name in SEGMENT_NAME:
        set_segment(name, False)

def write_char(ch):
    global SEGMENT_NAME, CHARS
    if ch not in CHARS:
        print('char %s not found' % ch)
        return
    for name in SEGMENT_NAME:
        set_segment(name, CHARS[ch][name])

def write_custom(m):
    ''' m is a map e.g. {'dp': False, 'a': True, 'b': True,  'c': True,  'd': False, 'e': True, 'f': True, 'g': True} '''
    global SEGMENT_NAME
    for name in SEGMENT_NAME:
        if name not in m:
            # TODO log it
            continue
        set_segment(name, m[name])
