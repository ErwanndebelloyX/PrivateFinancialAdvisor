# Private Financial Advisor

This project is an investment advisor that scrapes data from the web, processes it using a Large Language Model (LLM), and generates investment recommendations based on that data. The project is structured as follows:

## Directory Structure

- `src/`: Contains the source code for the project.
  - `main.py`: The entry point of the application.
  - `config.py`: Configuration settings for the project (API keys, URLs, etc.).
  - `scraping/`: Contains the web scraping logic.
    - `scraper.py`: The main scraping class/module.
    - `parsers.py`: Parsing utilities for the scraped data.
    - `utils.py`: Helper functions related to scraping.
  - `processing/`: Contains the data processing and LLM integration logic.
    - `llm_processor.py`: LLM-related processing (e.g., summarization, analysis).
    - `data_cleaning.py`: Data cleaning and pre-processing functions.
    - `analysis.py`: Investment analysis and recommendations logic.
    - `utils.py`: Helper functions for processing.
  - `display/`: Contains the display and visualization logic.
    - `cli.py`: Command-line interface.
    - `web.py`: Web interface (e.g., Flask/Django app).
    - `utils.py`: Helper functions for display.
  - `data/`: Contains the data storage.
    - `raw/`: Raw data from scrapers.
    - `processed/`: Processed data ready for analysis.
    - `models/`: Trained models or vector embeddings.
  - `logs/`: Contains log files for debugging and monitoring.
  - `tests/`: Contains test cases.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.
- `setup.py`: Package installation script.

## Installation

To install the project, run the following command:

```
pip install -r requirements.txt
```

## Usage

To run the project, navigate to the `src/` directory and run the following command:

```
python main.py
```

This will start the web scraping, data processing, and display processes. The results will be displayed in the command-line interface and the web interface.

## Testing

To run the test cases, navigate to the `src/tests/` directory and run the following command:

```
python -m unittest discover
```

This will run all the test cases in the `tests/` directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.