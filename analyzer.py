from openai import OpenAI
client = OpenAI()

def analyze_logs(log_data):
    prompt = f"""
You are a professional SOC analyst.

Analyze the logs and return structured output:

🚨 ALERT REPORT

Threat Type:
Source IP:
Risk Level (LOW/MEDIUM/HIGH):
Confidence Score (0-100%):

Analysis:
Explain clearly like a cybersecurity analyst.

Recommended Actions:
- Step 1
- Step 2

Logs:
{log_data}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content