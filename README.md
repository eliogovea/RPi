# Raspberry Pi + HTTP + 7 Segments Display

Ejemplo para clase.  
Servidor HTTP en un Raspberry Pi para controlar una lampara 7 segmentos.

## Run
```
./main.py
```

## Setup

### Hardware

- Raspberry Pi
- Seven segments display

| Segment | GPIO |
|---------|------|
|a        | 8    |
|b        | 10   |
|c        | 12   |
|d        | 16   |
|e        | 18   |
|f        | 22   |
|g        | 24   |
|dp       | 26   |

**TODO:** add screenshot

## Software

```display.py```
- `init`
- `clear`
- `set_segment`
- `flip_segment`
- `write_char` (0123456789ABCDEF)

### Server

## Screenshots