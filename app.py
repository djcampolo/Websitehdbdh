from flask import Flask, request, jsonify
import openai
import requests
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"
SERPAPI_KEY = "YOUR_SERPAPI_KEY"  # or use Bing or another API

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    medicine = data.get('medicine')

    # Step 1: Search the web
    search_query = f"{medicine} dietary restrictions site:mayoclinic.org OR site:drugs.com OR site:webmd.com"
    search_url = f"https://serpapi.com/search.json?q={search_query}&api_key={SERPAPI_KEY}"

    search_results = requests.get(search_url).json()
    links = [r['link'] for r in search_results.get('organic_results', [])[:3]]

    # Step 2: Gather content (simplified)
    summary_input = f"Summarize the dietary restrictions for the medicine '{medicine}' using information from:\n" + "\n".join(links)

    # Step 3: Use GPT to summarize
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a medical assistant that finds and summarizes dietary restrictions for medicines."},
            {"role": "user", "content": summary_input}
        ],
        max_tokens=300
    )

    result_text = completion['choices'][0]['message']['content']
    return jsonify({"result": result_text})

if __name__ == '__main__':
    app.run(debug=True)
  
