
# یک مدل خیلی ساده از اعتماد انسان به هوش مصنوعی

import random

class HumanAITrust:
    def __init__(self):
        self.trust = 0.5   # شروع اعتماد: 50 درصد

    def ai_accuracy(self):
        return random.uniform(0.4, 0.99)

    def update_trust(self, accuracy):
        if accuracy > 0.7:
            self.trust += 0.05
        else:
            self.trust -= 0.05

        self.trust = max(0, min(1, self.trust))

    def run_simulation(self):
        for i in range(10):
            acc = self.ai_accuracy()
            self.update_trust(acc)
        return self.trust


if __name__ == "__main__":
    model = HumanAITrust()
    final_trust = model.run_simulation()
    print("Final Trust Level:", final_trust)

