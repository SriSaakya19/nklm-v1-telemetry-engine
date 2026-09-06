import numpy as np

class NeuroKineticMatrix:
    def __init__(self, brace_angle=175.3, impact_g=9.3):
        self.brace_angle = brace_angle
        self.impact_g = impact_g

    def compute_asymmetry_index(self, bowling_overs, batting_balls_faced):
        """Calculates workload asymmetry score for all-rounders."""
        # Baseline kinetic stress formula
        bowling_load = bowling_overs * self.impact_g
        batting_load = (batting_balls_faced / 6.0) * 4.2
        
        total_kinetic_workload = bowling_load + batting_load
        
        # Strain index relative to knee brace stiffness threshold (175.0 deg standard)
        knee_stiffness_factor = self.brace_angle / 180.0
        fatigue_risk_index = (total_kinetic_workload / 100.0) * knee_stiffness_factor
        
        return {
            "kinetic_workload_score": round(total_kinetic_workload, 2),
            "fatigue_risk_index": round(fatigue_risk_index, 3),
            "status": "OPTIMAL" if fatigue_risk_index < 0.85 else "HIGH STRAIN WARNING"
        }

if __name__ == "__main__":
    matrix = NeuroKineticMatrix(brace_angle=175.3, impact_g=9.3)
    metrics = matrix.compute_asymmetry_index(bowling_overs=4, batting_balls_faced=28)
    print("--- NKR-18 NEURO-KINETIC MATRIX RESULTS ---")
    print(f"Total Workload Index: {metrics['kinetic_workload_score']}")
    print(f"Fatigue Strain Score: {metrics['fatigue_risk_index']}")
    print(f"Athlete Status: {metrics['status']}")