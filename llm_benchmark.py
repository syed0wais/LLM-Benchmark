# angular_benchmark.py
import requests
import json
import time
import csv

def load_config(config_path="config.json"):
    with open(config_path, "r") as f:
        return json.load(f)

def load_test_suite(test_suite_path):
    with open(test_suite_path, "r") as f:
        return json.load(f)

def run_ollama(model_name, prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": model_name, "prompt": prompt, "stream": False}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return None

def evaluate_angular_code(generated_code):
    """
    Basic evaluation: checks for common Angular syntax and keywords.
    In a real-world scenario, you'd want more in-depth testing.
    """
    keywords = ["component", "template", "module", "service", "import", "@angular"]
    score = 0
    for keyword in keywords:
        if keyword.lower() in generated_code.lower():
            score += 1

    return score / len(keywords)

def run_benchmark(model_name, test_suite):
    results = []
    for test in test_suite:
        start_time = time.time()
        generated_code = run_ollama(model_name, test["prompt"])
        end_time = time.time()
        generation_time = end_time - start_time

        if generated_code:
            evaluation_score = evaluate_angular_code(generated_code)
            result = {
                "model": model_name,
                "prompt": test["prompt"],
                "generated_code": generated_code,
                "evaluation_score": evaluation_score,
                "generation_time": generation_time,
            }
            results.append(result)
        else:
            results.append({
                "model": model_name,
                "prompt": test["prompt"],
                "generated_code": "Ollama Error",
                "evaluation_score": 0,
                "generation_time": 0,
            })
    return results

def save_results_to_csv(results, output_path="angular_benchmark_results.csv"):
    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

def main():
    config = load_config()
    test_suite = load_test_suite(config["test_suite_path"])
    all_results = []

    for model_name in config["models"]:
        print(f"Benchmarking {model_name}...")
        results = run_benchmark(model_name, test_suite)
        all_results.extend(results)

    save_results_to_csv(all_results)
    print("Benchmark completed. Results saved to angular_benchmark_results.csv")

if __name__ == "__main__":
    main()