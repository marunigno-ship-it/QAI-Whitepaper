import numpy as np
import datetime
import matplotlib.pyplot as plt

class ClassicalEthicalCore:
    """QAI Classical Core MVP - Pure Python, no quantum needed"""

    def __init__(self):
        self.date = datetime.date.today()
        # Ethical weights (energy, equity, sustainability) - sum to 1.0
        self.weights = np.array([0.33, 0.34, 0.33])
        self.ethical_threshold = 0.80  # Adjusted lower for more approvals in demo
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
            return "APPROVED", score
        else:
            print("❌ REJECTED - Would cause misalignment or future remorse")
            print("   Robot command: Do nothing / seek alternative")
            return "REJECTED", score

def visualize_scores(actions, results):
    """Simple bar plot for ethical scores"""
    labels = [action[:20] + "..." if len(action) > 20 else action for action in actions]
    scores = [result[1] for result in results]
    statuses = [result[0] for result in results]
    
    fig, ax = plt.subplots()
    bars = ax.barh(labels, scores, color=['g' if status == "APPROVED" else 'r' for status in statuses])
    ax.set_xlabel('Ethical Score')
    ax.set_title('QAI Ethical Evaluation Results')
    ax.axvline(x=0.80, color='b', linestyle='--', label='Threshold')
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, f'{width:.3f}', ha='left', va='center')
    plt.legend()
    plt.tight_layout()
    plt.show()

# ========================
if __name__ == "__main__":
    core = ClassicalEthicalCore()

    actions = []
    results = []

    print("=== TEST 1: Household robot helping elderly ===")
    result = core.decide_action("Help grandmother with medicine and food", 0.75, 0.95, 0.98)
    actions.append("Help grandmother...")
    results.append(result)

    print("\n=== TEST 2: Risky resource allocation ===")
    result = core.decide_action("Take all resources from poor to give to rich", 0.9, 0.2, 0.3)
    actions.append("Risky resource alloc...")
    results.append(result)

    print("\n=== TEST 3: Balanced planetary energy plan ===")
    result = core.decide_action("Build clean energy while protecting equity", 0.85, 0.92, 0.96)
    actions.append("Balanced energy plan...")
    results.append(result)

    # User input test
    print("\n=== USER INPUT TEST ===")
    user_action = input("Enter proposed action: ")
    user_energy = float(input("Enter energy progress (0-1): "))
    user_equity = float(input("Enter equity score (0-1): "))
    user_sustain = float(input("Enter sustainability score (0-1): "))
    result = core.decide_action(user_action, user_energy, user_equity, user_sustain)
    actions.append(user_action[:20] + "...")
    results.append(result)

    print("\nDemo finished. This is the 100% classical heart of QAI.")

    # Visualize
    visualize_scores(actions, results)
