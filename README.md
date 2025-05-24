# Coffee Machine Simulator

A Python-based coffee machine simulator that allows users to order drinks, process coin payments, and manage inventory resources.

## Features

- **Multiple Coffee Options**: Choose from espresso, latte, or cappuccino
- **Coin Processing**: Accept quarters, dimes, nickels, and pennies
- **Inventory Management**: Track water, milk, coffee, and money resources
- **Transaction Handling**: Process payments with change calculation
- **Resource Monitoring**: Check available ingredients before making drinks
- **Administrative Controls**: View resource reports and turn off the machine

## How to Use

1. Run the program to start the coffee machine
2. Choose your drink when prompted: `espresso`, `latte`, or `cappuccino`
3. Insert coins when requested (quarters, dimes, nickels, pennies)
4. Receive your drink and change (if applicable)

### Special Commands

- Type `report` to view current resource levels and money collected
- Type `off` to shut down the coffee machine

## Requirements

- Python 3.x
- `resources.py` file containing the `MENU` and `resources` dictionaries

## Installation

1. Clone this repository
2. Ensure you have the required `resources.py` file with menu and resource data
3. Run the main script:
   ```bash
   python main.py
   ```

## Example Usage

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters? : 3
how many dimes? : 0
how many nickles? : 0
how many pennies? : 0
Here is $0.25 in change.
Here is your latte ☕️. Enjoy!
```

## Project Structure

```
coffeeMachine/
├── main.py    # Main program file
├── resources.py         # Menu and resource definitions
└── README.md           # This file
```

## Contributing

Feel free to fork this project and submit pull requests for any improvements or bug fixes.
