import argparse
import json
import os
from dotenv import load_dotenv
from evaluator.scorer import LLMScorer

load_dotenv()

scorer = LLMScorer()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a response to a question using LLM scorer")
    parser.add_argument("--question", required=True, help="The question to evaluate the response against")
    parser.add_argument("--response", required=True, help="The response to evaluate")

    args = parser.parse_args()

    result = scorer.evaluate(args.question, args.response)
    print(json.dumps(result, indent=2))