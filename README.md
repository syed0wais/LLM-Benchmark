# LLM Code Generation Benchmark

This project provides a simple framework to benchmark the code generation capabilities of various Large Language Models (LLMs) served via Ollama. It allows you to define test cases and evaluate the LLMs' performance based on code execution and other metrics.

## Files

* **`config.json`**: This file contains the configuration settings for the benchmark, including the list of LLMs to test and the path to the test suite.
* **`test_suite.json`**: This file defines the test cases for the benchmark. Each test case includes a prompt, the target language, and (optionally) the expected output.
* **`llm_benchmark.py`**: This Python script executes the benchmark, interacts with Ollama, runs the generated code, evaluates the results, and saves them to a CSV file.

## How It Works

1.  **Configuration (`config.json`)**:
    * You specify the LLMs to benchmark in the `"models"` list. These model names should match the names used in Ollama (e.g., `"codellama:7b-code"`).
    * The `"test_suite_path"` key points to the location of your test suite file (e.g., `"test_suite.json"`).

2.  **Test Suite (`test_suite.json`)**:
    * This file contains a list of test case objects.
    * Each test case object has the following keys:
        * `"prompt"`: The prompt that will be sent to the LLM.
        * `"language"`: The programming language of the generated code (e.g., `"python"`, `"javascript"`, `"c++"`, `"angular"`).
        * `"expected_output"` (Optional): The expected output of the code execution. If provided, the benchmark will compare the actual output to this value.
    * You can add as many test cases as you need.

3.  **Benchmark Execution (`llm_benchmark.py`)**:
    * The script reads the configuration and test suite.
    * For each model in the configuration:
        * It iterates through the test cases.
        * It sends the prompt to Ollama and receives the generated code.
        * It attempts to execute the generated code using the appropriate interpreter or compiler.
        * It evaluates the execution results (success, errors, output comparison).
        * It evaluates the code based on the function `evaluate_code()` or in the case of angular code, the function `evaluate_angular_code()`. You can add more evaluation functions or modify the existing ones for your specific use cases.
        * It stores the results in a list.
    * Finally, it saves the results to a CSV file (`benchmark_results.csv` or `angular_benchmark_results.csv`).

## Usage

1.  **Install Dependencies:**
    * Make sure you have Python 3.6+ installed.
    * Install the `requests` library: `pip install requests`

2.  **Ollama Setup:**
    * Install Ollama and ensure it's running.
    * Pull the LLMs you want to test using `ollama pull <model_name>`.

3.  **Configure the Benchmark:**
    * Edit `config.json` to specify the models and the test suite path.
    * Edit `test_suite.json` to add your test cases.

4.  **Run the Benchmark:**
    * Execute the Python script: `python llm_benchmark.py` (or `python angular_benchmark.py` if you are using angular benchmark file).

5.  **Analyze Results:**
    * The results will be saved in `benchmark_results.csv` or `angular_benchmark_results.csv`. You can open this file with a spreadsheet program or use Python's `pandas` library for analysis.

## Customizing the Benchmark

* **Adding More Languages:**
    * Modify the `execute_code()` function in `llm_benchmark.py` to handle additional programming languages.
* **Adding More Evaluation Metrics:**
    * Modify or create new evaluation functions in `llm_benchmark.py` to assess code quality, efficiency, or other metrics.
* **Changing the Test Suite:**
    * Edit `test_suite.json` to add, modify, or remove test cases.
* **Changing the LLMs:**
    * Edit `config.json` to change the models that are being tested.
* **Changing the output file name:**
    * Modify the `save_results_to_csv()` function to change the name of the output csv file.

## Important Notes

* **Error Handling:** The script includes basic error handling, but you may need to enhance it for specific scenarios.
* **Resource Usage:** Running multiple LLMs can be resource-intensive. Monitor your system's performance.
* **Evaluation Accuracy:** The accuracy of the benchmark depends on the quality of your test suite and evaluation metrics.
* **Ollama Availability:** Ensure that Ollama is running and accessible.
