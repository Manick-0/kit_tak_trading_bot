# Kit-Tak Trading Bot

This project is an automated trading bot designed to analyze and execute trades across stocks using Python. It implements various trading algorithms such as mean reversion and momentum, coupled with robust risk management tools.

## Features

- Mean Reversion and Momentum trading algorithms
- Backtesting framework for strategy validation
- Integration with AWS for data storage and processing
- Deployment via AWS Lambda

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Manick-0/kit_tak_trading_bot.git
    cd kit_tak_trading_bot
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # For Mac/Linux
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Tests

To run the unit tests, use `pytest`:

```bash
pytest tests/
