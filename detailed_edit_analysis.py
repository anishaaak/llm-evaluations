#!/usr/bin/env python3

import difflib
from pathlib import Path

def analyze_transformation_methods():
    # Read the files
    with open("walkthrough.md", 'r') as f:
        original = f.read()
    
    with open("walkthrough_blogpost.md", 'r') as f:
        target = f.read()
    
    # Calculate basic metrics
    original_lines = original.splitlines()
    target_lines = target.splitlines()
    
    # Get detailed diff
    diff = list(difflib.unified_diff(original_lines, target_lines, lineterm=''))
    
    additions = sum(1 for line in diff if line.startswith('+') and not line.startswith('+++'))
    deletions = sum(1 for line in diff if line.startswith('-') and not line.startswith('---'))
    
    print("=== Detailed Transformation Analysis ===\n")
    
    # Method 1: Fixed context file, changing prompts
    print("METHOD 1: Fixed Context File + Changing Prompts")
    print("=" * 50)
    
    # Estimate prompt requirements for transformation
    required_prompts = [
        "Transform technical documentation to blog format with professional title and metadata",
        "Add comprehensive spec-driven development section with examples and best practices", 
        "Enhance prose style from technical to engaging blog writing",
        "Reorganize content flow and add section introductions",
        "Add code examples and detailed explanations",
        "Include professional formatting and styling"
    ]
    
    total_prompt_chars = sum(len(prompt) for prompt in required_prompts)
    
    print(f"Required prompts: {len(required_prompts)}")
    print(f"Estimated prompt complexity: {total_prompt_chars:,} characters")
    print(f"Content transformation needed: {additions + deletions:,} line changes")
    print(f"Total Method 1 effort: {total_prompt_chars + (additions + deletions):,} units\n")
    
    # Method 2: Fixed prompts, changing context file
    print("METHOD 2: Fixed Prompts + Changing Context File")
    print("=" * 50)
    
    # Direct file modifications needed
    file_edits = additions + deletions
    
    print(f"Direct file edits needed: {file_edits:,} line changes")
    print(f"No prompt engineering overhead")
    print(f"Total Method 2 effort: {file_edits:,} units\n")
    
    # Analysis of content changes
    print("CONTENT CHANGE BREAKDOWN")
    print("=" * 30)
    print(f"Lines added: {additions:,}")
    print(f"Lines deleted: {deletions:,}")
    print(f"Net content increase: {len(target_lines) - len(original_lines):,} lines")
    print(f"Character increase: {len(target) - len(original):,} characters\n")
    
    # Key differences analysis
    spec_driven_section = target.find("## Spec-Driven Development")
    spec_driven_end = target.find("## Getting Started")
    spec_driven_content = target[spec_driven_section:spec_driven_end] if spec_driven_section != -1 else ""
    
    print("MAJOR CONTENT ADDITIONS")
    print("=" * 25)
    print(f"Spec-driven development section: {len(spec_driven_content):,} characters")
    print("Blog formatting and metadata")
    print("Enhanced prose and explanations")
    print("Professional styling and organization\n")
    
    # Final comparison
    method1_total = total_prompt_chars + file_edits
    method2_total = file_edits
    
    savings = method1_total - method2_total
    efficiency = (savings / method1_total) * 100
    
    print("FINAL COMPARISON")
    print("=" * 20)
    print(f"Method 1 total effort: {method1_total:,} units")
    print(f"Method 2 total effort: {method2_total:,} units")
    print(f"Method 2 saves: {savings:,} units ({efficiency:.1f}% more efficient)")
    print(f"\nRecommendation: Method 2 (Fixed prompts + changing context file)")
    
    # Practical considerations
    print(f"\nPRACTICAL CONSIDERATIONS")
    print("=" * 25)
    print("Method 1 challenges:")
    print("- Complex prompt engineering required")
    print("- Multiple iterations likely needed")
    print("- Inconsistent results possible")
    print("- Difficult to maintain prompt quality")
    
    print("\nMethod 2 advantages:")
    print("- Direct, predictable edits")
    print("- Full control over content")
    print("- Easier to maintain and update")
    print("- No prompt complexity overhead")

if __name__ == "__main__":
    analyze_transformation_methods()