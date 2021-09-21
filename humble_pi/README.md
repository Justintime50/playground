# Humble Pi

A collection of Raspberry Pi projects.

## Install

**NOTE:** As these projects are for Raspberry Pi, they most likely won't build on another OS.

```bash
# Install locally
make install

# Get Makefile help
make help
```

## Usage

### Stoplight

Turn on red, yellow, and green LEDs like a stoplight, iterating multiple times. Uses pins `4 = red`, `17 = yellow`, and `27 = green`.

```bash
sudo python stoplight.py
```

**Hardware Example**

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/humble-pi/stoplights.jpg" alt="Stoplights">

## Development

```bash
# Lint the project
make lint

# Run tests
make test
```
