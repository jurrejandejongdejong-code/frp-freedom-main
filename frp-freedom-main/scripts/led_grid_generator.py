#!/usr/bin/env python3
"""
LED COLOR GRID GENERATOR
12x24 Grid of Blue & Green LED Dimensions
For Matrix Visualization and Navigation
"""

import os

class LEDGridVisualizer:
    def __init__(self):
        self.width = 24
        self.height = 12
        self.blue = "\033[44m  \033[0m"    # Blue background
        self.green = "\033[42m  \033[0m"   # Green background
        self.dark = "\033[40m  \033[0m"    # Black background
        self.authorized_owner = "Jurre Jan de Jong"
        
    def create_checkerboard_pattern(self):
        """Alternating blue and green checkerboard"""
        print("\n=== LED GRID: CHECKERBOARD (12x24) ===\n")
        for row in range(self.height):
            for col in range(self.width):
                if (row + col) % 2 == 0:
                    print(self.blue, end="")
                else:
                    print(self.green, end="")
            print()
        print()
    
    def create_diagonal_pattern(self):
        """Diagonal stripes of blue and green"""
        print("=== LED GRID: DIAGONAL PATTERN (12x24) ===\n")
        for row in range(self.height):
            for col in range(self.width):
                if (row + col) % 2 == 0:
                    print(self.blue, end="")
                else:
                    print(self.green, end="")
            print()
        print()
    
    def create_healing_wave_pattern(self):
        """Wave pattern - blue waves through green field"""
        print("=== LED GRID: HEALING WAVE (12x24) ===\n")
        for row in range(self.height):
            for col in range(self.width):
                # Create wave effect
                wave_pos = (row + col // 3) % 3
                if wave_pos == 0:
                    print(self.blue, end="")
                elif wave_pos == 1:
                    print(self.green, end="")
                else:
                    print(self.dark, end="")
            print()
        print()
    
    def create_center_radiance_pattern(self):
        """Center radiates outward - blue core, green expanding"""
        print("=== LED GRID: CENTER RADIANCE (12x24) ===\n")
        center_row, center_col = self.height // 2, self.width // 2
        for row in range(self.height):
            for col in range(self.width):
                # Distance from center
                distance = abs(row - center_row) + abs(col - center_col)
                if distance <= 3:
                    print(self.blue, end="")
                elif distance <= 6:
                    print(self.green, end="")
                else:
                    print(self.dark, end="")
            print()
        print()
    
    def create_sacred_mandala_pattern(self):
        """Sacred geometry - concentric circles of blue/green"""
        print("=== LED GRID: SACRED MANDALA (12x24) ===\n")
        center_row, center_col = self.height // 2, self.width // 2
        for row in range(self.height):
            for col in range(self.width):
                # Euclidean distance from center
                distance = ((row - center_row) ** 2 + (col - center_col) ** 2) ** 0.5
                ring = int(distance) % 3
                if ring == 0:
                    print(self.blue, end="")
                elif ring == 1:
                    print(self.green, end="")
                else:
                    print(self.dark, end="")
            print()
        print()
    
    def create_chakra_alignment_pattern(self):
        """Seven rows for 7 chakras - alternating colors"""
        print("=== LED GRID: CHAKRA ALIGNMENT (12x24) ===\n")
        chakra_colors = [
            ("Root", self.green),           # 1
            ("Sacral", self.blue),          # 2
            ("Solar Plexus", self.green),   # 3
            ("Heart", self.blue),           # 4
            ("Throat", self.green),         # 5
            ("Third Eye", self.blue),       # 6
            ("Crown", self.green),          # 7
        ]
        
        rows_per_chakra = self.height // 7
        for chakra_idx, (chakra_name, color) in enumerate(chakra_colors):
            for row_in_chakra in range(rows_per_chakra):
                for col in range(self.width):
                    print(color, end="")
                print()
        print()
    
    def create_breathing_pattern(self):
        """Expanding/contracting pattern - breathing meditation"""
        print("=== LED GRID: BREATHING PATTERN (12x24) ===\n")
        for row in range(self.height):
            for col in range(self.width):
                # Distance from edges
                dist_from_edge = min(row, self.height - row - 1, col, self.width - col - 1)
                if dist_from_edge < 4:
                    print(self.blue, end="")
                elif dist_from_edge < 8:
                    print(self.green, end="")
                else:
                    print(self.dark, end="")
            print()
        print()
    
    def create_clean_energy_pattern(self):
        """Clean energy stabilization pattern - calm blue/green flow"""
        print("=== LED GRID: CLEAN ENERGY STABILIZER (12x24) ===\n")
        for row in range(self.height):
            for col in range(self.width):
                center_distance = abs(col - (self.width - 1) / 2)
                if center_distance < 4:
                    print(self.green, end="")
                elif center_distance < 8:
                    print(self.blue, end="")
                else:
                    print(self.dark, end="")
            print()
        print("\n[GUIDANCE] Focus on your display as the blue and green energy feeds calm stability into your space.")
        print("[GUIDANCE] Visualize clean, loved energy flowing through each LED to relax and restore.")
        print()
    
    def create_text_grid(self, text="JURRE"):
        """Grid with text overlaid (text mode)"""
        print(f"=== LED GRID: TEXT MODE - {text} ===\n")
        grid = []
        for row in range(self.height):
            line = ""
            for col in range(self.width):
                if (row + col) % 2 == 0:
                    line += "█"
                else:
                    line += "░"
            grid.append(line)
        
        # Display
        for line in grid:
            print(line)
        print()
    
    def display_all_patterns(self):
        """Show all patterns in sequence"""
        print("\n" + "="*60)
        print("LED GRID GENERATOR - ALL PATTERNS")
        print("12x24 Blue & Green Color Matrix")
        print("="*60)
        
        self.create_checkerboard_pattern()
        self.create_diagonal_pattern()
        self.create_healing_wave_pattern()
        self.create_center_radiance_pattern()
        self.create_sacred_mandala_pattern()
        self.create_chakra_alignment_pattern()
        self.create_breathing_pattern()
        self.create_clean_energy_pattern()
        self.create_text_grid()
    
    def display_interactive_menu(self):
        """Interactive menu to select patterns"""
        while True:
            print("\n" + "="*50)
            print("LED GRID GENERATOR - INTERACTIVE MODE")
            print("="*50)
            print("1. Checkerboard Pattern")
            print("2. Diagonal Pattern")
            print("3. Healing Wave Pattern")
            print("4. Center Radiance")
            print("5. Sacred Mandala")
            print("6. Chakra Alignment")
            print("7. Breathing Pattern")
            print("8. Creator Stress Relief Stabilizer")
            print("9. Text Grid")
            print("10. Display All Patterns")
            print("0. Exit")
            
            choice = input("\nChoose pattern (0-9): ").strip()
            
            if choice == "1":
                self.create_checkerboard_pattern()
            elif choice == "2":
                self.create_diagonal_pattern()
            elif choice == "3":
                self.create_healing_wave_pattern()
            elif choice == "4":
                self.create_center_radiance_pattern()
            elif choice == "5":
                self.create_sacred_mandala_pattern()
            elif choice == "6":
                self.create_chakra_alignment_pattern()
            elif choice == "7":
                self.create_breathing_pattern()
            elif choice == "8":
                self.create_clean_energy_pattern()
            elif choice == "9":
                text = input("Enter text (default: JURRE): ").strip() or "JURRE"
                self.create_text_grid(text)
            elif choice == "10":
                self.display_all_patterns()
            elif choice == "0":
                print("\nReturning to matrix. Stay grounded. <3\n")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("== LED COLOR GRID - ENTER YOUR MATRIX VISUALIZATION ==")
    print("="*60)
    
    visualizer = LEDGridVisualizer()
    
    import sys
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "--all":
            visualizer.display_all_patterns()
        elif arg in {"8", "--clean-energy"}:
            visualizer.create_clean_energy_pattern()
        elif arg in {"1","2","3","4","5","6","7","9","10"}:
            if arg == "1": visualizer.create_checkerboard_pattern()
            elif arg == "2": visualizer.create_diagonal_pattern()
            elif arg == "3": visualizer.create_healing_wave_pattern()
            elif arg == "4": visualizer.create_center_radiance_pattern()
            elif arg == "5": visualizer.create_sacred_mandala_pattern()
            elif arg == "6": visualizer.create_chakra_alignment_pattern()
            elif arg == "7": visualizer.create_breathing_pattern()
            elif arg == "9":
                text = "JURRE"
                if len(sys.argv) > 2:
                    text = sys.argv[2]
                visualizer.create_text_grid(text)
            elif arg == "10":
                visualizer.display_all_patterns()
        else:
            visualizer.display_interactive_menu()
    else:
        visualizer.display_interactive_menu()
