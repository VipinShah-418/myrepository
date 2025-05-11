import requests


generate_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

payload = {
    "name": "Vipin shah",
    "regNo": "REG12347", 
    "email": "vipinshah418@gmai.com"
}

response = requests.post(generate_url, json=payload)
if response.status_code != 200:
    print("Failed to generate webhook:", response.text)
    exit()

data = response.json()
webhook_url = data.get("webhook")
access_token = data.get("accessToken")

print(" Webhook URL:", webhook_url)
print(" Access Token:", access_token)

final_sql_query = """
-- Replace the below query with your actual solution after solving the SQL problem
SELECT doctor_id, COUNT(*) as appointment_count
FROM Appointments
GROUP BY doctor_id
ORDER BY appointment_count DESC
LIMIT 1;
""".strip()

submit_url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submission_payload = {
    "finalQuery": final_sql_query
}

submit_response = requests.post(submit_url, headers=headers, json=submission_payload)

if submit_response.status_code == 200:
    print(" Successfully submitted your query!")
else:
    print(" Submission failed:", submit_response.text)
