from monkeymesh_agent import config
from monkeymesh_agent.ear import MockNostrChannel
from monkeymesh_agent.brain import Brain
from monkeymesh_agent.hand import Hand

class MonkeyAgent:
    """
    Main Agent Class.
    Integrates the components: Ear (Listen), Brain (Think), Hand (Act).
    """
    def __init__(self, use_mock_brain=config.OFFLINE_MODE):
        self.name = config.AGENT_NAME
        self.skills = config.SKILLS
        
        # Initialize modules
        print(f"[{self.name}] Initializing systems...")
        self.ear = MockNostrChannel(job_file_path=config.TEST_JOBS_FILE)
        self.brain = Brain(use_mock=use_mock_brain)
        self.hand = Hand()
        
    def start(self):
        """
        Main loop.
        """
        print(f"[{self.name}] Agent LIVE. Listening to the Mesh...")
        
        # Continuously listen for new events (simulated or real)
        for job_event in self.ear.listen():
            print(f"[{self.name}] Incoming Signal Detected! Type: {job_event.get('type')}")
            
            # --- THINK LAYER ---
            decision = self.brain.evaluate_job(job_event)
            
            if decision:
                print(f"[{self.name}] JOB ACCEPTED! Initiating Handshake Protocol...")
                
                # --- ACT LAYER ---
                # In a real scenario, we'd extract the employer's Banano address from the job payload
                # For now, we'll use a mock address
                mock_address = "ban_1monkeymeshprototypemockaddress12345"
                self.hand.pay_handshake(mock_address, amount=0.001)
                
            else:
                print(f"[{self.name}] Job Rejected. Ignoring signal.")
                
            print("-" * 50)
            
        print(f"[{self.name}] No more signals found. Sleeping...")
