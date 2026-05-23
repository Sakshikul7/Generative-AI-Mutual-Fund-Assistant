from transformers import pipeline

# Load lightweight text generation model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

def load_mutual_fund_data():

    with open("data/mutual_funds.txt", "r") as file:
        data = file.read()

    return data

def generate_response(user_query, market_info):

    fund_data = load_mutual_fund_data()

    prompt = f"""
    You are a Financial AI Assistant.

    Market Information:
    {market_info}

    Mutual Fund Knowledge:
    {fund_data}

    User Question:
    {user_query}

    Give a professional and beginner-friendly response.
    """

    response = generator(
        prompt,
        max_length=200,
        num_return_sequences=1
    )

    return response[0]["generated_text"]
