import json
from groq import Groq
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY)

# --- PROMPTS ---
ANALYST_SYSTEM_PROMPT = """
You are a Senior Product Manager. Refine the user's vague idea into a concrete list of functional requirements.
"""

ARCHITECT_SYSTEM_PROMPT = """
You are a Chief Software Architect. Output a JSON object with:
- modules (list of strings)
- database_schema (list of objects: {table_name, columns})
- apis (list of objects: {method, endpoint, description})
- tech_stack (list of strings)
"""

class ArchitectureEngine:
    
    @staticmethod
    def agent_analyst(user_input: str) -> str:
        response = client.chat.completions.create(
            model=Config.MODEL_NAME,
            messages=[
                {"role": "system", "content": ANALYST_SYSTEM_PROMPT},
                {"role": "user", "content": f"Refine this: {user_input}"}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

    @staticmethod
    def agent_architect(refined_reqs: str) -> dict:
        response = client.chat.completions.create(
            model=Config.MODEL_NAME,
            messages=[
                {"role": "system", "content": ARCHITECT_SYSTEM_PROMPT},
                {"role": "user", "content": f"Requirements:\n{refined_reqs}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        data = json.loads(response.choices[0].message.content)
        
        # Hybrid Logic Injection
        req_text = refined_reqs.lower()
        if "payment" in req_text or "subscribe" in req_text:
            data['modules'].append("💳 Payment Gateway (Stripe/PayPal)")
        
        return data