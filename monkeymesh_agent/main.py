#!/usr/bin/env python3
import sys
import argparse
from monkeymesh_agent import config
from monkeymesh_agent.agent import MonkeyAgent

def parse_args():
    parser = argparse.ArgumentParser(description="Run the MonkeyMesh Autonomous Agent Prototype.")
    parser.add_argument(
        "--mode", 
        type=str, 
        choices=["online", "offline"], 
        default="offline", 
        help="Run in offline mock mode or online (future)."
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    print(" === MONKEY MESH PROTOTYPE: THE SPROUT ===")
    print(f" Mode: {args.mode}")
    
    # Configure offline mode based on args
    config.OFFLINE_MODE = (args.mode == "offline")
    
    try:
        agent = MonkeyAgent(use_mock_brain=config.OFFLINE_MODE)
        agent.start()
        
    except KeyboardInterrupt:
        print("\n[Admin] Shutting down agent...")
        sys.exit(0)
    except Exception as e:
        print(f"[Error] Critical agent failure: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
