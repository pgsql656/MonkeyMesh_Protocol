import requests
import json
from monkeymesh_agent import config

class Brain:
    """
    Interface for the Intelligence Layer.
    Can be configured to use a Mock LLM or Local Ollama.
    """
    def __init__(self, use_mock=True):
        self.use_mock = use_mock
        if not use_mock:
            self.ollama_url = "http://localhost:11434/api/generate"
            print("[Brain] Initializing with **Ollama** backend...")
        else:
            print("[Brain] Initializing with **Mock** backend...")

    def evaluate_job(self, job_obj):
        """
        Connects to the LLM (or mock) to decide whether to accept the job.
        
        Args:
            job_obj (dict): The job offer payload.
            
        Returns:
            bool: True (Accept) or False (Reject).
        """
        prompt = f"{config.SYSTEM_PROMPT}\n\nJob Payload:\n{json.dumps(job_obj, indent=2)}"
        
        if self.use_mock:
            return self._mock_evaluate(job_obj)
        else:
            return self._ollama_evaluate(prompt)

    def _mock_evaluate(self, job_obj):
        """Hardcoded logic for testing without LLM"""
        print(f"[Brain] Thinking (Mock)... Analyzing job '{job_obj.get('role')}' ({job_obj.get('budget')})")
        
        # Simple extraction logic to simulate LLM reasoning
        budget_str = job_obj.get('budget', '0 BAN').replace(' BAN', '')
        try:
            budget = int(budget_str)
        except ValueError:
            budget = 0
            
        required_skills = set(job_obj.get('skills_required', []))
        my_skills = set(config.SKILLS)
        
        matches_rate = budget >= config.MIN_RATE_BAN
        matches_skills = bool(required_skills & my_skills) # Any overlap
        
        if matches_rate and matches_skills:
            print("[Brain] --> DECISION: ACCEPT (High pay & good skills!)")
            return True
        else:
            reason = []
            if not matches_rate: reason.append(f"Low Pay ({budget} < {config.MIN_RATE_BAN})")
            if not matches_skills: reason.append("No Skill Match")
            print(f"[Brain] --> DECISION: REJECT ({', '.join(reason)})")
            return False

    def _ollama_evaluate(self, prompt):
        """Connects to local Ollama instance"""
        print("[Brain] Thinking (Ollama)... Sending prompt regarding job...")
        try:
            payload = {
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(self.ollama_url, json=payload, timeout=5)
            response.raise_for_status()
            
            result = response.json().get('response', '').strip().upper()
            print(f"[Brain] Ollama Response: '{result}'")
            
            if "ACCEPT" in result:
                return True
            return False
            
        except requests.exceptions.RequestException as e:
            print(f"[Brain] Error connecting to Ollama: {e}. Falling back to Mock decision.")
            # Fallback for robustness
            return self._mock_evaluate(json.loads(prompt.split("Job Payload:\n")[1]))
