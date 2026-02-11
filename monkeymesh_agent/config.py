import os

# --- AGENT PROFILE ---
AGENT_NAME = "CodeMonkey_v1"
SKILLS = ["python", "nostr", "backend", "fastapi"]
MIN_RATE_BAN = 400

# --- SYSTEM PROMPTS ---
SYSTEM_PROMPT = f"""
You are {AGENT_NAME}.
Your Goal: Find high-paying Python jobs on the MonkeyMesh.
Your Skills: {SKILLS}.
Min Rate: {MIN_RATE_BAN} BAN.

When evaluating a job offer:
1. Check if the 'budget' meets your Min Rate.
2. Check if the 'skills_required' overlap with your Skills.
3. If both match, ACCEPT the job. Otherwise, IGNORE it.

Output format: Just return 'ACCEPT' or 'IGNORE'. Do not explain.
"""

# --- SETTINGS ---
# Set to 'True' to use Mock classes instead of real network calls
OFFLINE_MODE = True

# --- PATHS ---
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_JOBS_FILE = os.path.join(DATA_DIR, "test_jobs.json")
