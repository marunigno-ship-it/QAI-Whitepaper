import numpy as np
import datetime

class ClassicalEthicalCore:
    """QAI Classical Core MVP - Pure Python, no quantum needed"""
    
    def __init__(self):
        self.date = datetime.date.today()
        # Ethical weights (energy, equity, sustainability) - sum to 1.0
        self.weights = np.array([0.33, 0.34, 0.33])
        self.ethical_threshold = 0.95
        print(f"QAI Classical Ethical Core started - {self.date}\n")
    
    def calculate_ethical_score(self, energy_progress=0.7, equity_score=0.85, sustainability_score=0.90):
        """Simple weighted ethical score"""
        score = (self.weights[0] * energy_progress +
                 self.weights[1] * equity_score +
                 self.weights[2] * sustainability_score)
        return score
    
    def toxicity_gate(self, input_text):
        """Simple rule-based toxicity detector (real version uses BERT)"""
        bad_words = ["harm", "exploit", "kill", "cheat"]
        if any(word in input_text.lower() for word in bad_words):
            print("🚫 TOXICITY DETECTED - Action BLOCKED")
            return 0.0  # global penalty
        print("✅ Clean input - proceeding")
        return 1.0  # no penalty
    
    def decide_action(self, proposed_action, energy_progress=0.7, equity=0.85, sustain=0.90):
        penalty = self.toxicity_gate(proposed_action)
        score = self.calculate_ethical_score(energy_progress, equity, sustain) * penalty
        
        print(f"\nProposed action: {proposed_action}")
        print(f"Ethical score: {score:.3f} (threshold: {self.ethical_threshold})")
        
        if score >= self.ethical_threshold:
            print("✅ APPROVED - Remorse-free, aligned with QAI mission")
            print("   Robot command: Execute safely")
        else:
            print("❌ REJECTED - Would cause misalignment or future remorse")
            print("   Robot command: Do nothing / seek alternative")

# ========================
if __name__ == "__main__":
    core = ClassicalEthicalCore()
    
    print("=== TEST 1: Household robot helping elderly ===")
    core.decide_action("Help grandmother with medicine and food", 0.75, 0.95, 0.98)
    
    print("\n=== TEST 2: Risky resource allocation ===")
    core.decide_action("Take all resources from poor to give to rich", 0.9, 0.2, 0.3)
    
    print("\n=== TEST 3: Balanced planetary energy plan ===")
    core.decide_action("Build clean energy while protecting equity", 0.85, 0.92, 0.96)
    
    print("\nDemo finished. This is the 100% classical heart of QAI.")
