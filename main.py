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
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    FLOOR(DATEDIFF('2025-05-11', e.DOB)/365) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
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
