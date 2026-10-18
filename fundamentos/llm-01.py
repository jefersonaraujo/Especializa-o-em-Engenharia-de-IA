from groq import Groq

client = Groq()

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "Atue como um especialista em machine learning e forneça respostas detalhadas e precisas.",
        },
        {"role": "user", "content": "De forma simples, o que é  machine learning."},
    ],
    temperature=0.5,
    top_p=0.8,
)

print(response.choices[0].message.content)
