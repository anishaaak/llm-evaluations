#!/usr/bin/env python3

import difflib
from pathlib import Path

def levenshtein_distance(s1, s2):
    """Calculate Levenshtein distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def calculate_edit_distances():
    # Read the files
    walkthrough_path = Path("walkthrough.md")
    blogpost_path = Path("walkthrough_blogpost.md")
    
    with open(walkthrough_path, 'r') as f:
        original_content = f.read()
    
    with open(blogpost_path, 'r') as f:
        target_content = f.read()
    
    # Method 1: Fixed context, changing prompts
    # This would require prompts to transform original -> target
    # We estimate this as the difference between original and target
    method1_distance = levenshtein_distance(original_content, target_content)
    
    # Method 2: Fixed prompts, changing context
    # This would require modifying the context file to match target
    # We estimate this as the same distance (original -> target transformation)
    method2_distance = method1_distance  # Same transformation needed
    
    # However, let's consider the practical implementation:
    # Method 1: Need complex prompts to handle the transformation
    # Method 2: Direct file editing
    
    # For Method 1, estimate prompt complexity
    # A prompt to transform technical docs to blog would be ~500-1000 chars
    transformation_prompt = """Transform this technical documentation into a professional blog post with:
1. Add blog-style title and metadata
2. Add comprehensive spec-driven development section
3. Improve prose and readability
4. Enhance organization and flow
5. Add professional formatting
6. Expand explanations with examples
7. Include best practices sections"""
    
    method1_prompt_overhead = len(transformation_prompt)
    
    # Method 2: Direct content modification (just the file changes)
    method2_file_changes = method1_distance
    
    print("=== Edit Distance Analysis ===\n")
    print(f"Original file length: {len(original_content):,} characters")
    print(f"Target file length: {len(target_content):,} characters")
    print(f"Content difference: {len(target_content) - len(original_content):,} characters\n")
    
    print("=== Method Comparison ===")
    print(f"Method 1 (Fixed context, changing prompts):")
    print(f"  - Prompt complexity overhead: {method1_prompt_overhead:,} characters")
    print(f"  - Content transformation distance: {method1_distance:,} edits")
    print(f"  - Total estimated effort: {method1_prompt_overhead + method1_distance:,}\n")
    
    print(f"Method 2 (Fixed prompts, changing context):")
    print(f"  - Direct file modification distance: {method2_file_changes:,} edits")
    print(f"  - No prompt overhead needed")
    print(f"  - Total estimated effort: {method2_file_changes:,}\n")
    
    # Calculate the difference
    difference = (method1_prompt_overhead + method1_distance) - method2_file_changes
    winner = "Method 2" if difference > 0 else "Method 1"
    
    print(f"=== Result ===")
    print(f"Winner: {winner}")
    print(f"Difference: {abs(difference):,} fewer edits")
    print(f"Efficiency gain: {(abs(difference) / max(method1_prompt_overhead + method1_distance, method2_file_changes)) * 100:.1f}%")
    
    # Show a sample of the differences
    print(f"\n=== Sample Differences ===")
    diff = list(difflib.unified_diff(
        original_content.splitlines(keepends=True)[:10],
        target_content.splitlines(keepends=True)[:10],
        fromfile='walkthrough.md',
        tofile='walkthrough_blogpost.md',
        n=3
    ))
    
    for line in diff:
        print(line.rstrip())

if __name__ == "__main__":
    calculate_edit_distances()